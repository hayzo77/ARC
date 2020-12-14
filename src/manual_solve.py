#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

"""
LUKE HAYES
14498098
https://github.com/hayzo77/ARC
"""



"""PYTHON FEATURES USED AND COMMONALITIES

THERE ARE NO LIBRARIES USED IN ANY OF THESE SOLUTIONS.
EACH SOLUTIONS SIMPLY USES STANDARD PYTHON AND NUMPY.
HERE ARE SOME OF THE NUMPY FUNCTIONS USED IN THE SOLUTIONS:

Solution 1
1) Standard numpy arrays and get the values from the arrays using array[axis0][axis1] 
2) Standard python arrays
    
Solution 2
1) np.flipud().diagonal() - this is used to get the diagonal of the array from the bottom left to the top right
   This is used to isolate each diagonal so we can put them in an array and train on them
2) .copy() creates a new copy of the array
3) np.rot90() this rotates the current array 90 degrees and I use this twice to flip it 180 degrees to get the diagonals for the second half of the original array
4) np.roll() is used to rotate the pattern we are looking for by one place
   e.g. pattern = 2,3,4,5 after = 5,2,3,4 this is useful when we are trying to get the previous square value so we can use the pattern to predict the next
5) np.all(a==b) to check if two numpy values are equal
6) np.fill_diagonal() this is used to put the diagonal values back into the original numpy array
7) np.zeros() to create numpy arrays of a secific size which values will later be added to
8) Standard numpy arrays and get the values from the arrays using array[axis0][axis1] 
9) Standard python arrays
    
Solution 3
1) np.zeros() to create numpy arrays of a secific size which values will later be added to
2) np.append and np.vstack are both used to add both rows and columns to the shape arrays to make them the same size
3) np.full() this creates a numpy array with a certain value and a certain size
4) Standard numpy arrays and get the values from the arrays using array[axis0][axis1] 
5) Standard python arrays
    
    
COMMONALITIES BETWEEN THEM
-EACH SOLUTION USES NUMPY AND STANDARD PYTHON ARRAYS 
-THE MAIN SIMILARITIES ARE THAT EACH PROBLEM DEALS WITH PATTERNS AND IN ORDER TO SLOVE THE PROBLEM
 THE PATTERNS HAVE TO BE LEARNED
-THIS PATTERN SIMILARITY IS VERY SIMILAR IN PROBLEMS ONE AND TWO AS BOTH PROBLES REQUIRE LEARNING THE PATTERN
 AND THEN SOLVING IT ALTOUGH BOTH PATTERNS ARE VERY DIFFERENT
 
DIFFERENCES
-THERE ARE QUITE BIG DIFFERENCES IN HOW THESE PROBLEMS ARE SOLVED AS EACH PROBLEM DIFFERS FROM THE NEXT
-IN PROBLEM ONE THE PATTERN IS LARGE AND IS REPEATED IN EACH OF THE 4 SQUARES OF THE INPUT ARRAY
 PROBLEM TWO HAS A PATTERN THAT OCCURS ACCROSS THE DIAGONALS OF THE INPUT ARRAY
 PROBLEM THREE HAS A SERIES OF SHAPES THAT NEED TO BE EXTRACTED AND THEN PLACED ON TOP OF ONE ANOTHER WHILE ALSO BEING CENTERED 
"""




""" OPTIONAL COMMENTS ON THE ISSUES PRESENT IN THIS APPROACH

ONE SUCH ISSUE THAT I HAVE NOTICED IS THE LACK OF DIVERSITY IN THE TRAINING 
AND TEST EXAMPLES. I THINK THAT HAVING SO FEW EXAMPLES TO TRAIN ON MEANS 
THAT THERE ARE LIKELY SHORTCOMINGS IN THE CODE. FOR EXAMPLE IN ONE PROBLEM
I TRAIN IN THE SECOD HALF OF THE DATA BECAUSE ALL THE MISSING VALUES ARE IN
THE FIRST HALF. THIS MEANS THAT IF I WAS TRYING TO SOLVE A TEST PROBLEM,
WHERE THERE WAS DATA MISSING WHEN TRAINING THE PATTERN, THE SOLUTION WOULD
BE INCORRECT. THE LACK OF DIVERSITY IN EACH OF THE TRAINING PROBLEMS MEANS 
THAT SOLUTIONS CAN BE CODED IN SUCH A WAY THAT THEY WORK FOR THESE EXAMPLES
BUT DON'T WORK FOR OTHERS WHICH IS NOT WHAT WE WANT. THIS MEANS THAT THE 'INTELLIGENCE'
ELEMENT THAT WE ARE LOOKING FOR IS MISSING.

ANOTHER POSSIBLE ISSUE IS THAT THE RESULT IS EITHER TRUE OR FALSE AND PERHAPS
IF THERE WAS A VALUE RETURNED BETWEEN 0 AND 1 WOULD BE A BETTER FOR TRAINING.

"""

