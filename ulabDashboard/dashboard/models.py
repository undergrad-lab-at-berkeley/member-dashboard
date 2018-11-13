from django.db import models
from django.conf import settings
AUTH_USER_MODEL = settings.AUTH_USER_MODEL

from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import date

# The Member model has a one to one relationship with the User model Django uses for Authentication
# Other Member attributes are accessible through 'self.user.{attribute}' (ex: self.user.first_name)
# A complete list of User attributes is listed at https://docs.djangoproject.com/en/2.1/ref/contrib/auth/
class Member(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    join_date = models.DateField('Date Joined', default=date.today)
    active = models.BooleanField(default=True)
    bio = models.TextField(max_length=300, blank=True, default='')
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)

@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_member(sender, instance, **kwargs):
    instance.member.save()

class Lab(models.Model):
    name = models.CharField(max_length=50)
    directors = models.ManyToManyField(Member, related_name='lab_directors')
    managers = models.ManyToManyField(Member, related_name='lab_managers')
    mentors = models.ManyToManyField(Member, related_name='lab_mentors')
    members = models.ManyToManyField(Member, related_name='lab_members')

    def __str__(self):
        return self.name

class Subgroup(models.Model):
    name = models.CharField(max_length=50)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000, null=True)
    mentors = models.ManyToManyField(Member, related_name='group_mentors')
    members = models.ManyToManyField(Member, related_name='group_members')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000, null=True)
    start_date = models.DateField('Date Started', blank=True, null=True)
    end_date = models.DateField('Date Completed', blank=True, null=True)
    manager = models.ManyToManyField(Member, related_name='managers')
    researchers = models.ManyToManyField(Member, blank=True, related_name='researchers')
    blog_post = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Announcement(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=750)
    date_posted = models.DateTimeField('Date Posted')
    tags = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title