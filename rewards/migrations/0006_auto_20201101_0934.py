# Generated by Django 3.1.2 on 2020-11-01 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0005_auto_20201031_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilePic',
            field=models.ImageField(null=True, upload_to='profile/'),
        ),
    ]