#THIS FUNCTION RETURNS THE NEW POSITION
#IT WILL RETURN A NEW X VALUE OR Y VALUE
#IT IS USED TO GET THE POSITION FROM A DIFFERENT SQUARE 
#SO WE CAN CHECK THE VALUE AT THAT POSITION
def get_new_location(centre, position):
    value = position - centre
    new = centre - value
    return new


def solve_3631a71a(x):
    
    """TASK VERBAL DESCRIPTION
    There is one square that can be split into 4 sqaures that match perfectly
    The centre of this is not in the centre of the input array which adds difficulty to the problem
    This means tht there is a square in the input array that can be split into 4 seperate squares that mirror eachother
    Therefore if we have a vlue of 9 we can lookup the correctly value by looking at any of the other 3 squares
    However since the symmetric area is not in the centre this means that there are areas that are not mirrored in all the other squares
    In this case this area is also mirrored by the other areas that are outside the symetric square and therefore we can use these values
    """
    
    
    """
    PROBLEMS SOLVED - ALL TEST AND TRAINING PROBLEMS
    """
    
    
    """HOW SOLVE WORKS"""
    #LOOP THROUGH EACH SQUARE
    #IF THE SQUARE VALUE IS 9
    #IF IN SQUARE 1 TAKE FROM SQUARE 2 AND VICE VERSA
    #IF IN SQUARE 3 TAKE FROM SQUARE 4 AND VICE VERSA
    #IF OUTSIDE SQUARE ONE TO THE LEFT TAKE FROM TO THE LEFT OF SQUARE 2 AND VICE VERSA
    #IF ABOVE SQUARE ONE TAKE FROM ABOVE SQUARE 2 AND VICE VERSA
    #PROBLEM SOLVED


    xlen, ylen = x.shape
    
    xcounter = 1
    ycounter = 1
    #THESE ARE THE CENTRE VALUES OF THE MATCHING SQUARE
    xcentre = 16
    ycentre = 16
    square = 0 
    #TOTAL SIZE OF THE PATTERN 
    pattern_size = 28
    #THESE ARE USED FOR THE SQUARE SIZES
    xymax = pattern_size/2
    xmin = xcentre - xymax
    ymin = ycentre - xymax
    #FULL SQUARE SIZE
    pattern_max = 30
    
    new_x = x.copy()

    #FOR EACH ROW OF THE SQUARE
    for yval in range(ylen):
        xcounter = 1

        #FOR EACH SQUARE IN THE ROW
        for xval in range(ylen):
            
            #ONLY IF THE VALUE OF THE SQUARE IS 9/BLANK
            if new_x[yval][xval] == 9:
                          
                #FIRST SQUARE
                #IF WE ARE IN THE FIRST SQUARE AND INSIDE THE PART WHICH MATCHES ALL OTHER SQUARES
                if xcounter <= 16 and ycounter <= 16 and xcounter > xmin:
                    #GET THE NEW X LOCATION 
                    #WHICH COMES FROM THE RIGHT SIDE I.E. SQUARE 2
                    xnew = get_new_location(xcentre, xcounter)
                    
                    #IF THE NEW VALUE IS ALSO 9 WE CANNOT TAKE THIS VALUE 
                    #SO THEREFORE WE GET A NEW Y VALUE WHICH MEANS LOOKING AT SQUARE 3
                    if new_x[ycounter-1][xnew] ==  9:
                        ynew = get_new_location(ycentre, ycounter)
                        new_x[yval][xval] = new_x[ynew][xcounter-1]  
                    #OTHERWISE THE VALUE WE GOT FROM SQUARE 2 IS PERFECT
                    else:
                        new_x[yval][xval] = new_x[ycounter-1][xnew]
                        
                #IF WE ARE IN SQUARE 1 BUT OUTSIDE THE PART THAT MATCHES ALL OTHER SQUARES
                #TAKE THE VALUE FROM SQUARE 2
                elif xcounter <= xmin and ycounter > ymin and xcounter <= 16 and ycounter <= 16:
                    ynew = get_new_location(ycentre, ycounter)
                    new_x[yval][xval] = new_x[ynew][xcounter-1]     
                    
                    
                    
                #SECOND SQUARE
                #SAME PROCESS AS IN SQUARE ONE EXCEPT FIRSTLY WE TAKE A NEW X VALUE FROM SQUARE 1
                #IF THE VALUE AT OUR NEW POSITION IS ALSO 9 
                #THEN WE LOOK DOWN TO SQUARE 4
                elif xcounter >= 16 and ycounter <= 16:
                    xnew = get_new_location(xcentre, xcounter)

                    if new_x[ycounter-1][xnew] ==  9:
                        ynew = get_new_location(ycentre, ycounter)
                        new_x[yval][xval] = new_x[ynew][xcounter-1] 
                    else:
                        new_x[yval][xval] = new_x[ycounter-1][xnew]    

                    
                #THIRD SQUARE 
                #SAME PROCESS AS THE OTHER TWO SQUARES EXCEPT FIRSTLY WE TAKE A VALUE FROM SQUARE 4
                #IF THE VALUE AT THE LOCATION IN SQUARE 4 IS ALSO 9 THEN 
                #WE LOOK AT SQUARE 1
                elif xcounter <= 16 and ycounter >= 16  and xcounter > xmin:
                    xnew = get_new_location(xcentre, xcounter)
                    
                    if new_x[ycounter-1][xnew] == 9:
                        ynew = get_new_location(ycentre, ycounter)
                        new_x[yval][xval] = new_x[ynew][xcounter-1] 
                    else:
                        new_x[yval][xval] = new_x[ycounter-1][xnew]
                        
                #IF WE ARE IN SQUARE 3 BUT OUTSIDE THE PART THAT MATCHES ALL OTHER SQUARES
                #TAKE THE VALUE FROM SQUARE 1
                elif xcounter <= xmin and ycounter > ymin and xcounter <= 16 and ycounter >= 16:                    
                    ynew = get_new_location(ycentre, ycounter)
                    new_x[yval][xval] = new_x[ynew][xcounter-1] 
                    
                    
                    
                #FOURTH SQUARE 
                #SAME PROCESS AS THE OTHER THREE SQUARES EXCEPT FIRSTLY WE TAKE A VALUE FROM SQUARE 3
                #IF THE VALUE AT THE LOCATION IN SQUARE 3 IS ALSO 9 THEN 
                #WE LOOK AT SQUARE 2
                elif xcounter >= 16 and ycounter >= 16:
                    xnew = get_new_location(xcentre, xcounter)
                    if new_x[ycounter-1][xnew]  == 9:
                        ynew = get_new_location(ycentre, ycounter)
                        new_x[yval][xval] = new_x[ynew][xcounter-1] 
                    else:
                        new_x[yval][xval] = new_x[ycounter-1][xnew] 
                    
            #INCREMENT COUNTERS
            xcounter = xcounter + 1 
        ycounter = ycounter + 1 

    #RETURN NEW ANSWER SQUARE
    return new_x


