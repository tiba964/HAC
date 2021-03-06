# Generated by Django 4.0.4 on 2022-06-02 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_rename_storydetail_projectdetail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectdetail',
            options={'ordering': ['-project_date']},
        ),
        migrations.RenameField(
            model_name='projectdetail',
            old_name='story_date',
            new_name='project_date',
        ),
        migrations.RenameField(
            model_name='projectdetail',
            old_name='story_desc1',
            new_name='project_desc1',
        ),
        migrations.RenameField(
            model_name='projectdetail',
            old_name='story_desc1_ar',
            new_name='project_desc1_ar',
        ),
        migrations.RenameField(
            model_name='projectdetail',
            old_name='story_desc2',
            new_name='project_desc2',
        ),
        migrations.RenameField(
            model_name='projectdetail',
            old_name='story_desc2_ar',
            new_name='project_desc2_ar',
        ),
        migrations.RenameField(
            model_name='projectdetail',
            old_name='story_image_one',
            new_name='project_image_one',
        ),
        migrations.RenameField(
            model_name='projectdetail',
            old_name='story_image_three',
            new_name='project_image_three',
        ),
        migrations.RenameField(
            model_name='projectdetail',
            old_name='story_image_two',
            new_name='project_image_two',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_desc3',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_desc3_ar',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_desc4',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_desc4_ar',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_desc5',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_desc5_ar',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_desc6',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_desc6_ar',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_desc7',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_desc7_ar',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_location',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_location_ar',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_name',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='story_name_ar',
        ),
    ]
