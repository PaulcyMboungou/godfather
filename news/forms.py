from django import forms

from django.forms import ModelForm
# from .models import User

# class SignupForm(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ['user_name', 'first_name', 'last_name', 'email', 'location']

# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		email_base, provider = email.split('@')
# 		domain, extension = provider.split('.')
# 		if not extension == "com":
# 			raise forms.ValidationError("Please enter a valid email address !")
# 		return email