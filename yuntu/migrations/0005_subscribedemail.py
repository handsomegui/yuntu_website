# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuntu', '0004_featurematrix'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribedEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subscribed_email_address', models.EmailField(max_length=254)),
                ('subscribed_date_time', models.DateTimeField(auto_now_add=True)),
                ('notified', models.BooleanField(default=False)),
            ],
        ),
    ]
