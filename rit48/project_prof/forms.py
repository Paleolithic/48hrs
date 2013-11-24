from django import forms
from project_prof.models import ProjectPage

class ProjectForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Project name")
	location = forms.CharField(max_length=256, help_text="Location")
	pitchvid = forms.URLField()
	description = forms.CharField(widget=forms.Textarea, help_text="description")

	class Meta:
		model = ProjectPage

		fields('title', 'location', 'pitchvid', 'description')
