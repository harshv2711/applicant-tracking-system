# Generated by Django 5.1.3 on 2024-12-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0013_candidateprofile_resume_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='resume_file',
            field=models.FileField(blank=True, default='default.pdf', null=True, upload_to='candidate-resume'),
        ),
    ]
