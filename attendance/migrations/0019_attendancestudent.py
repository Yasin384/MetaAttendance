# Generated by Django 5.1.1 on 2024-10-05 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0018_alter_attendance_status_alter_student_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('faculty_id', models.BigIntegerField()),
                ('profile_id', models.BigIntegerField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
