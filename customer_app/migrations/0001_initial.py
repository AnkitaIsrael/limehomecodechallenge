# Generated by Django 2.1.7 on 2019-03-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=20, verbose_name='First Name')),
                ('surname', models.CharField(max_length=20, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=256, verbose_name='Phone')),
                ('firstStreet', models.CharField(max_length=265, verbose_name='Street 1')),
                ('secondStreet', models.CharField(max_length=256, verbose_name='Street 2')),
                ('zipCode', models.CharField(max_length=256, verbose_name='ZIP/Postal Code')),
            ],
        ),
    ]
