



def closestPrice(pizzas,toppings,x):

    ls = []

    for pizza in pizzas:
        for topping in toppings:
            ls.append(pizza+topping)

    return min(ls,key=lambda x:abs(1000-x))

pizzas = [800, 800, 800, 800]
toppings = [100]
x = 1000

print(closestPrice(pizzas,toppings,x))