def solve_484b58aa(x):
    
    """TASK VERBAL DESCRIPTION
    This problem was difficult to solve
    firstly the squares have patterns when we look diagonally such as 1,2,3,1,2,3
    we need to get each diagonal pattern
    these patterns then repeat themselves every n diagonals both left and right such as (1,1,1), (2,2,2,2), (2,3,2,3,2), (1,1,1,1,1,1)
    Therfore the key to solving this problem is to learn these patterns and then apply them as rules when we are trying to predict the value of a square
    """
    
    """
    PROBLEMS SOLVED - ALL TEST AND TRAINING PROBLEMS
    """
    
 
    """HOW SOLVE WORKS"""
    #TAKE ALL THE DIAGONAL DATA FROM THE ORIGINAL ARRAY AND PUT THEM INTO THEIR OWN ARRAY AND CREATE AN ARRAY TO STORE THEM ALL
    #GET THE PATTERN FOR EACH DIAGONAL 
    #TRAIN ON THE DIAGONAL DATA WITH THE LEAST AMOUNT OF MISSING DATA TO GET THE DIAGONAL PATTERN
    #ASSIGN A PATTERN TO EACH DIAGONAL
    #FOR EACH DIAGONAL IF IT HAS A 0 VALUE USE ITS ASSIGNED PATTERN AND THE PREVIOUS SQUARE VALUE TO PREDICT QHAT VALUE THE 0 SHOULD BE
    #IN SOME CASES THE DIAGONAL DATA WILL START WITH A 0 THEN WE HAVE NO PREVIOUS DATA
    #IN THIS CASE WE REVERSE THE PATTERN AND THE DIAGONAL DATA AND MAKE A PREDICTION THIS WAY
    #PUT ALL THE DIAGONALS BACK TOGETHER TO MAKE THE ARRAY WE RETURN
    
    
    
    
    
    #FIRST WE NEED TO GET ALL THE DIAGONALS AND PUT THEM INTO LISTS
    #NUMPY DOES HAVE A DIAGONAL METHOD WHICH WORKS WELL FOR THE FIRST HALF OF DIAGONALS
    #TO DO SO I MAKE THE SQUARE BIGGER AND BIGGER
    #IE 1x1 - GET DIAGONAL, 2x2 - GET DIAGONAL ALL THE WAY TO 30x30
    #THIS GIVES THE FIRST HALF
    
    first_half = []

    xdimension, ydimension = x.shape   
    if xdimension == ydimension:
        dimension = xdimension


    for size_its in range(dimension):
        actual_size = size_its + 1
        array = x[:actual_size, :actual_size]
        
        
        first_diagonals = np.flipud(array).diagonal()
        first_half.append(first_diagonals)
        
        
    #THEN TO GET THE SECOND HALF WE NEED TO FLIP THE NUMPY ARRAY 180 DEGREES
    #THEN DO THE SAME PROCESS

    newx = x.copy()
    newx = np.rot90(newx)
    newx = np.rot90(newx)

    second_half = []
    
    for size_its in range(dimension-1):
        actual_size = size_its + 1
        array = newx[:actual_size, :actual_size]
        
        second_diagonals = np.flipud(array).diagonal()
        
        #print(second_diagonals)
        second_half.append(np.flip(second_diagonals))
        
 
    #NOW WE HAVE TWO LISTS OF THE DIAGONALS 
    first = np.array(first_half)
    second = np.array(second_half)
    
    #THE TRAINING SET SHOULD BE APPLIED TO THE MORE FULL SET 
    #WHICH IS THE BOTTOM RIGHT HALF
    training_set = second


    #GET ALL THE PATTERNS FOR THE DIAGONALS AFTER THE FIFTH IN THE TRAINING HALF
    #WE REMOVE THE FIRST 5 AS THEY ARE USUALLY 1,2,3,4,5 SQUARES LONG
    #WHICH MAY NOT SHOW THE FULL PATTERN
    
    training_set = training_set[5:]
    pattern_list = []
    for diagonal in training_set:
        i = 0
        pattern = []
        for square_num in diagonal:
            if i == 0:
                pattern.append(square_num)
                i = i + 1
            elif square_num not in pattern:
                pattern.append(square_num)
                i = i + 1
            else:
                pattern_list.append(pattern)
                break
            
    #NOW WE HAVE A LIST OF PATTERNS

    #LETS GET THE LONGEST PATTERN I.E. THE MOST COMPLEX ONE
    #THIS IS BECAUSE PATTERNS SUCH AS ALL RED SQUARES CAN OCCUR
    #NUMEROUS TIMES IN THE DIAGONAL PATTERN
    #THIS WOULD CAUSE AN ISSUE IN CASES SUCH AS
    #P1,P3,P5,P3,P5,P1
    #WE NEED TO SEACH FOR THE START AND END OF P1 TO GET THE FULL PATTERN
    longest_pattern = [len(i) for i in pattern_list]
    pattern_to_search = max(pattern_list, key=len)

 
    #WE THEN REMOVE THE PATTERNS FROM THE LIST THAT COME BEFORE THE 
    #LONGEST PATTERN AS THESE ARE NOT NEEDED
    index = 0
    exitbool = False
    for pattern in pattern_list:
        index = index + 1
        if pattern == pattern_to_search and exitbool == False:
            actual_index = index
            exitbool = True
    
    pattern_list = pattern_list[actual_index:]
    
    
    #NOW WE NEED TO CREATE A DICTIONARY WITH THE DIAGONAL PATTERN
    #ADD THE FIRST/LONGEST PATTERN FIRST
    pattern_dict = {}
    all_patterns = []
    d = {1: pattern_to_search}
    pattern_dict.update(d)
    all_patterns.append({1: pattern_to_search})
    pattern_number = 1
    pattern_found = False
    number_of_patterns = 1
    
    
    #HERE WE APPEND TO THE PATTERN DICTIONARY UNTIL WE AGAIN REACH THE LONGEST
    #PATTERN WHICH IS OUR REFERENCE
    #IF WE REACH THIS WE STOP AND THEREFORE WE HAVE THE PATTERN FOR THE FULL SQUARE
    for pattern in pattern_list:
        pattern_number = pattern_number + 1
        if pattern_found == False:
            #WE LOOP HERE BECAUSE WE NEED TO SHIFT THE SEARCH PATTERN
            #WE DO THIS TO MAKE SURE IT MATCHES
            #E.G. 2,4,5 != 5,2,4 BUT WHEN WE SHIFT THEY ARE EQUAL
            for i in range(len(pattern_to_search)):

                if np.all(pattern_to_search==pattern):
                    pattern_found = True
                else:
                    #HERE WE SHIFT THE THE SEARCH PATTERN ONE BIT
                    pattern_to_search = np.roll(pattern_to_search, 1)
                    patterntoappend = {pattern_number: pattern}
                    d = {pattern_number: pattern}
            #DONT ADD THE PATTERN UNTIL WE REACH HERE
            if pattern_found == False:
                pattern_dict.update(d)
                all_patterns.append(patterntoappend)
                number_of_patterns = number_of_patterns + 1

                
        

    #NEED TO REVERSE THE SECOND SET OF DATA
    second_reversed = []

    for i in range(second.size):
        second_reversed.append(second[second.size - (i + 1)])
    
    
    #PUT ALL THE DATA INTO ONE LIST
    all_data = []
    for i in first:
        all_data.append(i)
    for j in second_reversed:
        all_data.append(j)

    #MAKE IT A NUMPY ARRAY
    all_data_numpy = np.array(all_data)        
    
    

    #WE DONT WANT TO LOOP MOER THAN THIS LATER
    pattern_max = 28 + number_of_patterns
    
    pattern_recognition = []
    
    
    #NOW WE CREATE A LIST FROM THE DIAGONALS SO WE CAN CHECK THE PATTERN WE HAVE COME UP WITH
    counter = 0
    for i in all_data_numpy:
        if counter >= 29 and counter <= pattern_max:
            pattern_recognition.append(i)
        counter = counter + 1
        
    pattern_recognition = np.array(pattern_recognition)
    
    
    
    

    pattern_size = pattern_to_search.size

    #THIS LOOP RETURNS THE INDEX OF THE DIAGONAL THAT MATCHES THE LONGEST/REFERENCE DIAGONAL PATTERN
    final_match_index = 0
    match_index = 28
    for pattern in pattern_recognition:
        match_index = match_index + 1

        for i in range(len(pattern_to_search)):
            if np.all(pattern_to_search==pattern[:pattern_size]):
                final_match_index = match_index
            else:
                pattern_to_search = np.roll(pattern_to_search, 1)
    

    #CREATE TWO LISTS OF BEFORE AND AFTER THE MATCH
    #AS WE WILL APPLY THE PATTERNS TO THESE
    before_match_list = all_data_numpy[:final_match_index]
    after_match_list = all_data_numpy[final_match_index:]
    
    """
    NOW WE HAVE THE DIAGONAL PATTERN THAT EXISTS 
    WE NEED TO THEN ASSIGN A PATTERN TO EACH DIAGONAL
    THIS IS EASY BECAUSE WE ALREADY KNOW THE PATTERN AND WE HAVE 
    AN INDEX FOR WHERE THIS PATTERN STARTS
    """
    
    #CREATE A LIST OF ZEROS WHICH WILL REPRESENT THE PATTERN NUMBER FOR EACH DIAGONAL
    pattern_index_list = np.zeros((all_data_numpy.size,), dtype=int)
    
    #FIRST LOOK AT ALL THE ONES TO THE LEFT OF THE REFERENCE/LONGEST PATTERN
    idx = (before_match_list.size)  
    patternidx = 1
    count = 0
    #HERE WE ASSIGN EACH ONE A PATTERN VALUE BASED ON OUT DIAGONAL PATTERN
    #E.G. DIAGONAL PATTERN IS 1,2,3,4,5,6
    #PATTERN 6 IS LOCATED AT INDEX OF 14
    #THEN WE ASSIGN INDEX 13 A VALUE OF 1 THEN INDEX 12 IS 2 AND SO ON
    for l in before_match_list:
        
        pattern_index_list[idx] = patternidx
        
        if patternidx == number_of_patterns:
            patternidx = 1
        else:
            patternidx = patternidx + 1
            
        idx = idx - 1
        count = count + 1

    
    #NOW WE DO THE SAME FOR TO THE RIGHT OF THE INDEX EXCEPT WE ASSIGN 
    #THE PATTERN IN A BACKWARDS MANNER
    #6,5,4,3,2,1
    #PATTERN 6 IS LOCATED AT INDEX 14
    #THEN WE ASSIGN INDEX 15 A PATTERN VALUE OF 5
    patternidx = patternidx - 2
    if patternidx == 0:
        patternidx = number_of_patterns - 1
        
    idx = (before_match_list.size)
    patternidx = 1
    loopfor = pattern_index_list.size - count

    for l in range(loopfor):
             
        pattern_index_list[idx] = patternidx     
        if patternidx == 1:
            patternidx = number_of_patterns
        else:
            patternidx = patternidx - 1
        idx = idx + 1
        

    #NOW I HAVE A LIST WITH THE PATTERN FOR EACH DIAGONAL
    #AND A LIST WITH THE DIAGONAL 
    #BOTH OF THESE MATCH INDEX WISE    
    
    
    #THE NEXT STEP IS TO USE THIS DATA TO PREDICT THE VALUES WHERE THERE ARE ZEROS
    
    i = 0
    new_data = []
    for data in all_data_numpy:

        #WE USE THE PREVIOUS VALUE TO PREDICT THE CURRENT ONE
        #IF THE FIRST SQUARE HAS A VALUE OF 0
        #THEN WE NEED TO FLIP THE ARRAY BECAUSE THEN WE HAVE A FIRST VALUE
        #TO GUESS FROM
        backwards_approach = False
        if data[0] == 0:
            backwards_approach = True 
            data = np.flip(data)

        #GET THE INDEX OF THE PATTERN 
        patternkey = pattern_index_list[i]
        updated_data = []
        if len(data) == 1:
            updated_data.append(data[0])
            
        #SOMETIMES THE KEY CAN BE 0 FOR THE CORNERS
        if(patternkey != 0):

            #GET THE PATTERN FROM THE DICTIONARY USING THE KEY
            actual_pattern = pattern_dict[patternkey]
            old_square = 50
            first_square = 0
            
            #LOOP THROUGH EACH SQUARE IN THE DIAGONAL DATA
            for square in data:
                first_square = first_square + 1
                
                #IF THE FIRST VALUE IS 0 THEN WE NEED TO REVERSE THE PATTERN
                if backwards_approach == True and first_square == 1:
                    new_pattern = list(actual_pattern)
                    pattern = new_pattern.reverse()
                    
                #IF THE SQAURE IS 0 WE NEED TO DO A PREDICTION
                if square == 0:
                    
                    #IF THE PATTERN LENGTH IS 1 THEN ALL SQUARES ARE THE SAME
                    if len(actual_pattern) == 1:
                        square = old_square
                        updated_data.append(square)
                    else:
                                                
                        if backwards_approach == False:
                            new_pattern = list(actual_pattern)
                        
                        detected = False
                        
                        #WE ARE SHIFTING THE PATTERN EACH TIME IT DOESNT MATCH SO WE LOOP OVER THE FULL PATTERN SIZE
                        for j in range(len(new_pattern)):
                            

                            #IF THE FIRST VALUE OF THE PATTERN IS EQUAL TO THE LAST SQUARE
                            #THEN WE CAN SAY THE NEXT VALUE SHOULD BE THE SECOND VALUE IN THE PATTERN
                            if new_pattern[0] == old_square and detected == False:
                                updated_data.append(new_pattern[1])
                                detected = True
                                old_square = new_pattern[1]
                            
                            #OTHERWISE WE SHIFT THE PATTERN ONE SPACE TO THE RIGHT
                            #AND TRY AGAIN
                            else:
                                new_pattern = np.roll(new_pattern, 1)
                         
                                
                                
                #IF THE SQAURE IS NOT 0 THEN WE ADD IT TO THE LIST 
                #AND SET OLDSQUARE TO THE CURRENT SQUARE FOR THE NEXT ITERATION
                else:
                    updated_data.append(square)
                    old_square = square
        i = i + 1
        
        #WE HAVE HAD TO REVERSE THE DATA SO BEFORE WE ADD IT TO THE LIST
        #WE NEED TO FLIP IT BACK TO NORMAL
        if backwards_approach == True:
            updated_data = updated_data[::-1]
            new_data.append(updated_data)
            
        #NOT REVERSED SO ADD
        else:
            new_data.append(updated_data)
        
    """
    NOW WE HAVE A LIST OF ALL THE DIAGONALS AND THEY ARE CORRECTED AND WE
    NEED TO PIECE THESE BACK TOGETHER 
    """
    
    #WE DO THE SAME PROCESS AS HOW WE EXTRACTED THE DIAGONALS
    #EXCEPT WE USE np.fill_diagonal TO FILL THE DIAGONAL WITH THE NEW VALUES
    #INCREMENTALLY MAKE THE SQUARE BIGGER AND ADD THE NEW DIAGONAL
    for size_its in range(dimension):
        actual_size = size_its + 1
        array = x[:actual_size, :actual_size]
        np.fill_diagonal(np.flipud(array), new_data[size_its])
        data_size = size_its

    #AS BEFORE THIS HAS ONLY DONE HALF AND NOW THE OTHER HALF MUST BE DONE    

    #CREATE A COPY OF X AND ROTATE IT 180 DEGREES SO WE CAN APPEND TO THE DIAGONALS
    xcopy = x.copy()
    xcopy = np.rot90(xcopy)
    xcopy = np.rot90(xcopy)   

    c = 0

    #SAME PROCESS AS ABOVE EXCEPT WE START WITH A BIG GRID AND MAKE IT SMALLER
    #ALSO WE HAVE TO REVERSE THE DATA WE ARE PUTTING INTO THE DIAGONAL
    #THIS IS BECAUSE WE HAVE FILLPED THE ARRAY
    #ALSO NOT WE ARE ADDING THE SECOND HALF OF THE DATA 
    
    for size_its in reversed(range(dimension)):
        actual_size = size_its + 1
        array = xcopy[:actual_size, :actual_size]

        dat = new_data[data_size+c]

        np.fill_diagonal(np.flipud(array), dat[::-1])

        c = c + 1
        
    
    #FLIP THE FINAL DATA AGAIN 180 DEGREES SO ITS BACK TO NORMAL
    xcopy = np.rot90(xcopy)
    xcopy = np.rot90(xcopy)
    
    
    return xcopy


