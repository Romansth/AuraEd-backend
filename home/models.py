from django.db import models
from django.utils import timezone
# Create your models here.
class Achievements(models.Model):
	title = models.CharField(max_length=100)
	value = models.IntegerField()

	def __str__(self):
		return self.title

class Blogs(models.Model):
	thumbnail = models.ImageField(upload_to='blog-thumbnail')
	writer = models.CharField(default='AuraEd',max_length=50)
	date_posted = models.DateTimeField(default=timezone.now)
	title = models.CharField(default='blank',max_length=200)
	blog_content = models.TextField(default='40 words')
	link = models.CharField(default="https://auraed.medium.com/",max_length=200)

	def __str__(self):
		return self.title

class Albums(models.Model):
	location = models.CharField(default='Kathmandu',max_length=50)
	image = models.ImageField(upload_to='albums')
	img_filter = models.TextField(default='all for all,hpde for digital literacy,sprinkle for child education and spray for workshop',max_length=100)

	def __str__(self):
		return self.location

class Teams(models.Model):
	name = models.CharField(default='',max_length=50)
	photo = models.ImageField(upload_to='team')	
	position = models.CharField(default='Member',max_length=50)
	facebook = models.CharField(default='#',max_length=150)
	twitter = models.CharField(default='#',max_length=150)
	linkedin = models.CharField(default='#',max_length=150)
	github = models.CharField(default='#',max_length=150)
	website = models.CharField(default='#',max_length=150)
	description = models.CharField(default='2 or 3 words',max_length=150)


	def __str__(self):
		return self.name