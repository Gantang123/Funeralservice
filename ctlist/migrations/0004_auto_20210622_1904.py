# Generated by Django 3.1.6 on 2021-06-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctlist', '0003_auto_20210622_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestion',
            old_name='Code',
            new_name='Gantangproduct',
        ),
        migrations.RenameField(
            model_name='suggestion',
            old_name='Date',
            new_name='Gantangproduct2',
        ),
        migrations.RenameField(
            model_name='suggestion',
            old_name='Price',
            new_name='Product_Category',
        ),
        migrations.RenameField(
            model_name='suggestion',
            old_name='Quantity',
            new_name='Product_Category2',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='Rent',
        ),
        migrations.AddField(
            model_name='suggestion',
            name='Radio',
            field=models.CharField(choices=[('chkYes', 'chk'), ('chkYess', 'chk')], default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='price',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='price2',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='quantity',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='quantity2',
            field=models.CharField(default='none', max_length=50),
        ),
    ]