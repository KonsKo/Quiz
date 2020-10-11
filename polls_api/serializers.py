from rest_framework import serializers
from polls_api.models import *
from django.utils import timezone

class ChoicesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerChoice
        fields = ['choice']

class QuestionDetailSerializer(serializers.ModelSerializer):
    qtype = serializers.CharField(source='get_qtype_display')
    choices = ChoicesDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = '__all__'

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def validate_choices(self, value):
        data = self.get_initial()
        qtype = int(data.get('qtype'))
        if qtype == 2 or qtype ==3:
            if len(value) < 1:
                raise serializers.ValidationError('You entered no choices for question')
        return value

class QuizDetailSerializer(serializers.ModelSerializer):
    questions = QuestionDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = '__all__'


class QuizCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

    def validate_date_finish(self, value):
        if value < timezone.now():
            raise serializers.ValidationError('Finish date has to be greater current date')
        return value

class PersonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousPerson
        fields = ['uuid']

class QuizPassSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassedQuiz
        fields = ['uuid', 'quiz', 'question', 'answer']

    def validate_answer(self, value):
        data = self.get_initial()
        num = PassedQuiz.objects.filter(uuid=data.get('uuid'), quiz=data.get('quiz'), question=data.get('question')).count()
        if num > 0:
            raise serializers.ValidationError('Answer < {} >: User {} already answered for question {} in quiz {}'.format(
                                                value, data.get('uuid'), data.get('question'), data.get('quiz')))

        question = Question.objects.get(pk=data.get('question'))
        if question.qtype == 3 or question.qtype == 2:
            choices = list(question.choices.all().values_list('choice', flat=True))
            if value not in choices:
                raise serializers.ValidationError('Your answer not in choices. Available answer options{}'.format(choices))

        return value

class QuizUserListSerializer(serializers.ModelSerializer):
    quiz = serializers.StringRelatedField()
    question = serializers.StringRelatedField()
    class Meta:
        model = PassedQuiz
        fields = ['uuid', 'quiz', 'question', 'answer']





