# Generated by Django 4.0.1 on 2022-01-21 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0007_internshipregistration_currentdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internshipregistration',
            old_name='currentdate',
            new_name='reg_date',
        ),
    ]
