# Generated by Django 3.1.6 on 2021-06-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctlist', '0007_auto_20210623_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bagahe',
            old_name='buwan',
            new_name='Month',
        ),
        migrations.RenameField(
            model_name='bagahe',
            old_name='CARD_NUMBER',
            new_name='Sex',
        ),
        migrations.RenameField(
            model_name='bagahe',
            old_name='taon',
            new_name='Year',
        ),
        migrations.RemoveField(
            model_name='bagahe',
            name='select',
        ),
        migrations.AddField(
            model_name='bagahe',
            name='card',
            field=models.CharField(max_length=50, null=True),
        ),
    ]