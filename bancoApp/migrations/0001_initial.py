# Generated by Django 4.1.1 on 2022-09-30 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=50)),
                ('segundo_nombre', models.CharField(max_length=50)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('no_celular', models.CharField(max_length=20)),
                ('rol', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('isAdmin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='enfermero',
            fields=[
                ('id_enfermero', models.AutoField(primary_key=True, serialize=False)),
                ('turno', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=100)),
                ('no_cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UsuarioEnf', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='medico',
            fields=[
                ('id_medico', models.AutoField(primary_key=True, serialize=False)),
                ('especialidad', models.CharField(max_length=100)),
                ('no_cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='secretario',
            fields=[
                ('id_secretario', models.AutoField(primary_key=True, serialize=False)),
                ('turno', models.CharField(max_length=50)),
                ('no_cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UsuarioSec', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('id_enfermero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enfermeroPac', to='bancoApp.enfermero')),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicoPac', to='bancoApp.medico')),
                ('no_cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UsuarioPac', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='historia_clinica',
            fields=[
                ('id_historia', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_hora', models.DateTimeField()),
                ('diagnostico', models.CharField(max_length=500)),
                ('FC', models.IntegerField()),
                ('TA', models.IntegerField()),
                ('FR', models.IntegerField()),
                ('Temp', models.IntegerField()),
                ('Oxi', models.IntegerField()),
                ('Recomendaciones', models.CharField(max_length=500)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Paciente_His', to='bancoApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='acompanante',
            fields=[
                ('id_acompanante', models.AutoField(primary_key=True, serialize=False)),
                ('parentesco', models.CharField(max_length=50)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pacienteAcom', to='bancoApp.paciente')),
                ('no_cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UsuarioAcom', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('lastChangeDate', models.DateField()),
                ('isActive', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='bancoApp.customer')),
            ],
        ),
    ]
