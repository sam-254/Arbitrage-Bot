# Generated by Django 4.0.1 on 2022-06-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_deposit_amount', models.IntegerField()),
                ('total_tax_collected', models.IntegerField()),
                ('slippage', models.IntegerField()),
                ('minimum_price_difference', models.FloatField()),
                ('maximum_gas_price', models.IntegerField()),
                ('start_pause', models.BooleanField(default=False)),
                ('tax_percentage', models.FloatField()),
                ('taxation_address', models.CharField(max_length=255)),
                ('min_deposit_amount', models.IntegerField()),
                ('max_deposit_amount', models.IntegerField()),
            ],
        ),
    ]
