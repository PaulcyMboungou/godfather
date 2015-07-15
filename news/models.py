from django.db import models

class Location(models.Model):
	country = models.CharField(primary_key=True, max_length= 150)

class User(models.Model):
	user_name = models.CharField(max_length= 100)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField()
	location = models.ForeignKey(Location)

class Article(models.Model):
	article_title = models.CharField(primary_key= True, max_length=500)
	article_content = models.TextField(blank=True)
	pub_date = models.DateTimeField('date published')