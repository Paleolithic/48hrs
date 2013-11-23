from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from user_prof.forms import UserForm
from user_prof.models import UserPage

def index(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.errors
	else:
		return render_to_response('rit48/index.html', {}, context)


def userPage(request, user_name):
	context = RequestContext(request)
	try:
		user = UserPage.objects.get(name=user_name)

		context_dict = {
				'name': user.name,
				'major': user.major,
				'location': user.location,
				'bio': user.bio,
				'available', user.available,
				'team': user.UserPage_set.all()
				'projects': user.PastProject_set.all()
				'skills': user.RankedSkill_set.all()
				'rank': user.Rank_set.all()
				}

	except UserPage.DoesNotExist:
		pass

	return render_to_response('rit48/user.html', context_dict, context)
