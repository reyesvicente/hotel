# Generated by Django 2.2.1 on 2019-05-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision', models.TextField()),
                ('mission', models.TextField()),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
    ]
