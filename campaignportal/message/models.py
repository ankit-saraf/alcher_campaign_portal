from django.db import models
from django.utils import timezone
# Create your models here.
class Message(models.Model):
    message=models.TextField(default="")
    admin_approved=models.BooleanField(default="False")
    pub_date= models.DateTimeField(default="2000-06-03 03:08:50.262391")

    def __str__(self):
        return self.message[:20]

class socialMessage(models.Model):
	message=models.TextField(default="")
	imglink=models.TextField(default="",null=True, blank=True)
	admin_approved=models.BooleanField(default="False")
	
	def __str__(self):
		return self.message[:20]