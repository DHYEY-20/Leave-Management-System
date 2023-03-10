# Generated by Django 4.1.2 on 2023-02-10 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp_Leave_app',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('emp_code', models.CharField(max_length=100)),
                ('no_of_days', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('m_email', models.CharField(max_length=100)),
                ('start_date', models.CharField(max_length=100)),
                ('end_date', models.CharField(max_length=100)),
                ('leave_type', models.CharField(max_length=100)),
                ('status', models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True)),
                ('remrk', models.CharField(default='Please enter some remark for leave!!', max_length=100)),
            ],
            options={
                'db_table': 'Emp_Leave_appli',
            },
        ),
    ]