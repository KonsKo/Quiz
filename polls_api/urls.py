from django.urls import path, include
from polls_api.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('gettoken/', obtain_auth_token),
    path('auth/', include('rest_framework.urls')),

    path('new_user/', PersonCreateView.as_view()),
    path('<str:uuid>/quiz/<int:quiz>/question/<int:question>/<str:answer>/', QuizPassView.as_view()),
    path('<str:uuid>/quiz/all/', QuizUserListView.as_view()),

    path('quiz/all/', QuizListView.as_view()),
    path('quiz/new/', QuizCreateView.as_view()),
    path('quiz/<int:pk>/', QuizDetailView.as_view()),

    path('question/all/', QuestionListView.as_view()),
    path('question/<int:pk>/', QuestionDetailView.as_view()),
    path('question/new/', QuestionCreateView.as_view()),
]