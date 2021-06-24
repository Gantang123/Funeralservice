# Generated by Django 3.1.6 on 2021-06-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctlist', '0006_auto_20210623_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='casket',
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.CharField(choices=[('Wooden Casket', 'Item1'), ('Metal Casket', 'Item2'), ('Imported Casket ', 'Item3')], default='Item1', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(choices=[('size1', 'Length: 78 inches Width: 23 inches'), ('size2', 'Length: 75 inches Width: 22 inches'), ('size3', 'Length: 83 inches Width: 28 inches'), ('size4', 'Length: 85 inches Width: 38 inches'), ('size5', 'Length: 60 inches Width: 11 inches')], default='size1', max_length=100),
        ),
    ]
