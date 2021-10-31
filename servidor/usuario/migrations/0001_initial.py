# Generated by Django 3.2.3 on 2021-10-30 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('tp_perfil', models.CharField(choices=[('C', 'Credor'), ('D', 'Devedor'), ('A', 'Amplo')], max_length=20)),
            ],
            options={
                'db_table': 'tp_perfil',
            },
        ),
        migrations.CreateModel(
            name='PAmplo',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('indice', models.CharField(choices=[('IPCA', 'IPCA'), ('IGPM', 'IGP-M'), ('PIB', 'PIB'), ('SELIC', 'Selic')], default='SELIC', max_length=15)),
                ('liquidez', models.CharField(choices=[('S', 'Seca'), ('I', 'Imediata'), ('G', 'Geral'), ('C', 'Corrente'), ('PNO', 'Prefiro não optar')], default='C', max_length=15)),
                ('aversao_ao_risco', models.CharField(choices=[('A', 'Alta'), ('M', 'Moderada'), ('B', 'Baixa'), ('I', 'Inexistente')], default='I', max_length=15)),
                ('ausencia_impostos', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=15)),
                ('disponibilidade_financeira', models.FloatField(default=30)),
            ],
            options={
                'db_table': 'perfil_a',
            },
        ),
        migrations.CreateModel(
            name='PCredor',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('liquidez', models.CharField(choices=[('S', 'Seca'), ('I', 'Imediata'), ('G', 'Geral'), ('C', 'Corrente'), ('PNO', 'Prefiro não optar')], default='C', max_length=15)),
                ('aversao_ao_risco', models.CharField(choices=[('A', 'Alta'), ('M', 'Moderada'), ('B', 'Baixa'), ('I', 'Inexistente')], default='I', max_length=15)),
                ('ausencia_impostos', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=15)),
                ('disponibilidade_financeira', models.FloatField(default=30)),
            ],
            options={
                'db_table': 'perfil_c',
            },
        ),
        migrations.CreateModel(
            name='PDevedor',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('indice', models.CharField(choices=[('IPCA', 'IPCA'), ('IGPM', 'IGP-M'), ('PIB', 'PIB'), ('SELIC', 'Selic')], default='SELIC', max_length=15)),
            ],
            options={
                'db_table': 'perfil_d',
            },
        ),
    ]
