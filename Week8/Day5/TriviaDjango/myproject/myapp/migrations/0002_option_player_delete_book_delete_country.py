# Generated by Django 4.2.4 on 2023-09-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=100)),
                ('correct_answer', models.CharField(max_length=100)),
                ('wrong_answer1', models.CharField(max_length=100)),
                ('wrong_answer2', models.CharField(max_length=100)),
                ('wrong_answer3', models.CharField(max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('difficulty', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=100)),
                ('score', models.IntegerField(default=1000)),
            ],
            options={
                'verbose_name_plural': 'Players',
                'ordering': ['user_name'],
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
