# Generated by Django 3.2.3 on 2021-12-17 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='department',
        ),
    ]
