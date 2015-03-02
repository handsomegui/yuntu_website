# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('yuntu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='about_us_string',
            field=models.TextField(default=datetime.datetime(2015, 2, 26, 10, 1, 3, 527745, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
