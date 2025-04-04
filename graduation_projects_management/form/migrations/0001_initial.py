# Generated by Django 5.1.7 on 2025-03-26 13:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0008_coordinator_is_super'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('coordinators', models.ManyToManyField(blank=True, related_name='evaluation_forms', to='users.coordinator')),
                ('target_role', models.ForeignKey(blank=True, help_text='The role of users for whom this evaluation form is intended.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.role')),
            ],
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('text', models.TextField()),
                ('weight', models.FloatField()),
                ('grade_type', models.CharField(choices=[('individual', 'Individual Grade'), ('group', 'Group Grade')], max_length=20)),
                ('evaluation_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_categories', to='form.evaluationform')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='form.maincategory')),
            ],
        ),
    ]
