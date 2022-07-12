# Generated by Django 4.0.1 on 2022-06-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_botmanager_remove_setting_maximum_gas_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whitelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='uploads/')),
            ],
            options={
                'verbose_name_plural': 'Whitelisted accounts',
            },
        ),
        migrations.AlterModelOptions(
            name='botmanager',
            options={'verbose_name_plural': 'Bot Manager'},
        ),
        migrations.AlterField(
            model_name='botmanager',
            name='start_pause',
            field=models.BooleanField(default=False, verbose_name=' Off | On'),
        ),
    ]