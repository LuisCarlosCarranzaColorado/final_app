# Generated by Django 4.1.1 on 2022-09-12 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bancoApp', '0007_paciente'),
    ]

    operations = [
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
                ('no_cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UsuarioAcom', to='bancoApp.usuario')),
            ],
        ),
    ]
