# Generated by Django 4.0.3 on 2022-04-16 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_service_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]