# Generated by Django 3.2.3 on 2021-12-17 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseRep', '0002_auto_20211216_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklecturehall',
            name='level',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='booklecturehall',
            name='class_rooms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courseRep.classrooms', verbose_name='Lecture Halls'),
        ),
    ]
