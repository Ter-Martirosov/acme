# Generated by Django 5.0.6 on 2024-05-23 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0005_alter_birthday_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='birthday',
            options={'verbose_name': 'День рождения', 'verbose_name_plural': 'Дни рождения'},
        ),
    ]
