# Generated by Django 2.2.5 on 2019-09-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_track_track_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='track_album',
            field=models.CharField(default='Unknown Album', max_length=100),
        ),
    ]