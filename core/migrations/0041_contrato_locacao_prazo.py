# Generated by Django 3.2.8 on 2021-11-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_compras_locacao_prazo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato_locacao',
            name='prazo',
            field=models.IntegerField(default=0, verbose_name='Prazo'),
            preserve_default=False,
        ),
    ]
