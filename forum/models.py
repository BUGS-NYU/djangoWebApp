from django.db import models

# Create your models here
# creating the table for the web app.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    detail = models.TextField(blank=True)

    def __str__(self):
        # the name of the user will be the name in the database
        return self.name