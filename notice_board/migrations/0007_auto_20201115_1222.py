# Generated by Django 3.1.1 on 2020-11-15 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice_board', '0006_auto_20201115_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='count',
            new_name='content',
        ),
    ]
