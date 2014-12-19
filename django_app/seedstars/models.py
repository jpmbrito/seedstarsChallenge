from django.db import models

# Create your models here.
class SeedStarsUser(models.Model):
    name = models.CharField(
                    max_length=100,
                    help_text="Name : "
                    )
    email = models.EmailField(
                    unique=True,
                    help_text="Email : "
                    )
    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return "{0} , {1}".format(self.name, self.email)

