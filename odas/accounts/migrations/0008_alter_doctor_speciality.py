# Generated by Django 3.2.9 on 2024-01-08 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_doctor_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(choices=[('Podiatrist', 'Podiatrist'), ('General', 'General'), ('Pediatrician', 'Pediatrician'), ('Endocrinologist', 'Endocrinologist'), ('NeuroLogist', 'Neurologist'), ('Rheumatologist', 'Rheumatologist'), ('Allergist', 'Allergist'), ('Psychiatrist', 'Psychiatrist')], max_length=20),
        ),
    ]