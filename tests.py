# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alumnos(models.Model):
    cod_alumno = models.IntegerField(primary_key=True)
    nombre_alumno = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alumnos'


class ClaseAlumno(models.Model):
    cod_alumno = models.ForeignKey(Alumnos, models.DO_NOTHING, db_column='cod_alumno', primary_key=True)
    id_clase = models.ForeignKey('Clases', models.DO_NOTHING, db_column='id_clase')

    class Meta:
        managed = False
        db_table = 'clase_alumno'
        unique_together = (('cod_alumno', 'id_clase'),)


class Clases(models.Model):
    id_clase = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey('Cursos', models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    id_tipo_clase = models.ForeignKey('TipoClase', models.DO_NOTHING, db_column='id_tipo_clase', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    presencial_online = models.SmallIntegerField(blank=True, null=True)
    aula = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clases'


class Cursos(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cursos'


class Evaluaciones(models.Model):
    id_evaluacion = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    id_tipo_evaluacion = models.ForeignKey('TipoEvaluacion', models.DO_NOTHING, db_column='id_tipo_evaluacion', blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluaciones'


class NotaAlumno(models.Model):
    cod_alumno = models.ForeignKey(Alumnos, models.DO_NOTHING, db_column='cod_alumno', primary_key=True)
    id_evaluacion = models.ForeignKey(Evaluaciones, models.DO_NOTHING, db_column='id_evaluacion')
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nota_alumno'
        unique_together = (('cod_alumno', 'id_evaluacion'),)


class PagoAlumno(models.Model):
    cod_alumno = models.ForeignKey(Alumnos, models.DO_NOTHING, db_column='cod_alumno', primary_key=True)
    id_pago = models.ForeignKey('Pagos', models.DO_NOTHING, db_column='id_pago')

    class Meta:
        managed = False
        db_table = 'pago_alumno'
        unique_together = (('cod_alumno', 'id_pago'),)


class Pagos(models.Model):
    id_pago = models.AutoField(primary_key=True)
    concepto = models.CharField(max_length=30, blank=True, null=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    realizado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagos'


class TipoClase(models.Model):
    id_tipo_clase = models.AutoField(primary_key=True)
    nombre_tipo_clase = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_clase'


class TipoEvaluacion(models.Model):
    id_tipo_evaluacion = models.AutoField(primary_key=True)
    nombre_tipo_evaluacion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_evaluacion'
