def get_starting_number():
    while True:
        try:
            number = int(input("How many bottles of beer on the wall?"))
            if number > 0:
                return number
        except ValueError:
            pass

def sing(number):
    counter = number
    while counter > 0:
        if counter == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
        elif counter == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down, pass it around, 1 bottle of beer on the wall.")
        else:
            print(f"{counter} bottles of beer on the wall, {counter} bottles of beer.\nTake one down, pass it around, {counter - 1} bottles of beer on the wall.")
        counter -= 1