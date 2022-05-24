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


def collect_money(drink):
    cost = drink['price']

    while True:
        print(f'\nYour total is: ${cost:.2f}\n')
        try:
            quarters = int(input('Enter quarters: ')) * 0.25
            dimes = int(input('Enter dimes: ')) * 0.10
            nickels = int(input('Enter nickels: ')) * 0.05
            pennies = int(input('Enter pennies: ')) * 0.01
            amount = quarters + dimes + nickels + pennies

            if amount < drink['price']:
                print('Sorry not enough money! Please try again')
                continue
            else:
                change = 0
                if amount > cost:
                    change = amount - cost

                COFFEE_MACHINE['profit'] += cost
                return change
        except ValueError:
            print('\nPlease enter a number for each coin')
            continue


def dispense(drink):
    machine_ingredients = COFFEE_MACHINE['ingredients']
    drink_ingredients = drink['ingredients']

    for ingredient in machine_ingredients.keys():
        if ingredient not in drink_ingredients:
            continue
        machine_ingredients[ingredient] -= drink_ingredients[ingredient]


def main():
    menu = get_menu()

    while True:
        print(f'\n{menu}\n')

        choice = input('Which drink would you like? ').lower()
        if choice not in DRINKS.keys():
            print('Please enter a drink from one of the choices on the menu')
            continue

        drink = DRINKS[choice]

        if has_enough_resources(drink):
            change = collect_money(drink)

            if change != 0:
                print(f'Here\'s your change: ${change:.2f}')

            dispense(drink)
            print(f'Here\'s your {choice} ☕️. Enjoy!')
        else:
            print('Please check machine for enough resources')
            continue


if __name__ == '__main__':
    main()
