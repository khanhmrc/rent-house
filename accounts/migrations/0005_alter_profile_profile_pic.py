# Generated by Django 4.1.3 on 2022-12-29 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_email_profile_name_alter_profile_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='photos/avt_default.png', upload_to='photos/%Y/%m/%d'),
        ),
    ]
