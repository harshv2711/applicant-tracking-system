# Generated by Django 5.1.3 on 2024-12-19 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_rename_timeline_name_shortlistedcandidatetimeline_timeline_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortlistedcandidatetimeline',
            old_name='timeline_comment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='shortlistedcandidatetimeline',
            old_name='timeline_title',
            new_name='comment_title',
        ),
    ]