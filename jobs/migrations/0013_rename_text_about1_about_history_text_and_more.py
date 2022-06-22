# Generated by Django 4.0.4 on 2022-06-01 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_replay'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='text_about1',
            new_name='history_text',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='text_about1_ar',
            new_name='history_text_ar',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='text_about2',
            new_name='letter',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='text_about2_ar',
            new_name='letter_ar',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='text_about3',
            new_name='vission',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='text_about3_ar',
            new_name='vission_ar',
        ),
        migrations.RemoveField(
            model_name='about',
            name='text_about4',
        ),
        migrations.RemoveField(
            model_name='about',
            name='text_about4_ar',
        ),
    ]
