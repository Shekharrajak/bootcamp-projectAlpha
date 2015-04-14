from django.db import models

# Create your models here.
class Member(models.Model):
	name=models.CharField(max_length=128)
	rno=models.IntegerField()
	branch=models.CharField(max_length=128)
	email=models.CharField(max_length=256)

	def __unicode__(self):
		return str(self.name)