sandwich_orders = ['blt', 'pastrami', 'panini', 'pastrami', 'cubano', 'pastrami']
finished_sandwiches = []

print("\nPlease note that we have run out of Pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    new_order = sandwich_orders.pop()

    print(f"I made your {new_order} sandwich ")
    finished_sandwiches.append(new_order)

print("\nHere is a list of all sandwiches that were made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)