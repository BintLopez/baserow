# Generated by Django 4.1.13 on 2024-03-12 19:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0006_alter_builderworkflowaction_event"),
    ]

    operations = [
        migrations.AddField(
            model_name="formcontainerelement",
            name="reset_initial_values_post_submission",
            field=models.BooleanField(
                default=False,
                help_text="Whether to reset the form to using its initial values after a successful form submission.",
            ),
        ),
        migrations.AddField(
            model_name="inputtextelement",
            name="validation_type",
            field=models.CharField(
                choices=[("any", "Any"), ("email", "Email"), ("integer", "Integer")],
                default="any",
                help_text="Optionally set the validation type to use when applying form data.",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="checkboxelement",
            name="required",
            field=models.BooleanField(
                default=False,
                help_text="Whether this form element is a required field.",
            ),
        ),
        migrations.AlterField(
            model_name="dropdownelement",
            name="required",
            field=models.BooleanField(
                default=False,
                help_text="Whether this form element is a required field.",
            ),
        ),
        migrations.AlterField(
            model_name="inputtextelement",
            name="required",
            field=models.BooleanField(
                default=False,
                help_text="Whether this form element is a required field.",
            ),
        ),
    ]
