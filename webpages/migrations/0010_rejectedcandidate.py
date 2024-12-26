# Generated by Django 5.1.3 on 2024-12-24 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0009_alter_jobposting_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RejectedCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_to_reject', models.CharField(choices=[('Lack of Required Skills', 'Lack of Required Skills'), ('Insufficient Experience', 'Insufficient Experience'), ('Overqualification', 'Overqualification'), ('Cultural Misfit', 'Cultural Misfit'), ('Poor Communication Skills', 'Poor Communication Skills'), ('Inadequate Problem-Solving Abilities', 'Inadequate Problem-Solving Abilities'), ('Unprepared for Interviews', 'Unprepared for Interviews'), ('Unprofessional Behavior', 'Unprofessional Behavior'), ('Negative Attitude', 'Negative Attitude'), ('Inconsistent Information', 'Inconsistent Information'), ('Salary Expectations Misalignment', 'Salary Expectations Misalignment'), ('Location Constraints', 'Location Constraints'), ('Availability Issues', 'Availability Issues'), ('Visa/Work Authorization Challenges', 'Visa/Work Authorization Challenges'), ('Position Closure', 'Position Closure'), ('Hiring Freeze', 'Hiring Freeze'), ('Better Fit Identified', 'Better Fit Identified'), ('Negative Background Check', 'Negative Background Check'), ('Legal or Compliance Issues', 'Legal or Compliance Issues'), ('Conflict of Interest', 'Conflict of Interest')], max_length=255)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.candidateprofile')),
            ],
        ),
    ]
