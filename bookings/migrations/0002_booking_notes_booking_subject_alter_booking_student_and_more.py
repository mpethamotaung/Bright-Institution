# Generated by Django 5.1 on 2024-08-26 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
        ('users', '0004_alter_tutorprofile_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='subject',
            field=models.CharField(default='Default Subject', max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='users.studentprofile'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='users.tutorprofile'),
        ),
    ]