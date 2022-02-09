# Generated by Django 4.0.1 on 2022-02-08 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='poll.Publication')),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
    ]
