# Generated by Django 5.1.1 on 2024-10-05 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0020_delete_attendancestudent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
