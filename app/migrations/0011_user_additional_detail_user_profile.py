# Generated by Django 3.2.8 on 2022-03-30 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_additional_detail',
            name='user_profile',
            field=models.ImageField(default=1, upload_to='app/userprofile/'),
            preserve_default=False,
        ),
    ]
