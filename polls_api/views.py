from rest_framework import generics
from polls_api.models import Quiz, Question
from polls_api.serializers import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from polls_api.filters import QuizFilter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

@permission_classes([IsAdminUser])
class QuizCreateView(generics.CreateAPIView):
    serializer_class = QuizCreateSerializer

#@permission_classes([IsAdminUser])
class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    #filter_backends = [filters.SearchFilter]
    #search_fields = ('description', 'title',)
    #filter_fields = ('title',)
    #filterset_fields = ['title', 'description',]
    filterset_class = QuizFilter

@permission_classes([IsAdminUser])
class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizCreateSerializer

@permission_classes([IsAdminUser])
class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer

@permission_classes([IsAdminUser])
class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionCreateSerializer

@permission_classes([IsAdminUser])
class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer

class PersonCreateView(generics.CreateAPIView):
    serializer_class = PersonCreateSerializer

class QuizPassView(generics.CreateAPIView):
    serializer_class = QuizPassSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=kwargs)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class QuizUserListView(generics.ListAPIView):
    serializer_class = QuizUserListSerializer

    def get_queryset(self):
        uuid = self.kwargs['uuid']
        return PassedQuiz.objects.filter(uuid=uuid)
