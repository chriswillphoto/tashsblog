# Generated by Django 2.0.4 on 2018-04-15 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='body',
            new_name='what',
        ),
    ]
