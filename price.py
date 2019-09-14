def discounted(price, discount):
    price_with_discount= price - (price * discount/100)
    print("Ответ:",price_with_discount)
    return price_with_discount
discounted(int(input("Введите цену:")),int(input("Введите скидку(числом):")))
a= discounted(100, 20)
print(a)

def discounted_two(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount= price
    else:
        price_with_discount= price - price * discount /100
    print("Ответ:", price_with_discount)
    return price_with_discount
discounted_two((input('Введите цену:')), input('Ввдите скидку(числом):'))

b = discounted_two(100, 5)
print(b)


product = {"name":"Samsung Galaxy S10", "stock": 8, "price": 50000.00, "discount":50}
product["with_discount"] = discounted(product['price'], product['discount'])
print(product)

