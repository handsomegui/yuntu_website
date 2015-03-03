# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuntu', '0003_auto_20150226_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureMatrix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feature_name', models.CharField(max_length=200)),
                ('yuntu_app', models.CharField(max_length=100)),
                ('replay_app', models.CharField(max_length=100)),
                ('meipai_app', models.CharField(max_length=100)),
                ('weishi_app', models.CharField(max_length=100)),
                ('xiaoying_app', models.CharField(max_length=100)),
                ('imovie_app', models.CharField(max_length=100)),
                ('hyperlapse_app', models.CharField(max_length=100)),
                ('weipai_app', models.CharField(max_length=100)),
                ('wopai_app', models.CharField(max_length=100)),
                ('yowo_app', models.CharField(max_length=100)),
                ('musemage_app', models.CharField(max_length=100)),
            ],
        ),
    ]
