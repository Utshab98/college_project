# Generated by Django 4.1.1 on 2023-02-09 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_theatre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(choices=[('Morning- 9 AM', 'Morning- 9 AM'), ('Noon- 12 PM', 'Noon- 12 PM'), ('Day- 3 PM', 'Day- 3 PM'), ('Evening- 6 PM', 'Evening- 6 PM'), ('Evening- 9 PM', 'Evening- 9 PM'), ('Night- 12 AM', 'Night- 12 AM')], max_length=200)),
                ('language', models.CharField(choices=[('Nepali', 'Nepali'), ('Hindi', 'Hindi'), ('English', 'English'), ('Other Regional Language', 'Other Regional Language')], max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.movie')),
            ],
        ),
    ]
