# Generated by Django 5.1.3 on 2024-12-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0019_rename_last_ctc_candidateprofile_ctc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='ctc',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
