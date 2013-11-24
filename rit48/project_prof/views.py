from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from project_prof.models import ProjectPage
from project_prof.forms import ProjectForm

def project_page(request, project_number):
	context = RequestContext(request)
	try:
		project = ProjectPage.objects.get(project_number=project_number)
		s = project.description.split(' ')
		first_s = ""

		if len(s) > 6:
			for i in range(6):
				first_s += (s[i]+" ")
				s.pop()
		else:
			first_s = ' '.join(s)
			s = []


		context_dict = {
				'number': project_number,
				'title': project.title,
				'location': project.location,
				'pitchVid': project.pitchVid,
				'bio': first_s,
				'description': ' '.join(s),
				'team': project.team.__class__.objects.all(),
				'organizer': project.organizer,
				}
	except ProjectPage.DoesNotExist:
		pass
	return render_to_response('rit48/project_page.html', context_dict, context)

def start_project(request):
	context = RequestContext(request)

	created = False
	if request.method == 'POST':
		project_form = ProjectForm(data=request.POST)
		if project_form.is_valid():
			project = project_form.save()
			project.save()
			created = True
		else:
			print project_forms.errors
	else:
		project_form = ProjectForm()
	return render_to_response(
			'rit48/project.html',
			{'project_form': project_form, 'created': created},
			context)
