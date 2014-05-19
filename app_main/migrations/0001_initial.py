# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassPl',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('z', models.ForeignKey(to='app_main.ClassPh', to_field='id')),
            ],
            options={
                'unique_together': set([('name', 'z')]),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClassPh',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClassPg',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('z', models.ManyToManyField(to='app_main.ClassPh')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
