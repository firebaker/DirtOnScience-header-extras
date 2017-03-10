# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderImageCopyrightExtension',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('header_image_source', models.CharField(max_length=20, blank=True)),
                ('header_image_source_url', models.CharField(max_length=255, blank=True)),
                ('header_image_license', models.CharField(max_length=20, blank=True)),
                ('header_image_license_url', models.CharField(max_length=255, blank=True)),
                ('extended_object', models.OneToOneField(to='cms.Page', editable=False)),
                ('public_extension', models.OneToOneField(related_name='draft_extension', to='DirtOnScience_header_extras.HeaderImageCopyrightExtension', null=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeaderOptionsExtension',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('header_subtitle', models.CharField(max_length=20, blank=True)),
                ('extended_object', models.OneToOneField(to='cms.Page', editable=False)),
                ('header_image', filer.fields.image.FilerImageField(blank=True, to='filer.Image')),
                ('public_extension', models.OneToOneField(related_name='draft_extension', to='DirtOnScience_header_extras.HeaderOptionsExtension', null=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
