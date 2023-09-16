# Generated by Django 4.2.5 on 2023-09-16 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('config_id', models.AutoField(primary_key=True, serialize=False)),
                ('config_name', models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigSet',
            fields=[
                ('config_set_id', models.AutoField(primary_key=True, serialize=False)),
                ('config_value', models.CharField(max_length=500)),
                ('config_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosts.config')),
            ],
        ),
    ]
