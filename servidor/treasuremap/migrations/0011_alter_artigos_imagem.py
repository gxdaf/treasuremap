# Generated by Django 3.2.3 on 2021-11-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasuremap', '0010_alter_artigos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigos',
            name='imagem',
            field=models.FileField(upload_to='imagens/artigo'),
        ),
    ]
