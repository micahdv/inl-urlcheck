from django.db import models

# Create your models here.

class Post(models.Model):
	id = models.AutoField(primary_key=True)
	domain = models.CharField(max_length=120)
	content_type = models.TextField()
#	title = models.CharField(max_length=120)
	url = models.CharField(max_length=350)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	request_count = models.IntegerField()	

	def __unicode__(self):
		return self.id
