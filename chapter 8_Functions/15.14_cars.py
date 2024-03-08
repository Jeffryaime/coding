def make_car(manufacturer, model_name, **cars_info):
    """Collections of car information in a dictionary"""
    cars_info['manufacturer'] = manufacturer
    cars_info['model name'] = model_name
    return cars_info

car = make_car('mercedez-benz s-class', 's 580 4matic',
               color = 'obsidian black metallic',
               price = 117000)

print(car)