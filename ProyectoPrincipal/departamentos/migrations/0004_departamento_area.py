# Generated by Django 4.0.4 on 2022-07-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0003_alter_departamento_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='area',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Area'),
        ),
    ]