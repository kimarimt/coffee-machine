from prettytable import PrettyTable


DRINKS = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'price': 1.50,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'coffee': 24,
            'milk': 150.
        },
        'price': 2.50
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'coffee': 24,
            'milk': 100,
        },
        'price': 3.00
    }
}

COFFEE_MACHINE = {
    'ingredients': {
        'water': 300,
        'coffee': 100,
        'milk': 200
    },
    'profit': 0
}


def get_menu():
    menu = PrettyTable()
    menu.field_names = ['Hot Drinks', 'Price']
    menu.align = 'l'
    menu.add_rows(
        [
            ["Espresso", "$1.50"],
            ["Latte", "$2.50"],
            ["Cappucino", "$3.00"],
        ]
    )

    return menu


def has_enough_resources(drink):
    machine_ingredients = COFFEE_MACHINE['ingredients']
    drink_ingredients = drink['ingredients']

    for ingredient, amount in machine_ingredients.items():
        if 'milk' not in drink_ingredients:
            continue
        else:
            if drink_ingredients[ingredient] > amount:
                return False

    return True


def main():
    menu = get_menu()

    while True:
        print(f'\n{menu}\n')

        choice = input('Which drink would you like? ').lower()
        drink = DRINKS[choice]

        if has_enough_resources(drink):
            print(f'Your total is: {drink["price"]:.2f}')
        else:
            print('Not enough resources')

        break


if __name__ == '__main__':
    main()
