# Generated by Django 3.0.5 on 2020-05-06 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decedent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('middle_name', models.CharField(blank=True, max_length=255, verbose_name='middle name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('date_of_birth', models.DateField(blank=True, verbose_name='date of birth')),
                ('date_of_death', models.DateField(verbose_name='date of death')),
            ],
        ),
    ]
