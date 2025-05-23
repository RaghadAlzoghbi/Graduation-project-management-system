# Generated by Django 4.2.19 on 2025-05-07 10:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('form_weight', models.FloatField(help_text='The weight of the entire evaluation form.')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
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
