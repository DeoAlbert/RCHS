# Generated by Django 5.0.3 on 2024-06-24 20:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("mother", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Child",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("child_name", models.CharField(max_length=255)),
                ("healthcare_centre_name", models.CharField(max_length=255)),
                ("mother_name", models.CharField(max_length=255)),
                ("child_number", models.IntegerField()),
                ("child_gender", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                ("weight_at_birth", models.IntegerField()),
                ("length_at_birth", models.IntegerField()),
                ("birth_region", models.CharField(max_length=255)),
                ("birth_district", models.CharField(max_length=255)),
                ("residential_region", models.CharField(max_length=255)),
                ("residential_district", models.CharField(max_length=255)),
                ("maternal_health_worker", models.CharField(max_length=255)),
                (
                    "mother",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mother.mother"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Child_visit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("child_name", models.CharField(max_length=255)),
                ("visit_number", models.IntegerField()),
                ("visit_phase", models.CharField(max_length=255)),
                ("date", models.DateField()),
                (
                    "child_growth_and_development_status",
                    models.CharField(max_length=255),
                ),
                ("return_date", models.DateField()),
                ("vitamin_a", models.CharField(max_length=255)),
                ("deworming_medication", models.CharField(max_length=255)),
                ("weight_grams", models.IntegerField()),
                ("height", models.IntegerField()),
                ("anemia", models.CharField(max_length=255)),
                ("body_temperature", models.IntegerField()),
                ("infant_nutrition", models.CharField(max_length=255)),
                ("unable_to_breastfeed", models.CharField(max_length=255)),
                ("child_play", models.CharField(max_length=255)),
                ("eyes", models.CharField(max_length=255)),
                ("mouth", models.CharField(max_length=255)),
                ("ears", models.CharField(max_length=255)),
                ("navel_healed", models.CharField(max_length=255)),
                ("navel_red", models.CharField(max_length=255)),
                ("navel_discharge_odor", models.CharField(max_length=255)),
                ("has_pus_filled_bumps", models.CharField(max_length=255)),
                ("has_turned_yellow", models.CharField(max_length=255)),
                ("received_bcg", models.CharField(max_length=255)),
                ("received_polio_0", models.CharField(max_length=255)),
                ("received_polio_1", models.CharField(max_length=255)),
                ("received_dtp_hep_hib", models.CharField(max_length=255)),
                ("received_pneumococcal", models.CharField(max_length=255)),
                ("received_rota", models.CharField(max_length=255)),
                ("name_of_attendant", models.CharField(max_length=255)),
                ("attendant_title", models.CharField(max_length=255)),
                ("hb_percentage", models.IntegerField()),
                ("bmi", models.IntegerField()),
                (
                    "child",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="child.child"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Consultation_Visit_Child",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("child_name", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("visit_type", models.CharField(max_length=255)),
                ("weight", models.CharField(max_length=255)),
                ("height", models.CharField(max_length=255)),
                ("temperature", models.CharField(max_length=255)),
                ("other", models.CharField(max_length=255)),
                ("test_results", models.CharField(max_length=255)),
                ("additional_notes", models.CharField(max_length=255)),
                (
                    "child",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="child.child"
                    ),
                ),
            ],
        ),
    ]
