from django.db import models

class UserPage(models.Model):
	#top right
        name = models.CharField(max_length=128)
	major = models.CharField(max_length=128)
	location = models.CharField(max_length=256)
	#top left
        bio = models.TextField()
	available = models.CharField(max_length=256)
	dreamTeam = models.ForeignKey(UserPage)
	#middle
        projects = models.ForeignKey(PastProject)
	skills = models.ForeignKey(RankedSkill)
        ranking = models.ForeignKey(Rank)

class PastProject(models.Model):
        name = models.CharField(max_length=128)
        url = models.URLField()
        description = models.TextField()

        def __unicode__(self):
                return self.name

class RankedSkill(models.Model):
	skill = models.CharField(max_length=80)
	rank = models.IntegerField(default=0, max_value=5)
	endorse = models.IntegerField(default=0)

class Rank(models.Model):
	stars = models.IntegerField(max_value=5)
	comment = models.TextField()
