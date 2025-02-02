# -*- coding: utf-8 -*-

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=140)),
                ('done', models.BooleanField(default=False)),
                ('done_time', models.DateTimeField(null=True, blank=True)),
                ('deadline', models.DateField(null=True, blank=True)),
                ('business_line', models.ForeignKey(to='incidents.BusinessLine', on_delete=models.deletion.CASCADE)),
                ('category', models.ForeignKey(to='incidents.IncidentCategory', on_delete=models.deletion.CASCADE)),
                ('incident', models.ForeignKey(to='incidents.Incident', on_delete=models.deletion.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
