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


def main():
    menu = get_menu()

    print(f'\n{menu}\n')


if __name__ == '__main__':
    main()
