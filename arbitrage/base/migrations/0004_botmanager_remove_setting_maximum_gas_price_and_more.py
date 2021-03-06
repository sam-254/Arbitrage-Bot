# Generated by Django 4.0.1 on 2022-06-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_settings_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_pause', models.BooleanField(default=False)),
                ('maximum_gas_price', models.IntegerField()),
                ('slippage', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='setting',
            name='maximum_gas_price',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='minimum_price_difference',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='slippage',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='start_pause',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='total_deposit_amount',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='total_tax_collected',
        ),
    ]
