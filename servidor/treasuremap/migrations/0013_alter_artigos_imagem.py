# Generated by Django 3.2.3 on 2021-11-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasuremap', '0012_alter_artigos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigos',
            name='imagem',
            field=models.FileField(upload_to='static/imagens'),
        ),
    ]
