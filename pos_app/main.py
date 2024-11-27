from datetime import date

def selection_list()->list[str]:
    return [
        '1: Caffe Latte',
        '2: Vanilla Latte',
        '3: Cappuccino',
        '4: Espresso',
        '5: Mocha Latte',
    ]

def handle_selection(choice):
    match choice:
        case 1:
            print('Brewing........')
            print(selection_list()[0])
        case 2:
            print('Brewing........')
            print(selection_list()[1])
        case 3:
            print('Brewing........')
            print(selection_list()[2])
        case 4:
            print('Brewing........')
            print(selection_list()[3])
        case 5:
            print('Brewing........')
            print(selection_list()[4])
        case _:
            print('Unavailable!! Try again!')


def main():
    print('Good day!')
    print('Date', date.today())
    print('Welcome to TeleBaristas!')
    print('')
    print('The available selection is:')

    for value in selection_list():
        print(value)

    coffee_choice = input()    
    handle_selection(int(coffee_choice))


main()

