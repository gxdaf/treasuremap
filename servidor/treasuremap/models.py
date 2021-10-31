# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artigos(models.Model):
    imagem = models.FileField(upload_to='treasuremap/static/imagens/')
    titulo = models.CharField(max_length=100, primary_key=True)
    subtitulo = models.CharField(max_length=500)
    corpo = models.TextField(max_length=6000)

    class Meta:
        db_table = 'artigos'

    def __str__(self):
        return self.titulo      


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExpectativaIgpm(models.Model):
    data = models.DateField(blank=True, null=True)
    dez_2021 = models.FloatField(blank=True, null=True)
    nov_2021 = models.FloatField(blank=True, null=True)
    out_2021 = models.FloatField(blank=True, null=True)
    set_2021 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expectativa_igpm'


class ExpectativaIpca(models.Model):
    data = models.DateField(blank=True, null=True)
    dez_2021 = models.FloatField(blank=True, null=True)
    nov_2021 = models.FloatField(blank=True, null=True)
    out_2021 = models.FloatField(blank=True, null=True)
    set_2021 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expectativa_ipca'


class ExpectativaPib(models.Model):
    field_2021 = models.FloatField(db_column='_2021', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2022 = models.FloatField(db_column='_2022', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2023 = models.FloatField(db_column='_2023', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2024 = models.FloatField(db_column='_2024', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2025 = models.FloatField(db_column='_2025', blank=True, null=True)  # Field renamed because it started with '_'.
    data = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expectativa_pib'


class ExpectativaSelic(models.Model):
    data = models.DateField(blank=True, null=True)
    dez_2021 = models.FloatField(blank=True, null=True)
    out_2021 = models.FloatField(blank=True, null=True)
    set_2021 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expectativa_selic'


class Igpm(models.Model):
    acum_12_meses = models.FloatField(blank=True, null=True)
    acum_ano = models.FloatField(blank=True, null=True)
    mes = models.CharField(max_length=3, blank=True, null=True)
    var_mes = models.FloatField(blank=True, null=True)
    indice = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'igpm'


class Imposto(models.Model):
    id = models.BigAutoField(primary_key=True)
    taxa = models.FloatField()
    periodo = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)

    class Meta:
        db_table = 'imposto'


class Ipca(models.Model):
    acum_12_meses = models.FloatField(blank=True, null=True)
    acum_ano = models.FloatField(blank=True, null=True)
    mes = models.CharField(max_length=3, blank=True, null=True)
    var_mes = models.FloatField(blank=True, null=True)
    indice = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'ipca'


class PCredor(models.Model):
    id = models.BigAutoField(primary_key=True)
    prod = models.CharField(max_length=20)
    risco = models.CharField(max_length=10)
    disp_financ = models.CharField(max_length=30)
    liquidez = models.CharField(max_length=20)
    prosp_rent = models.CharField(max_length=20)
    imposto = models.CharField(max_length=3)
    area = models.CharField(max_length=20)
    indicador = models.CharField(max_length=10)

    class Meta:
        db_table = 'p_credor'


class ProdFixo(models.Model):
    id_prod_fixo = models.CharField(primary_key=True, max_length=32)
    nome = models.CharField(max_length=60)
    investimento = models.FloatField()
    preco_unit = models.FloatField()
    vencimento = models.DateField()
    garantia = models.CharField(max_length=20, blank=True, null=True)
    prazo_resgate = models.CharField(max_length=60)
    rentabilidade = models.FloatField()
    tipo = models.CharField(max_length=60)
    lastro = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'prod_fixo'

class Selic(models.Model):
    data = models.DateField(blank=True, null=True)
    taxas = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'selic'


class Tr(models.Model):
    taxas = models.FloatField(blank=True, null=True)
    mes = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tr'
