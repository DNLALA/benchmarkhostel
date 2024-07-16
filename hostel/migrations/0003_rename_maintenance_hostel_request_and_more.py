# Generated by Django 4.1.7 on 2024-07-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_hostel_issues_hostel_maintenance_hostel_reports_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostel',
            old_name='maintenance',
            new_name='request',
        ),
        migrations.AddField(
            model_name='hostel',
            name='request_status',
            field=models.CharField(blank=True, choices=[('pending', 'pending'), ('processing', 'processing'), ('successful', 'successful')], max_length=255, null=True),
        ),
    ]
