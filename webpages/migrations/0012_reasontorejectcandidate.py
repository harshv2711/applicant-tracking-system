# Generated by Django 5.1.3 on 2024-12-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0011_rejectedcandidate_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReasonToRejectCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255)),
            ],
        ),
    ]