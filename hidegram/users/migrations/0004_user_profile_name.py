# Generated by Django 2.0.4 on 2018-04-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180411_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_name',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]