from django.db import models

class Booklog(models.Model):
	name = models.CharField(max_length=100 ,verbose_name='نام کتاب')
	page = models.CharField(max_length=20,null=True,blank=True,unique=False,verbose_name='شماره صفحه')

	def __str__(self):
	    return self.name
