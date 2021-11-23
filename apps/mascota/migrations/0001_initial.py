# Generated by Django 3.0.7 on 2021-11-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('date_save', models.DateField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]