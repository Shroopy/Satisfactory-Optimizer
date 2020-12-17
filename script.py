from data import RECIPES, COMPONENTS


def basic_recurse(component_name: str) -> None:
    print(component_name)
    component = COMPONENTS[component_name]
    if component.recipes[0] is None:
        return
    for recipe in component.recipes:
        ingredients = RECIPES[recipe].ingredients
        for ingredient in ingredients:
            basic_recurse(ingredient.component)


def main():
    print("Hello World!")
    basic_recurse("Smart Plating")


if __name__ == "__main__":
    main()