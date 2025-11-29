# seating_chart_randomizer

An attempt to make a seat randomizer in the KAGAN format in Python. 

This code is focused on a non-GUI, 32 seat classroom, arranged in 8 groups of 4. The numbers a enumerated from left to right, 8 rows with 4 seats per row.

ex.
        [1 ][2 ]        [3 ][4 ] 
        [5 ][6 ]        [7 ][8 ]
                [9 ][10]        [11][12]
                [13][14]        [15][16]
        [17][18]        [19][20]
        [21][22]        [23][24]
                [25][26]        [27][28]
                [29][30]        [31][32]
The seats are arranged in performance level (I used GPA) to seat the students per KAGAN strategies. 1 - High, 2 - Medium High, 3 - Medium Low, 4- Low. 

The code is also set up to handle a different assortment of level; a non-even spread of ones, twos, threes, and fours, allowing for adaptive overlap (Not enough ones, use twos; too many twos, use threes; etc.)
                    
