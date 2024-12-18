def f(shopping_cart, price_list, customer_wallet):
    # Return True if customer has enough money to pay, false otherwise

    total_price = 0

    for key in cart.keys():
        total_price += prices[key] * cart[key]

    if total_price <= customer_wallet:
        return True
    
    else:
        return False

if __name__ == "__main__":
    cart = {'juice': 3, 'bread' : 1, 'milk' : 2}
    prices = {'milk' : 1.49, 'butter' : 2.09, 'juice' : 1.19, 'bread' : 1.99}

    print(f(cart, prices, 10))
    print(f(cart,prices,8))