def solve_c8cbb738(x):
    
    """TASK VERBAL DESCRIPTION
    The method I chose to solve this problem was to isolate each pattern and 
    create a new array for each pattern. I then extracted the locations for each 
    shape and then I classed the shape as a symetric rectangle or not
    The based on the location information and the type of shape I removed all 
    of the data outside the dimenasions of the shape.
    Then I had all the shapes isolated and needed a method to put them all together
    I then got the dimensions for the arrays that held the shapes.
    To put them altogether I had the arrays with the shapes in them the same size.
    Once this was done putting them altogether was easy.
    """
    
    """
    PROBLEMS SOLVED - ALL TRAINING AND TEST PROBLEMS.
    """
    
    
    """HOW SOLVE WORDS"""
    #GET THE BASE COLOUR AND ALL THE COLOURS OF THE PATTERNS
    #GET THE LOCATIONS IN AN ARRAY FOR EACH COLOUR. THIS GIVES US THE LOCATIONS OF EACH SQUARE OF EACH SHAPE
    #CREATE A COPY OF THE ORIGINAL NUMPY ARRAY FOR EACH SHAPE/PATTERN
    #WITH THIS COPY WE THEN REMOVE THE DATA THAT IS NOT TO DO WITH THAT SPECIFIC SHAPE
    #NOW WE HAVE ALL THE RELVENT SHAPES IN THEIR OWN NUMPY ARRAY
    #THESE SHAPES CAN BE OF DIFFERENT SIZES AND IN ORDER TO PUT THEM BACK TOGETHER THEY NEED TO BE THE SAME SIZE
    #I THEN DO SOME WORK TO ADD SOME OF THE BACKGROUND COLOUR TO MAKE ALL THE NUMPY ARRAYS THAT STORE THE SHAPES THE SAME SIZE
    #FINALLY I CREATED A BLANK NUMPY ARRAY AND INDIVIDUALLY ADD EACH SHAPE TO THE ARRAY
    

    
    #get the shape of the input
    xlen, ylen = x.shape
    all_colours = []
    base_colour = 0

    #get the base colour by seeing if the top left colour is equal to the bottom right
    if x[xlen-1][ylen-1] == x[0][0]:
        base_colour = x[0][0]
    
    #loop through each square
    for xi in x:
        for y in xi: 
            #if the colour is not already in the list add it
            if y not in all_colours:
                all_colours.append(y)
    
    #remove the base colour
    all_colours.remove(base_colour)
    
    
    all_colour_locations = []
    colour_array = []
    
    #here we get the locations for each shape
    #loop through all the colours
    for colour in all_colours:
        #for each colour create a copy of the original array and put it in a list
        xcolour = x.copy()
        colour_array.append(xcolour)
        colour_locations = []
        
        #loop through the data
        for xi in range(xlen):
            for y in range(ylen):

                #if the square is the current colour we are looking for
                #add the location to a list for each colour
                if np.all(x[xi][y]==colour):
                    location = (xi,y)
                    colour_locations.append(location)
        #add each list of locations to a main list
        all_colour_locations.append(colour_locations)

    
    #by symetical here I mean that the locations of the shape are symmetrical
    #This difference matters as it influences how the data is parsed when isolating the shape
    symetrical_list = np.zeros(len(all_colour_locations))
    
    #loop through the number of shapes
    for i in range(len(all_colour_locations)): 
        #if these values match then the shape is flat and we call it symetric
        if all_colour_locations[i][0][0] == all_colour_locations[i][1][0] and all_colour_locations[i][2][0] == all_colour_locations[i][3][0]: 
            symetrical_list[i] = 1
        #otherwise we done ane we will parse it differently
        else:
            symetrical_list[i] = 0
    
    #loop through the number of shapes
    for i in range(len(all_colour_locations)):
        
        #if its not symetrical 
        if symetrical_list[i] == 0:
            #loop for the number of locations
            for j in range(len(all_colour_locations[i])):
                array = colour_array[i]
                
                #1 first we remove all the data to the right of the shape which means we need the third/righmost part of a non symetrical shape
                #2 then we remove all the data below the fourth/lowest part of the shape in the y direction
                #3 then we remove all the data above the highest/first part of the shape
                #4 finally we remove the data to the left of the leftmost/second part of the shape
                #now we are left with the parsed data
                if j == 0:
                    colour_array[i] = array[:,:all_colour_locations[i][2][1]+1]
                elif j == 1:
                    colour_array[i] = array[:all_colour_locations[i][3][0]+1,:]
                elif j == 2:
                    colour_array[i] = array[all_colour_locations[i][0][0]:, :]
                elif j == 3:
                    colour_array[i] = array[:,all_colour_locations[i][1][1]:]
        #if it is symetrical
        else:
            for k in range(len(all_colour_locations[i])):
                array = colour_array[i]
                
                #very similar to the example above except 
                # firstly element 2 and 4 are the righmost part of the shape so we use those in step 1 - we use 2
                # then we use part 1 to remove the data to the left of the shape as it is the leftmost along with the third peice of the pattern 
                if k == 0:
                    colour_array[i] = array[:,:all_colour_locations[i][1][1]+1]
                elif k == 1:
                    colour_array[i] = array[:all_colour_locations[i][3][0]+1,:]
                elif k == 2:
                    colour_array[i] = array[all_colour_locations[i][0][0]:, :]
                elif k == 3:
                    colour_array[i] = array[:,all_colour_locations[i][2][1]:]

    #now we have all our shapes

    xshapes = []
    yshapes = []
    
    #we look through each shape to get its dimensions
    #we also sometimes in our shape have parts of other shapes so we remove those and set them to the base colour
    for i in range(len(all_colour_locations)):
        
        #get dimensions
        yshape,xshape = colour_array[i].shape
 
        #add to list to store all the dimensions
        xshapes.append(xshape)
        yshapes.append(yshape)
        
        #loop through each piece of data for each shape list
        #if it contains a value of another shape set it to the base colour
        for x in range(yshape):
            for y in range(xshape):
                if colour_array[i][x][y] != all_colours[i] and colour_array[i][x][y] != base_colour:
                    colour_array[i][x][y] = base_colour

    #get the maximum x and y dimensions from the list 
    #to put the data together we need them all tp be the same size
    max_xshape = max(xshapes)
    max_yshape = max(yshapes)


    #here is the part where we make them all the same size
    for i in range(len(all_colour_locations)):
        #get the dimensions for the shape
        y_shape, x_shape = colour_array[i].shape
    
        #create a numpy array of the base colour
        #create one horizontal and one vertical so we can add these to make our shapes the same size
        values_to_add_y = np.full(max_yshape,base_colour)
        values_to_add_x = np.full(max_yshape,base_colour)
        #make this one vertical
        values_to_add_x.shape = (max_yshape,1)
  
        #if there is a difference of 2 here we add 2 horixontal np arrays
        #one at the start and one at the end
        if max_xshape - x_shape == 2:
            colour_array[i] = np.append(colour_array[i], values_to_add_x, axis = 1)
            colour_array[i] = np.append(values_to_add_x, colour_array[i] , axis = 1)
        
        #same here again but for y direction
        if max_yshape - y_shape == 2:
            colour_array[i] = np.vstack([colour_array[i], values_to_add_y])
            colour_array[i] = np.vstack([values_to_add_y, colour_array[i]])

        #we do the same again except if the difference is 4 we add 4
        #two at the start and two at the end
        if max_xshape - x_shape == 4:
            colour_array[i] = np.append(colour_array[i], values_to_add_x, axis = 1)
            colour_array[i] = np.append(colour_array[i], values_to_add_x, axis = 1)
            colour_array[i] = np.append(values_to_add_x, colour_array[i] , axis = 1)
            colour_array[i] = np.append(values_to_add_x, colour_array[i] , axis = 1)

        #same as above but add vertical arrays
        if max_yshape - y_shape == 4:
            colour_array[i] = np.vstack([colour_array[i], values_to_add_y])
            colour_array[i] = np.vstack([colour_array[i], values_to_add_y])
            colour_array[i] = np.vstack([values_to_add_y, colour_array[i]])
            colour_array[i] = np.vstack([values_to_add_y, colour_array[i]])

    
    #create a new numpy array of zeros in the shape that all of our shapes now are in
    newx = np.zeros((max_yshape,max_xshape), dtype=int)
    
    
    #loop through each colour
    for i in range(len(colour_array)):
        #loop through the data in the array that holds the shape
        for j in range(max_yshape):
            for k in range(max_xshape):
                #if its colour information we add it to the main array
                if colour_array[i][j][k] != base_colour:
                    newx[j][k] = colour_array[i][j][k]
    
    #now we have an array with all the colours we need 
    #except there is 0's instead of the base colour
    #so we replace these 
    for i in range(max_yshape):
        for j in range(max_xshape):
            if newx[i][j] == 0:
                newx[i][j] = base_colour
                
    #return the array
    return newx


def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        #directory = os.path.join("..", "data", "training")
        print(os.getcwd())
        #os.chdir("ARC/data/training")
        print(os.getcwd())
        #directory = "../data/training/"
        json_filename = os.path.join(os.getcwd(), ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for xtest, y in zip(train_input, train_output):
        yhat = solve(xtest)
        print("starting")
        show_result(xtest, y, yhat)
        #return
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(xtest, y, yhat):
    print("Input")
    print(xtest)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))

if __name__ == "__main__": main()

