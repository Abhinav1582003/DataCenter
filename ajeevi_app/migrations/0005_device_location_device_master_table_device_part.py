# Generated by Django 5.0.3 on 2024-03-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajeevi_app', '0004_branch_contact_contact_delete_contact_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='device_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_1', models.CharField()),
                ('line_2', models.CharField()),
                ('pincode', models.CharField()),
                ('install_date', models.CharField()),
                ('location', models.CharField()),
            ],
            options={
                'db_table': 'device_location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='device_master_table',
            fields=[
                ('packet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('device_name', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('remaning', models.CharField(max_length=50)),
                ('coming_date', models.CharField(max_length=50)),
                ('update', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'device_master_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='device_part',
            fields=[
                ('device_id', models.IntegerField(primary_key=True, serialize=False)),
                ('part_1', models.CharField(max_length=50)),
                ('part_2', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'device_part',
                'managed': False,
            },
        ),
    ]
