# Generated by Django 4.0.4 on 2022-06-16 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='msg',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Name',
            new_name='name',
        ),
    ]
