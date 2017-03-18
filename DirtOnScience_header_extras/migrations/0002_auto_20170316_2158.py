# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DirtOnScience_header_extras', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headerimagecopyrightextension',
            name='extended_object',
        ),
        migrations.RemoveField(
            model_name='headerimagecopyrightextension',
            name='public_extension',
        ),
        migrations.AddField(
            model_name='headeroptionsextension',
            name='header_image_license',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='headeroptionsextension',
            name='header_image_license_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='headeroptionsextension',
            name='header_image_source',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='headeroptionsextension',
            name='header_image_source_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='headeroptionsextension',
            name='header_subtitle',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.DeleteModel(
            name='HeaderImageCopyrightExtension',
        ),
    ]
