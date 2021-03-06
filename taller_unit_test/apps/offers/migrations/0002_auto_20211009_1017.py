# Generated by Django 3.2.8 on 2021-10-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'ordering': ['-price']},
        ),
        migrations.AddField(
            model_name='offer',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='offer',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Price'),
        ),
    ]
