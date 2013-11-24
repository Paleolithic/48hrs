from django import forms
from project_prof.models import ProjectPage

class ProjectForm(forms.ModelForm):
	title = forms.CharField(max_length=128)
	location = forms.CharField(max_length=256)
	pitchvid = forms.URLField()
	description = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = ProjectPage

		fields = ('title', 'location', 'pitchvid', 'description')
