# Generated by Django 3.1.7 on 2022-08-09 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_comment_parent_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='question',
        ),
    ]
