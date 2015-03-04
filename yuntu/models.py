from django.db import models


class Index(models.Model):
    master_title = models.CharField(max_length=50)
    slave_title = models.CharField(max_length=200)
    about_us_string = models.TextField()
    contact_us_address = models.CharField(max_length=500)
    contact_us_email = models.CharField(max_length=200)

    def __unicode__(self):
        return self.master_title


class FeatureMatrix(models.Model):
    feature_name = models.CharField(max_length=200)
    yuntu_app = models.CharField(max_length=100)
    replay_app = models.CharField(max_length=100)
    meipai_app = models.CharField(max_length=100)
    weishi_app = models.CharField(max_length=100)
    xiaoying_app = models.CharField(max_length=100)
    imovie_app = models.CharField(max_length=100)
    hyperlapse_app = models.CharField(max_length=100)
    weipai_app = models.CharField(max_length=100)
    wopai_app = models.CharField(max_length=100)
    yowo_app = models.CharField(max_length=100)
    musemage_app = models.CharField(max_length=100)

    def __unicode__(self):
        return self.feature_name


class SubscribedEmail(models.Model):
    subscribed_email_address = models.EmailField(null=False, blank=False)
    subscribed_date_time = models.DateTimeField(auto_now_add=True)
    notified = models.BooleanField(default=False)
