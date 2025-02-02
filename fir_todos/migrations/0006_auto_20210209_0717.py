# Generated by Django 3.1.6 on 2021-02-09 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0011_auto_20210208_2156'),
        ('fir_todos', '0005_auto_20160119_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolisttemplate',
            name='detection',
            field=models.ForeignKey(blank=True, limit_choices_to={'group__name': 'detection'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='incidents.label'),
        ),
        migrations.AlterField(
            model_name='todolisttemplate',
            name='todolist',
            field=models.ManyToManyField(blank=True, limit_choices_to={'incident__isnull': True}, to='fir_todos.TodoItem'),
        ),
    ]
