from django.db import models

# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    join_date = models.DateTimeField('Date Joined')
    active = models.BooleanField()
    bio = models.TextField(max_length=300)
    # linkedin = models.URLField(null=True)
    # github = models.URLField(null=True)
    # website = models.URLField(null=True)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    executives = models.ManyToManyField(Member, related_name='executives')
    members = models.ManyToManyField(Member, related_name='members')

    def __str__(self):
        return self.name

class Lab(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000, null=True)
    start_date = models.DateTimeField('Date Started', null=True)
    end_date = models.DateTimeField('Date Completed', null=True)
    manager = models.ManyToManyField(Member, related_name='managers')
    researchers = models.ManyToManyField(Member, related_name='researchers')
    # blog_post = models.URLField(initial='https://medium.com/undergraduate-laboratory-berkeley')

    def __str__(self):
        return self.name

class Announcement(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    bio = models.TextField(max_length=750)
    date_posted = models.DateTimeField('Date Posted')
    tags = models.TextField(max_length=200)

    def __str__(self):
        return self.title