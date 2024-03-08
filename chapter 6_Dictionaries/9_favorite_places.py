favorite_places = {
    'roger': ['toronto'],
    'falonne': ['santo domingo', 'québec city', 'mascouche'],
    'ylonne': ['port-au-prince', 'bainet'],
    }
for people, places in favorite_places.items():
    if len(places) > 2:
        print(f"\n{people.title()}'s favorite places are:")
    else: 
        print(f"\n{people.title()}'s favorite place is:")

    for place in places:
        print(f"- {place.title()}")
    
    