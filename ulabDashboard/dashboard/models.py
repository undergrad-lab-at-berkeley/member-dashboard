from django.db import models

# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    join_date = models.DateTimeField('date published')
    active = models.BooleanField()
#     question_text = models.CharField(max_length=200)