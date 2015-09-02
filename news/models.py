from django.contrib.auth.models import ( 
	BaseUserManager, AbstractBaseUser
)
from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils import timezone
from django.contrib.auth.hashers import (
	check_password, is_password_usable, make_password,
)
from django.utils.crypto import get_random_string, salted_hmac

class Location(models.Model):
	country = models.CharField(max_length= 150)

	def __str__(self):
		return self.country

class MatriculeNo(models.Model):
	No = models.IntegerField()

	def __str__(self):
		return self.No


class MyUserManager(BaseUserManager):
	use_in_migrations = True

	def create_user(self, username, email=None, password=None):
		if not username:
			raise ValueError('The given username must be set')
		email = self.normalize_email(email)
		user = self.model(
			username = username,
			email=email
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, password):
		user = self.create_user(username, email,
			password=password,
		)
		user.is_admin = True
		# user.is_staff = True
		# user.is_superuser = True
		user.save(using=self._db)
		return user

class MyUser(AbstractBaseUser):
	"""
	Custom user class.
	"""
	username = models.CharField('Username', max_length=100, unique=True, db_index=True)
	email = models.EmailField('email address',)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	last_name = models.CharField(max_length=50, blank=True)
	first_name = models.CharField(max_length=50 , blank=True)
	joined = models.DateTimeField(auto_now_add=True , null=True)
	MatriculeNo = models.OneToOneField(MatriculeNo, blank=True, null=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = MyUserManager()

	def __unicode__(self):
		return self.username

	def get_full_name(self):
		fullname = self.first_name+" "+self.last_name
		return self.fullname

	def get_short_name(self):
		return self.first_name

	@property
	def is_superuser(self):
		return self.is_admin

	@property
	def is_staff(self):
		return self.is_admin

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return self.is_admin

	def is_authenticated(self):
		"""
		Always return True. This is a way to tell if the user has been
		authenticated in templates.
		"""
		return True

class Comment(models.Model):
	comment = models.TextField()

# class Like(models.Model):
# 	likes = models.IntegerField()


class Article(models.Model):
	article_title = models.CharField(max_length=500)
	# image = models.ImageField(upload_to=None, heigth_field=None, width_field=None, max_length=100)
	article_content = models.TextField(blank=True)
	pub_date = models.DateTimeField('date published')
	# image = models.ImageField(upload_to="news/images")
	likes = models.IntegerField(blank=True, default=0)
	author = models.CharField(max_length=50, blank=True)
	image = models.ImageField(upload_to='Images/%Y/%m/%d', blank=True)
	comment = models.ManyToManyField(Comment)
	video = EmbedVideoField(blank=True)

	def __str__(self):
		return self.article_title
