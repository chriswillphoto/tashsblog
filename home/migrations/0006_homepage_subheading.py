# Generated by Django 2.0.4 on 2018-04-21 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180415_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='subheading',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
