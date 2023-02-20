# Generated by Django 4.1.5 on 2023-01-26 01:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reserves', '0009_remove_booking_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defaultvalue', models.PositiveIntegerField(blank=True, verbose_name='全日予約数')),
            ],
        ),
        migrations.CreateModel(
            name='MaxNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxnum', models.PositiveIntegerField(blank=True, verbose_name='予約最大数')),
                ('starts', models.DateTimeField(default=django.utils.timezone.now, verbose_name='開始時間')),
                ('ends', models.DateTimeField(default=django.utils.timezone.now, verbose_name='終了時間')),
            ],
        ),
    ]
