from django.db import models

class PastProject(models.Model):
        name = CharField(max_length=128)
        url = models.URLField()
        description = models.TextField()

        def __unicode__(self):
                return self.name

class ProjectPage(models.Model):
        name = models.CharField( max_length=128 )
        pitchVid = models.URLField()
        description = TextField()
        team = models.ForeignKey(TeamMember)
        ranking = None
