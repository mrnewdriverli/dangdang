# Generated by Django 2.0.6 on 2020-09-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
