from django.db import models
from django.contrib.auth.models import User
#from user_prof import TeamMember

class TeamMember(models.Model):
	user = models.OneToOneField(User)
	roleName = models.CharField(max_length=128)
	roleDesc = models.TextField()
	#requirements = models.ForeignKey()

	def __unicode__(self):
		return self.user.username

class ProjectPage(models.Model):
	#splash bar
        title = models.CharField(max_length=128)
	typeOfProject = None
	location = models.CharField(max_length=256)
	#bottom
        pitchVid = models.URLField()
        description = models.TextField()
        team = models.ForeignKey(TeamMember, blank=True, null=True)
	organizer = models.OneToOneField(User, blank=True, null=True)

	def __unicode__(self):
		return self.title
