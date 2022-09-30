# Generated by Django 4.1.1 on 2022-09-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancoApp', '0004_alter_usuario_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='email2',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]