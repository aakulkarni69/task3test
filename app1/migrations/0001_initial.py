# Generated by Django 3.0.9 on 2020-08-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('pno', models.IntegerField()),
                ('pd', models.CharField(max_length=255)),
            ],
        ),
    ]
