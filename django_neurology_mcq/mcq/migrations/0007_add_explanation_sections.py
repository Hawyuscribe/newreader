from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0006_userprofile_alter_bookmark_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcq',
            name='explanation_sections',
            field=models.JSONField(
                blank=True,
                null=True,
                help_text='Structured explanation sections in JSON format'
            ),
        ),
        migrations.AddField(
            model_name='mcq',
            name='verification_confidence',
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                help_text='Confidence level of the verification'
            ),
        ),
        migrations.AddField(
            model_name='mcq',
            name='primary_category',
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                help_text='Primary category of the question'
            ),
        ),
        migrations.AddField(
            model_name='mcq',
            name='secondary_category',
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                help_text='Secondary category of the question'
            ),
        ),
        migrations.AddField(
            model_name='mcq',
            name='key_concept',
            field=models.TextField(
                blank=True,
                null=True,
                help_text='Key concept tested in the question'
            ),
        ),
        migrations.AddField(
            model_name='mcq',
            name='difficulty_level',
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                help_text='Difficulty level of the question'
            ),
        ),
    ]