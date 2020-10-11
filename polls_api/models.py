from django.db import models
import os,binascii
from rest_framework import serializers

class AnonymousPerson(models.Model):
    uuid = models.CharField(max_length=128, unique=True, blank=True, primary_key=True)

    def save(self, *args, **kwargs):
        self.uuid = binascii.hexlify(os.urandom(20)).decode()
        super(AnonymousPerson, self).save(*args, **kwargs)

    def __str__(self):
        return self.uuid

class Quiz(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256, null=True)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(null=True)
    questions = models.ManyToManyField('Question', related_name='questions', blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    TYPES={
        (1, 'By text'),
        (2, 'Choose one'),
        (3, 'Choose many'),
    }
    text = models.CharField(max_length=128, unique=True)
    qtype = models.IntegerField(choices=TYPES, null=False)
    choices = models.ManyToManyField('AnswerChoice', related_name='choices', blank=True)

    def __str__(self):
        return self.text

class AnswerChoice(models.Model):
    choice = models.CharField(max_length=128)

    def __str__(self):
        return self.choice

class PassedQuiz(models.Model):
    uuid = models.ForeignKey('AnonymousPerson', on_delete=models.CASCADE)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.CharField(max_length=128, null=False)

    def __str__(self):
        return '{}, {}'.format(self.uuid, self.quiz)
