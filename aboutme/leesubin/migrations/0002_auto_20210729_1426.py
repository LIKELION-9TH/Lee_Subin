# Generated by Django 3.2.5 on 2021-07-29 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leesubin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Leesubin',
        ),
    ]
