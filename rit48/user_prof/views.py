from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from user_prof.forms import UserForm
from user_prof.models import UserPage

def register(request):
	context = RequestContext(request)

	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print user_form.errors
	else:
		user_form = UserForm()
	return render_to_response(
			'rit48/index.html',
			{'user_form': user_form, 'registered': registered},
			context)

def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				guy = UserPage.objects.get(user=user)
				s = "/user/"+str(guy.user_number)
				return HttpResponseRedirect(s)
			else:
				return HttpResponse("Your account is disabled")
		else:
			#"ethically" wrong? :p
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invaild login details")
	else:
		#this might change 
		return render_to_response('rit48/login.html', {}, context)

def profile_page(request, user_number):
	context = RequestContext(request)
	try:
		user = User.objects.get(pk=int(user_number))
		user_page = UserPage.objects.get(user=user)

		context_dict = {
				'name': user.username,
				'major': user_page.major,
				'location': user_page.location,
				'bio': user_page.bio,
				'available': user_page.available,
				'team': user_page.user.__class__.objects.all(),
				'projects': user_page.projects.__class__.objects.all(),
				'skills': user_page.skills.__class__.objects.all(),
				'rank': user_page.ranking.__class__.objects.all(),
				}

	except UserPage.DoesNotExist:
		pass

	return render_to_response('rit48/user.html', context_dict, context)

def projects(request):
	context = RequestContext(request)
	pass
