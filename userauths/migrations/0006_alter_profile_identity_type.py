# Generated by Django 5.0.3 on 2024-04-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0005_alter_profile_identity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='identity_type',
            field=models.CharField(blank=True, choices=[("Driver's License Number", "Driver's License Number"), ('National Identications Number', 'National Identity Number'), ('Other', 'Other'), ('Passport Number', 'Passport Number')], max_length=200, null=True),
        ),
    ]
