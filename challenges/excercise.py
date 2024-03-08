
def ordinal_number(calling_numbers):
    """print a list of the ordinal numbers.""" 

    for number in calling_numbers:
        if number < 2:
            print(f'{number}st')
        elif number < 3:
            print(f'{number}nd')
        elif number < 4:
            print(f'{number}rd')
        else:
            print(f'{number}th')

numbers = [1,2,3,4,5,6,7,8,9]

ordinal_number(numbers)