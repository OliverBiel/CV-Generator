# Generated by Django 4.0.4 on 2022-05-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('institution', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
