# Generated by Django 2.1.4 on 2019-03-02 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_news_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.URLField(blank=True, verbose_name='Интернет-адрес'),
        ),
    ]