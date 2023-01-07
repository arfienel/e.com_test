# Generated by Django 4.1.5 on 2023-01-07 11:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateFormItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('value', models.CharField(choices=[('text', 'text'), ('email', 'email'), ('phone', 'phone'), ('date', 'date')], default=('text', 'text'), max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='TemplateForm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=255, unique=True)),
                ('items', models.ManyToManyField(blank=True, to='forms_validator.templateformitem')),
            ],
        ),
    ]
