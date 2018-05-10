# Generated by Django 2.0.4 on 2018-05-10 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lock_name', models.CharField(max_length=32, unique=True)),
                ('worker_name', models.CharField(max_length=32)),
                ('lock_time', models.DateTimeField(auto_now_add=True)),
                ('expire_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Lock',
                'verbose_name_plural': 'Locks',
            },
        ),
    ]