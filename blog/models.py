from django.db import models
from datetime import datetime


# Create your models here.

class BlogPost(models.Model):
	author = models.CharField(max_length=1024)
	date = models.DateTimeField(default=datetime.now)
	title = models.CharField(max_length=1024)
	content = models.TextField()
	imageUrl = models.URLField(default="http://i.imgur.com/DtJyTkB.jpg")


	def __str__(self):
		return self.title

