# Generated by Django 4.2.4 on 2023-08-13 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_author_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('posts', models.ManyToManyField(to='polls.post')),
            ],
        ),
    ]
