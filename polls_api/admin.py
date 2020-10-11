from django.contrib import admin
from polls_api.models import *

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(AnonymousPerson)
admin.site.register(PassedQuiz)
admin.site.register(AnswerChoice)

# Register your models here.
