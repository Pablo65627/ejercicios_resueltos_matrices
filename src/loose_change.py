
def loose_change(amount):

    coin_keys = ['Nickels', 'Pennies', 'Dimes', 'Quarters']
    coin_values = [5, 1, 10, 25]

    coin_dict = dict(zip(coin_keys, coin_values))

    if amount < 0:
        return {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    
    quarters = amount // 25
    amount %= 25
    
    dimes = amount // 10
    amount %= 10
    
    nickels = amount // 5
    amount %= 5
    
    pennies = amount
    
    return {'Nickels': nickels, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarters}


if __name__ == "__main__":
    
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    # assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    #assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    # assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    # assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
