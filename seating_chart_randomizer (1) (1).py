'''
    seating chart randomizer
    location: c://users//jamesegre/OneDrive - LeeSchools/documents/python_scripts
'''
import random

def text_list_list(text):
    #if list is student name and kagan number
    value = create_list_from_text(text)

    return create_list_in_list(value)

def kagan_random_seats(text_list):
    ones = [5,7,13,15,21,23,29,31]
    random.shuffle(ones)
    
    twos = [1,3,9,11,17,19,25,27]
    random.shuffle(twos)
    
    threes =[2,4,10,12,18,20,26,28]
    random.shuffle(threes)
    
    fours = [6,8,14,16,22,24,30,32]
    random.shuffle(fours)

    ones_counter = 0
    twos_counter = 0
    threes_counter = 0
    fours_counter = 0

    #the idea is that ones should sit in one seats, and so on, but account
    #for when all the one seats fill up (then they sit in two seats). Make
    #sure that fours only other seat can be a three (threes only other seat
    #can be a two)

    for i in text_list:
        if i[2] == '1':
            if ones_counter < 8:
                i.append(ones[ones_counter])
                ones_counter += 1
            elif twos_counter < 8:
                i.append(twos[twos_counter])
                twos_counter += 1
            elif threes_counter < 8:
                i.append(threes[threes_counter])
                threes_counter += 1
            elif fours_counter < 8:
                i.append(fours[fours_counter])
                fours_counter += 1 
        elif int(i[2]) == 2:
            if twos_counter < 8:
                i.append(twos[twos_counter])
                twos_counter += 1
            elif ones_counter < 8:
                i.append(ones[ones_counter])
                ones_counter += 1
            elif threes_counter < 8:
                i.append(threes[threes_counter])
                threes_counter += 1
            elif fours_counter < 8:
                i.append(fours[fours_counter])
                fours_counter += 1
        elif int(i[2]) == 3:
            if threes_counter < 8:
                i.append(threes[threes_counter])
                threes_counter += 1
            elif fours_counter < 8:
                i.append(fours[fours_counter])
                fours_counter += 1
            elif twos_counter < 8:
                i.append(twos[twos_counter])
                twos_counter += 1
            elif ones_counter < 8:
                i.append(ones[ones_counter])
                ones_counter += 1
        elif int(i[2]) == 4:
            if fours_counter < 8:
                i.append(fours[fours_counter])
                fours_counter += 1
            elif threes_counter < 8:
                i.append(threes[threes_counter])
                threes_counter += 1
            elif twos_counter < 8:
                i.append(twos[twos_counter])
                twos_counter += 1
            elif ones_counter < 8:
                i.append(ones[ones_counter])
                ones_counter += 1

    return text_list#, kagan_diagnostics(text_list)

def create_list_from_text(text):
    value = text.split('\n')
##    value = value[:-1]

    return value

def create_list_in_list(text_list):
    #if list is student name and kagan number
    return_list = []

    for i in text_list:
        return_list.append(i.split('\t'))

    return return_list

def kagan_diagnostics(text_list):
    table_one = [5,1,2,6]
    t1_counter = 0
    
    table_two = [7,3,4,8]
    t2_counter = 0

    table_three = [13,9,10,14]
    t3_counter = 0

    table_four = [15,11,12,16]
    t4_counter = 0
    
    table_five = [21,17,18,22]
    t5_counter = 0

    table_six = [23,19,20,24]
    t6_counter = 0

    table_seven = [29,25,26,30]
    t7_counter = 0

    table_eight = [31,27,28,32]
    t8_counter = 0
    
    for i in text_list:
        try:
            if i[2] in table_one:
                t1_counter += 1
            elif i[2]  in table_two:
                t2_counter += 1
            elif i[2]  in table_three:
                t3_counter += 1
            elif i[2]  in table_four:
                t4_counter += 1
            elif i[2]  in table_five:
                t5_counter += 1
            elif i[2]  in table_six:
                t6_counter += 1
            elif i[2]  in table_seven:
                t7_counter += 1
            elif i[2]  in table_eight:
                t8_counter += 1
        except IndexError:
            pass
    print(f'''
            Table One has   {t1_counter} students
            Table Two has   {t2_counter} students
            Table Three has {t3_counter} students
            Table Four has  {t4_counter} students
            Table Five has  {t5_counter} students
            Table Six has   {t6_counter} students
            Table Seven has {t7_counter} students
            Table Eight has {t8_counter} students
            ''')


##def create_num_list(text):
##    value = 0
##    value_list = []
##    
##    for i in range(len(create_list_from_text(text))):
##        value += 1
##        value_list.append(value)
##
##    random.shuffle(value_list)
##
##    return value_list

##def create_seat_chart(roster,number_list):
##    seating_chart = {}
##    for x,y in enumerate(roster):
##        seating_chart[f'{y}'] = number_list[x]
##
##    return seating_chart

##def random_seat_chart(text):
##    return create_seat_chart(create_list_from_text(text),
##                                  create_num_list(text))


