from django.urls import reverse
from simple_menu import Menu, MenuItem

Menu.add_item(
    'breakfast',
    MenuItem(
        "Eggs",
        "/",
        children=[MenuItem("Scrambled", "/"), MenuItem("Fried", "/")],
    ),
)
Menu.add_item('breakfast', MenuItem("Cereal", "/"))
Menu.add_item('breakfast', MenuItem("Waffles", "/"))

Menu.add_item(
    "MainMenu",
    MenuItem(
        'Person',
        reverse("{{cookiecutter.project_name}}:person-list"),
        children=[
            MenuItem(
                "List", reverse("{{cookiecutter.project_name}}:person-list")
            ),
            MenuItem(
                "Create",
                reverse("{{cookiecutter.project_name}}:person-create"),
            ),
        ],
    ),
)
