# Generated by Django 3.1.1 on 2020-09-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Product name')),
                ('shop', models.CharField(max_length=250)),
                ('bought_on', models.DateField()),
                ('warranty_date', models.DateField()),
            ],
        ),
    ]
