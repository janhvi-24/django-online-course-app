from django.db import models
from django.conf import settings

class Question(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    grade = models.IntegerField(default=5)

    def __str__(self):
        return self.content

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content

class Submission(models.Model):
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
