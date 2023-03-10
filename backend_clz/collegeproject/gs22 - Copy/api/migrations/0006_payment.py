# Generated by Django 4.1.1 on 2023-02-09 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('Esewa', 'Esewa'), ('Khalti', 'Khalti'), ('IMEPay', 'IMEPay'), ('Others', 'Others')], max_length=50)),
                ('transaction_id', models.CharField(max_length=100)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
