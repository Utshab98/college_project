# Generated by Django 4.1.1 on 2023-02-09 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('QFX Cinemas Jalma', 'QFX Cinemas Jalma'), ('Chitwan cineplex', 'Chitwan cineplex'), ('Indradev Cinema', 'Indredev cinema'), ('Ganesh Filmhall', 'Ganesh Filmhall')], max_length=100)),
                ('location', models.TextField()),
                ('capacity', models.PositiveIntegerField()),
            ],
        ),
    ]
