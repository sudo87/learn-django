# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the project name', verbose_name='name', max_length=100)),
                ('color', models.CharField(default='#fff', help_text='Enter the hex color code, like #ccc or #cccccc', verbose_name='color', validators=[django.core.validators.RegexValidator('(^#[0-9a-fA-F]{3}$)|(^#[0-9a-fA-F]{6}$)')], max_length=7)),
                ('user', models.ForeignKey(verbose_name='user', related_name='projects', to='taskmanager.Profile')),
            ],
            options={
                'verbose_name': 'Project',
                'ordering': ('user', 'name'),
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('user', 'name')]),
        ),
    ]
