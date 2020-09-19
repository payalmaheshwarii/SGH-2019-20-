from django.db import models

class patients(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    class Meta:
        db_table = 'patients'

