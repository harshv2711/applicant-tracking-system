# Generated by Django 5.1.3 on 2024-12-19 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_alter_shortlistedcandidatetimeline_timeline_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortlistedcandidatetimeline',
            old_name='timeline_name',
            new_name='timeline_title',
        ),
    ]
