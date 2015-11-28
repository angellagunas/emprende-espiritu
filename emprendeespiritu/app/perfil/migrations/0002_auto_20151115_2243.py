# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.FileField(upload_to=b'perfil/%Y/%m/%d', null=True, verbose_name='profile picture', blank=True),
        ),
    ]
