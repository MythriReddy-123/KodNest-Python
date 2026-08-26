def display_invoice_total(price, quantity):
    print("Total:", price * quantity)

price = int(input())
quantity = int(input())

display_invoice_total(price, quantity)