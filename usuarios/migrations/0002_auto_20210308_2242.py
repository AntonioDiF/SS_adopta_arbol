# Generated by Django 3.1.3 on 2021-03-09 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='apellido_materno',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='apellido_paterno',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='nombre',
        ),
    ]