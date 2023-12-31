# Generated by Django 4.2.5 on 2023-11-22 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_ingreso', models.TimeField(null=True)),
                ('hora_termino', models.TimeField(null=True)),
                ('diagnostico', models.CharField(max_length=245, null=True)),
                ('tratamiento', models.CharField(max_length=145, null=True)),
                ('observaciones', models.CharField(max_length=245, null=True)),
                ('fecha_atencion', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=145)),
                ('apellidos', models.CharField(max_length=145)),
                ('fono_1', models.IntegerField(null=True)),
                ('fono_2', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=245, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mascota', models.CharField(max_length=95)),
                ('num_chip', models.CharField(max_length=145, null=True)),
                ('edad_meses', models.IntegerField(null=True)),
                ('sexo', models.BooleanField(null=True)),
                ('url_imagen', models.CharField(max_length=145, null=True)),
                ('id_cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='veterinaria.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_raza', models.CharField(max_length=145)),
                ('nombre_especie', models.CharField(max_length=145)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=95)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=145)),
                ('apellidos', models.CharField(max_length=145)),
                ('cod_profesional', models.CharField(max_length=45, null=True)),
                ('fono_1', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=245, null=True)),
                ('id_tipo_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='veterinaria.tipousuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Asistentes',
        ),
        migrations.DeleteModel(
            name='Atenciones',
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
        migrations.DeleteModel(
            name='FichasClinicas',
        ),
        migrations.DeleteModel(
            name='Mascotas',
        ),
        migrations.DeleteModel(
            name='Razas',
        ),
        migrations.DeleteModel(
            name='Veterinarios',
        ),
        migrations.AddField(
            model_name='mascota',
            name='id_raza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='veterinaria.raza'),
        ),
        migrations.AddField(
            model_name='atencion',
            name='id_mascota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='veterinaria.mascota'),
        ),
        migrations.AddField(
            model_name='atencion',
            name='id_veterinario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='veterinaria.usuario'),
        ),
    ]
