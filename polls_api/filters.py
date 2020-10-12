import django_filters
from polls_api.models import Quiz

class QuizFilter(django_filters.FilterSet):
    class Meta:
        model = Quiz
        fields = {
            'title': ['contains',],  # or icontains
            'description': ['contains',],  # or icontains
        }