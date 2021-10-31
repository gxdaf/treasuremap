# Generated by Django 3.2.3 on 2021-10-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExpectativaIgpm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('dez_2021', models.FloatField(blank=True, null=True)),
                ('nov_2021', models.FloatField(blank=True, null=True)),
                ('out_2021', models.FloatField(blank=True, null=True)),
                ('set_2021', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'expectativa_igpm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExpectativaIpca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('dez_2021', models.FloatField(blank=True, null=True)),
                ('nov_2021', models.FloatField(blank=True, null=True)),
                ('out_2021', models.FloatField(blank=True, null=True)),
                ('set_2021', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'expectativa_ipca',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExpectativaPib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_2021', models.FloatField(blank=True, db_column='_2021', null=True)),
                ('field_2022', models.FloatField(blank=True, db_column='_2022', null=True)),
                ('field_2023', models.FloatField(blank=True, db_column='_2023', null=True)),
                ('field_2024', models.FloatField(blank=True, db_column='_2024', null=True)),
                ('field_2025', models.FloatField(blank=True, db_column='_2025', null=True)),
                ('data', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'expectativa_pib',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExpectativaSelic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('dez_2021', models.FloatField(blank=True, null=True)),
                ('out_2021', models.FloatField(blank=True, null=True)),
                ('set_2021', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'expectativa_selic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Igpm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acum_12_meses', models.FloatField(blank=True, null=True)),
                ('acum_ano', models.FloatField(blank=True, null=True)),
                ('mes', models.CharField(blank=True, max_length=3, null=True)),
                ('var_mes', models.FloatField(blank=True, null=True)),
                ('indice', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'igpm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Selic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('taxas', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'selic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxas', models.FloatField(blank=True, null=True)),
                ('mes', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'tr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Artigos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('imagem', models.FileField(upload_to='')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=60)),
                ('corpo', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'artigos',
            },
        ),
        migrations.CreateModel(
            name='Imposto',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('taxa', models.FloatField()),
                ('periodo', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'imposto',
            },
        ),
        migrations.CreateModel(
            name='Ipca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acum_12_meses', models.FloatField(blank=True, null=True)),
                ('acum_ano', models.FloatField(blank=True, null=True)),
                ('mes', models.CharField(blank=True, max_length=3, null=True)),
                ('var_mes', models.FloatField(blank=True, null=True)),
                ('indice', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ipca',
            },
        ),
        migrations.CreateModel(
            name='PCredor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('prod', models.CharField(max_length=20)),
                ('risco', models.CharField(max_length=10)),
                ('disp_financ', models.CharField(max_length=30)),
                ('liquidez', models.CharField(max_length=20)),
                ('prosp_rent', models.CharField(max_length=20)),
                ('imposto', models.CharField(max_length=3)),
                ('area', models.CharField(max_length=20)),
                ('indicador', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'p_credor',
            },
        ),
        migrations.CreateModel(
            name='ProdFixo',
            fields=[
                ('id_prod_fixo', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
                ('investimento', models.FloatField()),
                ('preco_unit', models.FloatField()),
                ('vencimento', models.DateField()),
                ('garantia', models.CharField(blank=True, max_length=20, null=True)),
                ('prazo_resgate', models.CharField(max_length=60)),
                ('rentabilidade', models.FloatField()),
                ('tipo', models.CharField(max_length=60)),
                ('lastro', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'prod_fixo',
            },
        ),
    ]
