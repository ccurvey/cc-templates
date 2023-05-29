# Generated by Django 4.2.1 on 2023-05-28 21:23

from django.db import migrations


def add_stooges(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Person = apps.get_model("{{cookiecutter.project_name}}", "Person")

    Person.objects.create(
        first_name="Larry", last_name="Stooge", email="larry@example.com"
    )
    Person.objects.create(
        first_name="Moe", last_name="Stooge", email="moe@example.com"
    )
    Person.objects.create(
        first_name="Curly", last_name="Stooge", email="curly@example.com"
    )


class Migration(migrations.Migration):
    dependencies = [
        ("{{cookiecutter.project_name}}", "0002_initial"),
    ]

    operations = [
        migrations.RunPython(add_stooges),
    ]
