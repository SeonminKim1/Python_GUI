# Generated by Django 4.0.4 on 2022-06-21 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_expose_end_date_article_expose_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='expose_end_date',
            field=models.DateField(verbose_name='노출 종료 날짜'),
        ),
        migrations.AlterField(
            model_name='article',
            name='expose_start_date',
            field=models.DateField(verbose_name='노출 시작 날짜'),
        ),
    ]