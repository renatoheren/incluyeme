# Generated by Django 2.2.5 on 2019-09-15 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_vencimiento', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('realizado', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pago.Boleta')),
            ],
        ),
    ]
