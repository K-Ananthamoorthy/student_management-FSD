# Generated by Django 5.1.1 on 2024-10-15 16:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0003_course_student_email_student_course"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="course",
        ),
        migrations.RemoveField(
            model_name="student",
            name="email",
        ),
        migrations.DeleteModel(
            name="Course",
        ),
    ]
