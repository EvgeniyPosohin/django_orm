# Generated by Django 4.2.4 on 2023-08-16 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
