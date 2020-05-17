from django.db import models



class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	pdf    = models.FileField(upload_to="mag/")
	cover  = models.ImageField(upload_to="mag/cover/", null=True, blank=True)

	def __str__(self):
		return self.title


	def delete(self,*args, **kwargs):
		self.pdf.delete()
		self.cover.delete()
		super().delete(*args, **kwargs)
		