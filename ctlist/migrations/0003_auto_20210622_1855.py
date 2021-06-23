# Generated by Django 3.1.6 on 2021-06-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctlist', '0002_bagahe_select'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='Message',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='User',
        ),
        migrations.AddField(
            model_name='suggestion',
            name='Code',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='Date',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='Price',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='Quantity',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='Rent',
            field=models.CharField(choices=[('Jeep', 'Jeep'), ('Cementery', 'Cementery')], default='none', max_length=50),
        ),
    ]