# Generated by Django 5.0.3 on 2024-05-08 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

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
                ("healthcare_centre_name", models.CharField(max_length=255)),
                ("child_number", models.CharField(max_length=255)),
                ("child_name", models.CharField(max_length=255)),
                ("child_gender", models.CharField(max_length=255)),
                ("date_of_birth", models.CharField(max_length=255)),
                ("weight_at_birth", models.CharField(max_length=255)),
                ("length_at_birth", models.CharField(max_length=255)),
                ("place_of_birth", models.CharField(max_length=255)),
                ("maternal_health_worker", models.CharField(max_length=255)),
                ("child_residence", models.CharField(max_length=255)),
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
                ("Tarehe", models.DateField()),
                ("Visit_type", models.CharField(max_length=255)),
                ("weight", models.CharField(max_length=255)),
                ("height", models.CharField(max_length=255)),
                ("temperature", models.CharField(max_length=255)),
                ("other", models.CharField(max_length=255)),
                ("Test_Results", models.CharField(max_length=255)),
                ("Additional_Notes", models.CharField(max_length=255)),
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
                ("Tarehe", models.DateField()),
                ("Joto_la_Mwili", models.IntegerField()),
                ("Date", models.DateField()),
                (
                    "Child_growth_and_development_status",
                    models.CharField(max_length=255),
                ),
                ("Return_date", models.DateField()),
                (
                    "Bcg_tuberculosis_injection_right_shoulder",
                    models.CharField(max_length=255),
                ),
                ("Polio", models.CharField(max_length=255)),
                ("Dpt_hep_b", models.CharField(max_length=255)),
                ("Pneumococcal", models.CharField(max_length=255)),
                ("Rota", models.CharField(max_length=255)),
                ("Measles", models.CharField(max_length=255)),
                ("Vitamin_a", models.CharField(max_length=255)),
                ("Deworming_medication", models.CharField(max_length=255)),
                ("Weight_grams", models.IntegerField()),
                ("Anemia", models.CharField(max_length=255)),
                ("Body_temperature", models.IntegerField()),
                ("Exclusive_breastfeeding", models.CharField(max_length=255)),
                ("Replacement_milk", models.CharField(max_length=255)),
                ("Unable_to_breastfeed", models.CharField(max_length=255)),
                ("Child_play", models.CharField(max_length=255)),
                ("Eyes", models.CharField(max_length=255)),
                ("Mouth", models.CharField(max_length=255)),
                ("Ears", models.CharField(max_length=255)),
                ("Navel_Healed", models.CharField(max_length=255)),
                ("Navel_Red", models.CharField(max_length=255)),
                ("Navel_Discharge_odor", models.CharField(max_length=255)),
                ("Has_pus_filled_bumps", models.CharField(max_length=255)),
                ("Has_turned_yellow", models.CharField(max_length=255)),
                ("Received_BCG", models.CharField(max_length=255)),
                ("Received_Polio_0", models.CharField(max_length=255)),
                ("Received_Polio_1", models.CharField(max_length=255)),
                ("Received_DTP_Hep_Hib", models.CharField(max_length=255)),
                ("Received_Pneumococcal", models.CharField(max_length=255)),
                ("Received_Rota", models.CharField(max_length=255)),
                ("Name_of_attendant", models.CharField(max_length=255)),
                ("Attendant_title", models.CharField(max_length=255)),
                ("Other_issues", models.CharField(max_length=255)),
                (
                    "child",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="child.child"
                    ),
                ),
            ],
        ),
    ]
