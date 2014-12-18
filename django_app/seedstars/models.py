from django.db import models

# Create your models here.
class SeedStarsUser(models.Model):
    name = models.CharField(
                    "The user's name",
                    max_length=100
                    )
    email = models.EmailField(
                    "The user's email",
                    unique=True,
                    )
    class Meta:
        ordering = ['-name']

    def __unicode__(self):
        return "{0} , {1}".format(self.name, self.email)

