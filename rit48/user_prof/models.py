from django.db import models

class UserPage(models.Model):
        name = models.CharField( max_length=128 )
        pitchVid = models.URLField()
        selfDescription = models.TextField()
        projects = models.ForeignKey(PastProject)
	skills = models.ForeignKey(RankedSkill)
        ranking = None
        picture = None

class PastProject(models.Model):
        name = CharField(max_length=128)
        url = models.URLField()
        description = models.TextField()

        def __unicode__(self):
                return self.name

class RankedSkill(models.Model):
	skill = CharField(max_length=80)
	rank = IntegerField(default=0)
