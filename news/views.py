import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import UserManager

# from .forms import SignupForm


from .models import MyUser, Location, Article, MatriculeNo

def home(request):
	# c = {}
	# c.update(csrf(request))
	template = loader.get_template('home.html')
	context = RequestContext(request, {
			# c,
		})

	return HttpResponse(template.render(context))

def login(request):
	if request.method == 'POST':
		email = request.POST.get('email', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(email=email , password=password)

		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/account')
		else:
			return HttpResponse('invalid details. Try again')

	message = "Welcome back ! Login and Discuss with Your Congolese's Brothers"
	template = loader.get_template('login.html')
	context = RequestContext(request, {
        'message':message
 		})

	return HttpResponse(template.render(context))

def loggedin(request):
	template = loader.get_template('loggedin.html')
	context = RequestContext(request, {
 		})

	return HttpResponse(template.render(context))
	
def register(request):
	subtitle = 'Please Register !'
	location_list = Location.objects.all()
	country_name = [liste.country for liste in location_list]
	number_list = MatriculeNo.objects.all()
	unique_number = [number.No for number in number_list]
	# user = User.objects.get(id=User_id)
	# User.location = user

	if request.method == 'POST':
		username = request.POST.get('username', '')
		lastname = request.POST.get('lastname', '')
		firstname = request.POST.get('firstname', '')
		email = request.POST.get('email', '')
		# matricule = [request.POST.get('matricule')]

		# if len(matricule) == 0:
		# 	error = "The matricule your entered is not valid"
		# else:
		# 	error = "valid"

		user = MyUser.objects.create(
		username = username,
			first_name = firstname,
			last_name = lastname,
			email = email,
			# MatriculeNo = matricule
			# location = country
		  )

		if user is not None:
			return HttpResponseRedirect('POST Success')
		else:
			return HttpResponseRedirect('Failed to Register !')

	# else:
	# 	return HttpResponseRedirect('/')
		

	template = loader.get_template('register.html')
	context = RequestContext(request, {
		'subtitle': subtitle,
		'location_list': location_list,
		'country_name' : country_name,
		'number_list': number_list,
		'unique_number': json.dumps(unique_number),
		# 'error' : error
		# 'form' : SignupForm()
	})


	return HttpResponse(template.render(context))

def logout(request):
	message = "You have successfully logged out !"
	auth.logout(request)
	template = loader.get_template('logout.html')
	context = RequestContext(request, {
         'message': message
		})
	return HttpResponse(template.render(context))

def articles(request):
	title = 'Breaking News'
	list_of_articles = Article.objects.all()
	template = loader.get_template('articles.html')
	context = RequestContext(request, {
		'title': title,
		'list_of_articles': list_of_articles
		})

	return HttpResponse(template.render(context))

def article(request, article_id=1):
	chosen_article = Article.objects.get(id=article_id)
	template = loader.get_template('article.html')
	context = RequestContext(request, {
		'chosen_article': chosen_article
		})

	return HttpResponse(template.render(context))

def media(request):
	template = loader.get_template('media.html')
	context = RequestContext(request, {

		})

	return HttpResponse(template.render(context))

# def clean_password2(self):
# 	# Check that the two password entries match
# 	password1 = self.cleaned_data.get("password1")
# 	password2 = self.cleaned_data.get("password2")
# 	if password1 and password2 and password1 != password2:
# 		raise ValueError('Passwords dont match')
# 	return password2

# def save(self, commit=True):
# 	# Save the provided password in hashed format
# 	u = MyUser.objects.get(username=username)
# 	u.set_password(self.cleaned_data["password1"])
# 	u.save()
