# Generated by Django 4.2.4 on 2023-08-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galareya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Cars')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField()),
                ('gibrid', models.CharField(blank=True, max_length=255, null=True)),
                ('max_speed', models.PositiveBigIntegerField(blank=True, null=True)),
                ('motor', models.FloatField(blank=True, null=True)),
                ('passangers', models.PositiveBigIntegerField(blank=True, null=True)),
                ('battery_capacity', models.FloatField(blank=True, null=True)),
                ('max_cruising_range', models.PositiveBigIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Galareya',
                'verbose_name_plural': 'Galareya',
            },
        ),
    ]