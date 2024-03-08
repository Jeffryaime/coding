sandwich_orders = ['blt', 'club sandwich', 'panini', 'monte cristo', 'cubano']
finished_sandwiches = []

while sandwich_orders:
    new_order = sandwich_orders.pop()

    print(f"I made your {new_order} ")
    finished_sandwiches.append(new_order)

print("\nHere is a list of all sandwiches that were made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
