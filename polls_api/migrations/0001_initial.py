# Generated by Django 3.1.2 on 2020-10-05 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousPerson',
            fields=[
                ('uuid', models.CharField(blank=True, max_length=128, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128)),
                ('qtype', models.IntegerField(choices=[(3, 'Choose many'), (2, 'Choose one'), (1, 'By text')])),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('description', models.CharField(max_length=256, null=True)),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('date_finish', models.DateTimeField(null=True)),
                ('questions', models.ManyToManyField(blank=True, related_name='questions', to='polls_api.Question')),
            ],
        ),
        migrations.CreateModel(
            name='PassedQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=128)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls_api.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls_api.quiz')),
                ('uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls_api.anonymousperson')),
            ],
        ),
    ]
