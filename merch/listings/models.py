from django.db import models

class Ref(models.Model):
	gtin = models.fields.CharField(max_length=100)
	expiration_date = models.fields.DateField()

	def __str__(self):
		return f'{self.gtin}'

# Create your models here.
