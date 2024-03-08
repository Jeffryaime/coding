cities = {
    'montreal':{
        'country': 'canada',
        'population': 1.78,
        'fact': 'Montreal has the second largest Amusement Park.',
        },
    'paris':{
        'country':'france',
        'population': 2.161,
        'fact': 'The Louvre is the largest museum in the world.',
        },
    'london':{
        'country':'england',
        'population': 8.982,
        'fact': 'London was once the capital of 6 countries at the same time.',
            },
        }
for city, infos in cities.items():
    print(f"\nCity: {city.title()}")

    for info, detail in infos.items():
        if info == 'population':
            print(f"{info.title()}: {detail} million")
        elif info == 'fact':
            print(f"{info.title()}: {detail}")
        else:
            if isinstance(detail, str):
                print(f"{info.title()}: {detail.title()}")
            else:
                print(f"{info.title()}: {detail}")
        
         