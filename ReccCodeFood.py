import restaurantData

def AskUser():
    try:
        Food = input('What type of food would you like to search for?')
        FoodLow = Food.lower()

        if FoodLow not in restaurantData.types:
            raise ValueError

    except ValueError:
        print('Available Types: {}'.format(', '.join(restaurantData.types)))

    finally:
        return FoodLow

def Reccomendation():
    Food = AskUser()
    recommendations = []
    for i in restaurantData.restaurant_data:
        if Food == i[0]:
            recommendations.append(i[1])
    result = ', '.join(recommendations)
    return result


def Address():
    ListRecc = Reccomendation()
    print(ListRecc)
    ListReccAsList = ListRecc.split(',')

    try:
        AskAddress = input('Would you like the address for your recommended restaurants?')
        if AskAddress not in ['Yes', 'yes', 'no', 'No']:
            raise ValueError

    except ValueError:
        print('Invalid Input')

    else:
        if AskAddress == 'no' or AskAddress == 'No':
            print('No Addresses Needed')

        else:
            addresses = []
            for i in restaurantData.restaurant_data:
                # Check if the name matches in a case-sensitive way, stripping spaces or other characters that may affect the comparison
                if i[1].strip() in [name.strip() for name in ListReccAsList]:
                    addresses.append(i[4])

            result = list((zip(ListReccAsList,addresses)))
            for i in result:
                print('Restaurant Name: {}, Address: {}'.format(i[0].strip(),i[1].strip()))



def Run():
    Address()

if __name__ == '__main__':
    Run()