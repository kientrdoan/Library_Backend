# Generated by Django 5.0.3 on 2024-04-30 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='profile_image_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
