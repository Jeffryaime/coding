def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left"""
    while unprinted_designs:
        current_print = unprinted_designs.pop()
        print(f"Printing model: {current_print}")
        completed_models.append(current_print)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
