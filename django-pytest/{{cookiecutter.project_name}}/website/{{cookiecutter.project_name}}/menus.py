"""
Menu definition file as specified by djangos-simple-menu
"""
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
