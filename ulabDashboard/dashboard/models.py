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
    about = models.TextField(max_length=750, blank=True, default='')
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    @property
    def full_name(self):
      if self.user.first_name and self.user.last_name:
        return f'{self.user.first_name} {self.user.last_name}'
      else:
        return self.user.username

    @property
    def status(self):
      if self.active:
        return 'Active'
      else:
        return 'Inactive'

    def __str__(self):
      if self.user and self.user.username:
        return self.user.username
      else:
        return 'MEMBER OBJECT HAS NO OBJECT USER'

@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)

@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_member(sender, instance, **kwargs):
    instance.member.save()

class Lab(models.Model):
    name = models.CharField(max_length=50)
    # directors = models.ManyToManyField(Member, related_name='lab_directors')
    managers = models.ManyToManyField(Member, related_name='lab_managers')
    mentors = models.ManyToManyField(Member, related_name='lab_mentors')
    members = models.ManyToManyField(Member, related_name='lab_members')

    def __str__(self):
        return self.name

class Subgroup(models.Model):
    name = models.CharField(max_length=50)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=2500, null=True)
    active = models.BooleanField(default=True)
    mentors = models.ManyToManyField(Member, related_name='group_mentors')
    members = models.ManyToManyField(Member, related_name='group_members')

    @property
    def status(self):
      if self.active:
        return 'Active'
      else:
        return 'Inactive'

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=2500, null=True)
    start_date = models.DateField('Date Started', blank=True, null=True)
    end_date = models.DateField('Date Completed', blank=True, null=True)
    managers = models.ManyToManyField(Member, related_name='managers')
    researchers = models.ManyToManyField(Member, blank=True, related_name='researchers')
    blog_post = models.URLField(null=True, blank=True)
    in_progress = models.BooleanField(default=True)

    @property
    def status(self):
      if self.in_progress:
        return 'In Progress'
      else:
        return 'Completed'

    @property
    def short_description(self):
        if len(self.description) >= 103:
          return f'{self.description[:100]}...'
        else:
          return self.description

    def __str__(self):
        return self.name

class Announcement(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2500)
    date_posted = models.DateTimeField('Date Posted')
    tags = models.TextField(max_length=200, null=True, blank=True)

    @property
    def short_description(self):
        if len(self.description) >= 253:
          return f'{self.description[:250]}...'
        else:
          return self.description

    def __str__(self):
        return self.title

class ExecutiveRelationship(models.Model):
    student = models.ForeignKey(Member, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    SP, FA = "SPRING", "FALL"
    semester_choices = ( (SP, "Spring"), (FA, "Fall") )
    semester = models.CharField(max_length=32, choices=semester_choices, default=FA)
    year = models.IntegerField(blank=True, null=True)

    @property
    def semester_active(self):
        return f'{self.semester} {self.year}'

    def __str__(self):
        return f'{self.semester_active} {self.lab} {self.position} - {self.student.full_name}'
