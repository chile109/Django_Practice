# Generated by Django 2.2.24 on 2021-06-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(default='kevin@aktsk.com', max_length=254),
        ),
    ]
