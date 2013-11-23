from django.db import models
from django.contrib.auth.models import User

class PastProject(models.Model):
        name = models.CharField(max_length=128)
        url = models.URLField()
        description = models.TextField()

        def __unicode__(self):
                return self.name

class RankedSkill(models.Model):
	skill = models.CharField(max_length=80)
	rank = models.IntegerField(default=0)
	endorse = models.IntegerField(default=0)

class Rank(models.Model):
	stars = models.IntegerField()
	comment = models.TextField()

class UserPage(models.Model):
	user = models.OneToOneField(User)

	#top right
	major = models.CharField(max_length=128)
	location = models.CharField(max_length=256)
	#top left
        bio = models.TextField()
	available = models.CharField(max_length=256)
	dreamTeam = models.ForeignKey('UserPage')
	#middle
        projects = models.ForeignKey('PastProject')
	skills = models.ForeignKey('RankedSkill')
        ranking = models.ForeignKey('Rank')

	def __unicode__(self):
		return self.user.username
