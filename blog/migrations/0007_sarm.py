# Generated by Django 3.1.5 on 2021-04-14 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210326_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('posts', models.ManyToManyField(to='blog.Post')),
            ],
        ),
    ]