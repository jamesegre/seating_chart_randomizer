'''
    seating chart randomizer
    location: c://users//jamesegre/OneDrive - LeeSchools/documents/python_scripts
'''
import random

def create_list_from_text(text):
    value = text.split('\n')
    value = value[:-1]

    return value

def create_list_in_list(text_list):
    #if list is student name and kagan number
    return_list = []

    for i in text_list:
        return_list.append(i.split('\t'))

    return return_list

def text_list_list(text):
    #if list is student name and kagan number
    value = create_list_from_text(text)

    return create_list_in_list(value)

def create_num_list(text):
    value = 0
    value_list = []
    
    for i in range(len(create_list_from_text(text))):
        value += 1
        value_list.append(value)

    random.shuffle(value_list)

    return value_list

def create_seat_chart(roster,number_list):
    seating_chart = {}
    for x,y in enumerate(roster):
        seating_chart[f'{y}'] = number_list[x]

    return seating_chart

def random_seat_chart(text):
    return create_seat_chart(create_list_from_text(text),
                                  create_num_list(text))


def kagan_random_seats(text_list):
    ones = [5,7,13,15,21,23]
    random.shuffle(ones)
    
    twos = [1,3,9,11,17,19]
    random.shuffle(twos)
    
    threes =[2,4,10,12,18,20]
    random.shuffle(threes)
    
    fours = [6,8,14,16,22,24]
    random.shuffle(fours)

    ones_counter = 0
    twos_counter = 0
    threes_counter = 0
    fours_counter = 0

    for i in text_list:
        print(i)
        if int(i[1]) == 1:
            if ones_counter < 6:
                i.append(ones[ones_counter])
                ones_counter += 1
            elif twos_counter < 6:
                i.append(twos[twos_counter])
                twos_counter += 1
            elif threes_counter < 6:
                i.append(threes[threes_counter])
                threes_counter += 1
            elif fours_counter < 6:
                i.append(fours[fours_counter])
                fours_counter += 1 
        elif int(i[1]) == 2:
            if ones_counter < 6:
                i.append(ones[ones_counter])
                ones_counter += 1
            elif twos_counter < 6:
                i.append(twos[twos_counter])
                twos_counter += 1
            elif threes_counter < 6:
                i.append(threes[threes_counter])
                threes_counter += 1
            elif fours_counter < 6:
                i.append(fours[fours_counter])
                fours_counter += 1 
        elif int(i[1]) == 3:
            if ones_counter < 6:
                i.append(ones[ones_counter])
                ones_counter += 1
            elif twos_counter < 6:
                i.append(twos[twos_counter])
                twos_counter += 1
            elif threes_counter < 6:
                i.append(threes[threes_counter])
                threes_counter += 1
            elif fours_counter < 6:
                i.append(fours[fours_counter])
                fours_counter += 1 
        elif int(i[1]) == 4:
            if ones_counter < 6:
                i.append(ones[ones_counter])
                ones_counter += 1
            elif twos_counter < 6:
                i.append(twos[twos_counter])
                twos_counter += 1
            elif threes_counter < 6:
                i.append(threes[threes_counter])
                threes_counter += 1
            elif fours_counter < 6:
                i.append(fours[fours_counter])
                fours_counter += 1 

    return text_list
def kagan_diagnostics()
    

