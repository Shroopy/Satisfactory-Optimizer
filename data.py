from dataclasses import dataclass


@dataclass
class Component:
    recipes: list


@dataclass
class Recipe:
    rate: float
    ingredients: list
    building_width: int
    """
    Smelter: 6
    Constructor: 8
    Assembler: 10
    Foundry: 10
    Manufacturer: 18
    """


@dataclass
class Ingredient:
    quantity: float
    component: str


RECIPES = {
    "Smart Plating": Recipe(
        2, [Ingredient(2, "Reinforced Iron Plate"), Ingredient(2, "Rotor")], 10
    ),
    "Reinforced Iron Plate": Recipe(
        5, [Ingredient(30, "Iron Plate"), Ingredient(60, "Screw")], 10
    ),
    "Bolted Iron Plate": Recipe(
        15, [Ingredient(90, "Iron Plate"), Ingredient(250, "Screw")], 10
    ),
    "Stitched Iron Plate": Recipe(
        5.625, [Ingredient(18.75, "Iron Plate"), Ingredient(37.5, "Wire")], 10
    ),
    "Iron Plate": Recipe(20, [Ingredient(30, "Iron Ingot")], 8),
    "Iron Ingot": Recipe(30, [Ingredient(30, "Iron Ore")], 6),
    "Screw": Recipe(40, [Ingredient(10, "Iron Rod")], 8),
    "Casted Screw": Recipe(50, [Ingredient(12.5, "Iron Ingot")], 8),
    "Iron Rod": Recipe(15, [Ingredient(15, "Iron Ingot")], 8),
    "Wire": Recipe(30, [Ingredient(15, "Copper Ingot")], 8),
    "Fused Wire": Recipe(
        90, [Ingredient(12, "Copper Ingot"), Ingredient(3, "Caterium Ingot")], 10
    ),
    "Iron Wire": Recipe(22.5, [Ingredient(12.5, "Iron Ingot")], 8),
    "Caterium Wire": Recipe(120, [Ingredient(15, "Caterium Ingot")], 8),
    "Caterium Ingot": Recipe(15, [Ingredient(45, "Caterium Ore")], 6),
    "Copper Ingot": Recipe(30, [Ingredient(30, "Copper Ore")], 6),
    "Copper Sheet": Recipe(10, [Ingredient(20, "Copper Ingot")], 8),
    "Rotor": Recipe(4, [Ingredient(20, "Iron Rod"), Ingredient(100, "Screw")], 10),
    "Copper Rotor": Recipe(
        11.25, [Ingredient(22.5, "Copper Sheet"), Ingredient(195, "Screw")], 10
    ),
}

COMPONENTS = {
    "Smart Plating": Component(["Smart Plating"]),
    "Reinforced Iron Plate": Component(
        ["Reinforced Iron Plate", "Bolted Iron Plate", "Stitched Iron Plate"]
    ),
    "Iron Plate": Component(["Iron Plate"]),
    "Iron Ingot": Component(["Iron Ingot"]),
    "Iron Ore": Component([None]),
    "Screw": Component(["Screw", "Casted Screw"]),
    "Iron Rod": Component(["Iron Rod"]),
    "Wire": Component(["Wire", "Fused Wire", "Iron Wire", "Caterium Wire"]),
    "Copper Ingot": Component(["Copper Ingot"]),
    "Copper Ore": Component([None]),
    "Caterium Ingot": Component(["Caterium Ingot"]),
    "Caterium Ore": Component([None]),
    "Copper Sheet": Component(["Copper Sheet"]),
    "Rotor": Component(["Rotor", "Copper Rotor"]),
}