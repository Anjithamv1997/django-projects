# Generated by Django 2.2.4 on 2019-08-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=6),
        ),
    ]
