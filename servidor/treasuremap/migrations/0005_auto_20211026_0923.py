# Generated by Django 3.2.3 on 2021-10-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasuremap', '0004_auto_20211024_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigos',
            name='corpo',
            field=models.TextField(max_length=6000),
        ),
        migrations.AlterField(
            model_name='artigos',
            name='subtitulo',
            field=models.CharField(max_length=100),
        ),
    ]
