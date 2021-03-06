# Generated by Django 2.2.5 on 2019-09-15 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curso', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('hora_inicio', models.TimeField(blank=True, null=True)),
                ('hora_fin', models.TimeField(blank=True, null=True)),
                ('presencial_u_online', models.CharField(choices=[('Presencial', 'Presencial'), ('Online', 'Online')], max_length=10)),
                ('aula', models.CharField(blank=True, max_length=5, null=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='TipoClase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_clase', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClasesAlumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horario.Clase')),
            ],
        ),
        migrations.AddField(
            model_name='clase',
            name='tipo_clase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horario.TipoClase'),
        ),
    ]
