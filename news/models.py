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
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=MyUserManager.normalize_email(email),
			# username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(email,
			# username=username,
			password=password,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

	def get_by_natural_key(self, username):
		return self.get(**{self.model.USERNAME_FIELD: username})


class MyUser(AbstractBaseUser):
	"""
	Custom user class.
	"""
	username = models.CharField('Username', max_length=100, blank=True, unique=True)
	email = models.EmailField('email address', unique=True, db_index=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	last_name = models.CharField(max_length=50, blank=True)
	first_name = models.CharField(max_length=50 , blank=True)
	joined = models.DateTimeField(auto_now_add=True , null=True)
	MatriculeNo = models.OneToOneField(MatriculeNo, blank=True, null=True)

	USERNAME_FIELD = 'email'

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


class Article(models.Model):
	article_title = models.CharField(max_length=500)
	# image = models.ImageField(upload_to=None, heigth_field=None, width_field=None, max_length=100)
	article_content = models.TextField(blank=True)
	pub_date = models.DateTimeField('date published')
	# image = models.ImageField(upload_to="news/images")
	likes = models.BooleanField(default=False)
	author = models.CharField(max_length=50, blank=True)
	image = models.ImageField(upload_to='Images/%Y/%m/%d', blank=True)
	video = EmbedVideoField(blank=True)

	def __str__(self):
		return self.article_title
