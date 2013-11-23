from django.db import models
#from user_prof import TeamMember

class PastProject(models.Model):
        name = models.CharField(max_length=128)
        url = models.URLField()
        description = models.TextField()

        def __unicode__(self):
                return self.name

class ProjectPage(models.Model):
	#splash bar
        title = models.CharField(max_length=128)
	typeOfProject = None
	location = models.CharField(max_length=256)
	#bottom
        pitchVid = models.URLField()
        description = models.TextField()
        #team = models.ForeignKey(TeamMember)

class Team(models.Model):
	roleName = models.CharField(max_length=128)
	roleDesc = models.TextField()
#	requirements = models.ForeignKey()
