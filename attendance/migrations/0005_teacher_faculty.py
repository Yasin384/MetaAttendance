# Generated by Django 5.1.1 on 2024-10-01 01:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_remove_teacher_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='attendance.faculty'),
        ),
    ]
