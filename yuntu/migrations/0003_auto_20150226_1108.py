# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('yuntu', '0002_index_about_us_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='contact_us_address',
            field=models.CharField(default=datetime.datetime(2015, 2, 26, 11, 8, 10, 744118, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='index',
            name='contact_us_email',
            field=models.CharField(default=datetime.datetime(2015, 2, 26, 11, 8, 18, 202740, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
