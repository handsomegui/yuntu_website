from django.db import models


class Index(models.Model):
    master_title = models.CharField(max_length=50)
    slave_title = models.CharField(max_length=200)
    about_us_string = models.TextField()
    contact_us_address = models.CharField(max_length=500)
    contact_us_email = models.CharField(max_length=200)

    def __unicode__(self):
        return self.master_title
