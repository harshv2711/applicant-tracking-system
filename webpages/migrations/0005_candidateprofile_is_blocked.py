# Generated by Django 5.1.3 on 2024-12-16 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_candidateproject_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofile',
            name='is_blocked',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
