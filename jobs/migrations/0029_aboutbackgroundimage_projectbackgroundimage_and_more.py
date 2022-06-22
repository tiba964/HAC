# Generated by Django 4.0.4 on 2022-06-03 12:33

from django.db import migrations, models
import jobs.validators


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0028_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBackgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_about', models.FileField(blank=True, upload_to='background/services/', validators=[jobs.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='ProjectBackgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_project', models.FileField(blank=True, upload_to='background/services/', validators=[jobs.validators.validate_image_extension])),
            ],
        ),
        migrations.RemoveField(
            model_name='about',
            name='image_bg_about',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='image_bg_project',
        ),
    ]
