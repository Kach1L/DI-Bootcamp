# Generated by Django 4.2.4 on 2023-08-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('temperature', models.FloatField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('types', models.CharField(choices=[('Sy', 'Sunny'), ('Cy', 'Cloudy'), ('Wy', 'Windy'), ('Ry', 'Rainy'), ('Sy', 'Stormy')], max_length=3)),
            ],
        ),
    ]
