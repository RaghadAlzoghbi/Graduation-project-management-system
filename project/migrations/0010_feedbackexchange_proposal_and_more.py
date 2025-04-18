# Generated by Django 4.2.19 on 2025-04-14 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_projectproposal_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackexchange',
            name='proposal',
            field=models.ForeignKey(blank=True, help_text='The project proposal associated with this feedback.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback_exchanges', to='project.projectproposal'),
        ),
        migrations.AlterField(
            model_name='feedbackexchange',
            name='project',
            field=models.ForeignKey(blank=True, help_text='The project associated with this feedback.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback_exchanges', to='project.project'),
        ),
    ]
