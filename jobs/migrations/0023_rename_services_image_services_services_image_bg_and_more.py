# Generated by Django 4.0.4 on 2022-06-03 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0022_alter_projectdetail_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='services_image',
            new_name='services_image_bg',
        ),
        migrations.RemoveField(
            model_name='index',
            name='whatDoDetail_text',
        ),
        migrations.RemoveField(
            model_name='index',
            name='whatDoDetail_text_ar',
        ),
        migrations.RemoveField(
            model_name='services',
            name='services_name',
        ),
        migrations.RemoveField(
            model_name='services',
            name='services_name_ar',
        ),
    ]
