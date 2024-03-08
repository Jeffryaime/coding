def sandwich_order(*items_list):
    """Collecting & Printing a summary of sandwich orders"""
    print("\nHere is a summary of the order:")
    for item_list in items_list:
        print(f"-{item_list}")


sandwich_order('deli', 'philly steak', 'cheese burger', 'club sandwich')
sandwich_order('blt', 'reuben', 'panini', 'monte cristo', 'cubano', 'banh mi')
sandwich_order('muffueletta', 'shawarma', "po'boy")