# Generated by Django 3.1.6 on 2021-04-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, null=True)),
                ('Essential', models.CharField(max_length=30, null=True)),
                ('Quantity', models.CharField(max_length=20, null=True)),
                ('Address', models.CharField(max_length=50, null=True)),
                ('Payment', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
