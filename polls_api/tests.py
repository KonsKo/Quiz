from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from polls_api.models import *

class QuizTestAdminCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='foo',password='1234', is_staff=True)
        self.token = Token.objects.create(user=self.user)
        self.api_authenticate()

    def api_authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_quiz_date_finish_greater_current(self):
        data = {"title": "test1", "date_finish": "2030-10-10T14:48:32.698430Z"}
        response = self.client.post("/api/v1/quiz/new/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_update_delete_quiz_only_admin(self):
        data = {"title": "test1",}
        response = self.client.post("/api/v1/quiz/new/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        url = "/api/v1/quiz/" + str(response.json().get('id')) +"/"
        data = {"title": "test1_new", }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class QuizTestCase(APITestCase):

    def test_create_quiz_only_admin_not_anyone(self):
        data = {"title": "test1",}
        response = self.client.post("/api/v1/quiz/new/", data)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_not_admin_could_not_update_and_delete_quiz(self):
        quiz = Quiz.objects.create(title='title')
        url = "/api/v1/quiz/" + str(quiz.id) + "/"
        data = {"title": "test1_new", }
        response = self.client.patch(url, data)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.delete(url)
        self.assertNotEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class QuestionTestAdminCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='foo',password='1234', is_staff=True)
        self.token = Token.objects.create(user=self.user)
        self.api_authenticate()

    def api_authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_update_delete_question_only_admin(self):
        data = {"text": "test1", "qtype": 1}
        response = self.client.post("/api/v1/question/new/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        url = "/api/v1/question/" + str(response.json().get('id')) +"/"
        data = {"text": "test1_new", }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_question_with_choices_for_type_1_and_2(self):
        data = {"text": "test1", "qtype": 2}
        response = self.client.post("/api/v1/question/new/", data)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        ac = AnswerChoice(choice='choice')
        ac.save()
        data['choices']= ac.id
        response = self.client.post("/api/v1/question/new/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class QuestionTestCase(APITestCase):

    def test_create_question_only_admin_not_anyone(self):
        data = {"text": "test1", "qtype": 1}
        response = self.client.post("/api/v1/question/new/", data)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_not_admin_could_not_update_and_delete_question(self):
        question = Question.objects.create(text='test', qtype=1)
        url = "/api/v1/question/" + str(question.id) + "/"
        data = {"text": "test1_new", }
        response = self.client.patch(url, data)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.delete(url)
        self.assertNotEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class QuizPassCase(APITestCase):

    def test_pass_quiz(self):
        anon_user = AnonymousPerson.objects.create()
        Choice1 = AnswerChoice.objects.create(choice='Choice1')
        Question1 = Question.objects.create(text='Question1', qtype=1)
        Question2 = Question.objects.create(text='Question1', qtype=2)
        Question2.choices.add(Choice1)
        Question2.save()
        #Question3 = Question.objects.create(text='Question1', qtype=3, choices=Choice)
        Quiz1 = Quiz.objects.create(title='Quiz1')
        Quiz1.questions.add(Question1,Question2)
        url = "/api/v1/" + str(anon_user.uuid) + "/quiz/" + str(Quiz1.id) + "/question/" + str(
            Question2.id) + "/" + "OtherAnswer" + "/"
        response = self.client.post(url)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        url = "/api/v1/" + str(anon_user.uuid) + "/quiz/" + str(Quiz1.id) + "/question/" + str(
            Question2.id) + "/" + "Choice1" + "/"
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)