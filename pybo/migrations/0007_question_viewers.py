# Generated by Django 3.1.7 on 2022-08-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='viewers',
            field=models.IntegerField(default=0),
        ),
    ]