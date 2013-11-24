from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
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
			print user.forms.errors
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
				return HttpResponse('/projects/')
			else:
				return HttpResponse("Your account is disabled")
		else:
			#"ethically" wrong? :p
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invaild login details")
	else:
		#this might change 
		return render_to_response('/login.html', {}, context)

def profile_page(request, user_number):
	context = RequestContext(request)
	try:
		user = UserPage.objects.get(user_number=user_number)

		context_dict = {
				'name': user.name,
				'major': user.major,
				'location': user.location,
				'bio': user.bio,
				'available': user.available,
				'team': user.UserPage_set.all(),
				'projects': user.PastProject_set.all(),
				'skills': user.RankedSkill_set.all(),
				'rank': user.Rank_set.all(),
				}

	except UserPage.DoesNotExist:
		pass

	return render_to_response('rit48/user.html', context_dict, context)

def projects(request):
	context = RequestContext(request)
	pass
