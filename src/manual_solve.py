#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.
def solve_3631a71a(x):
    """
    Rules for this example are 
    1) all 4 squares are the same when we are in bounds 
    2) when out of bounds then copy what also has this bounds 
    """


    xlen, ylen = x.shape
    
    xcounter = 1
    ycounter = 1
    xcentre = 16
    ycentre = 16
    square = 0 
    pattern_size = 28
    xymax = pattern_size/2
    xmin = xcentre - xymax
    ymin = ycentre - xymax
    pattern_max = 30
    
    for yval in range(ylen):
        xcounter = 1

        for xval in range(ylen):
            if x[yval][xval] == 9:
                
                
                #square 1
                if xcounter <= 16 and ycounter <= 16 and xcounter > xmin:
                    xnew = get_new_location(xcentre, xcounter)
                    
                    if x[ycounter-1][xnew] ==  9:
                        ynew = get_new_location(ycentre, ycounter)
                        x[yval][xval] = x[ynew][xcounter-1]    
                    else:
                        x[yval][xval] = x[ycounter-1][xnew]
                        
                #outside square 1 to the left side
                elif xcounter <= xmin and ycounter > ymin and xcounter <= 16 and ycounter <= 16:
                    ynew = get_new_location(ycentre, ycounter)
                    x[yval][xval] = x[ynew][xcounter-1]     
                    
                    
                    
                #square 2 
                elif xcounter >= 16 and ycounter <= 16:
                    xnew = get_new_location(xcentre, xcounter)

                    if x[ycounter-1][xnew] ==  9:
                        ynew = get_new_location(ycentre, ycounter)
                        x[yval][xval] = x[ynew][xcounter-1] 
                    else:
                        x[yval][xval] = x[ycounter-1][xnew]    

                    
                #square 3 
                elif xcounter <= 16 and ycounter >= 16  and xcounter > xmin:
                    xnew = get_new_location(xcentre, xcounter)
                    
                    if x[ycounter-1][xnew] == 9:
                        ynew = get_new_location(ycentre, ycounter)
                        x[yval][xval] = x[ynew][xcounter-1] 
                    else:
                        x[yval][xval] = x[ycounter-1][xnew]
                        
                #outside square 3 to the left side
                elif xcounter <= xmin and ycounter > ymin and xcounter <= 16 and ycounter >= 16:                    
                    ynew = get_new_location(ycentre, ycounter)

                    x[yval][xval] = x[ynew][xcounter-1] 
                    
                    
                    
                #square 4
                elif xcounter >= 16 and ycounter >= 16:
                    xnew = get_new_location(xcentre, xcounter)
                    if x[ycounter-1][xnew]  == 9:
                        ynew = get_new_location(ycentre, ycounter)
                        x[yval][xval] = x[ynew][xcounter-1] 
                    else:
                        x[yval][xval] = x[ycounter-1][xnew] 
                    
                    
            xcounter = xcounter + 1 
        ycounter = ycounter + 1 

    return x


def get_new_location(centre, position):
    value = position - centre
    new = centre - value
    return new

def solve_484b58aa(x):
    
    """
    with this one we need to be able to detect the diagonal pattern
    if the next diagonal square is the same as the previous then all are that colour
    if not we will store the colour in a colour array and then move on
    """
    first_half = []

    xdimension, ydimension = x.shape   
    if xdimension == ydimension:
        dimension = xdimension
    #there are 30 diagonals and we need to loop through them
    print(dimension)
    for size_its in range(dimension):
        actual_size = size_its + 1
        array = x[:actual_size, :actual_size]
        
        
        first_diagonals = np.flipud(array).diagonal()
        first_half.append(first_diagonals)
        

        print(first_diagonals)

    #print(array)
    #array = np.flipud(array)
    newx = x.copy()
    newx = np.rot90(newx)
    newx = np.rot90(newx)

        
    #print(newx)
    second_half = []
    
    for size_its in range(dimension-1):
        actual_size = size_its + 1
        array = newx[:actual_size, :actual_size]
        
        second_diagonals = np.flipud(array).diagonal()
        
        print(second_diagonals)
        second_half.append(np.flip(second_diagonals))
        
    #list of patterns
    #we need to firstly select a half to train on 
    first = np.array(first_half)
    second = np.array(second_half)
    
    zero_count_first = 0
    for i in first:
        for j in i:
            if j == 0:
                zero_count_first = zero_count_first + 1
                
    zero_count_second = 0  
    for i in second:
        for j in i:
            if j == 0:
                zero_count_second = zero_count_second + 1
                
    print(zero_count_first)
    print(zero_count_second)
    
    if zero_count_first <= zero_count_second:
        training_set = first
    else: 
        training_set = second


    training_set = training_set[5:]
    pattern_list = []
    for diagonal in training_set:
        #we need to get the pattern
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
            
    print("helper1")
    print(pattern_list)
    longest_pattern = [len(i) for i in pattern_list]
    pattern_to_search = max(pattern_list, key=len)
    #print(pattern_to_search)
    print(pattern_list)
    print("helper2")
 
    index = 0
    exitbool = False
    for pattern in pattern_list:
        index = index + 1
        if pattern == pattern_to_search and exitbool == False:
            actual_index = index
            exitbool = True
    
    print(pattern_list)  
    pattern_list = pattern_list[actual_index:]
    print(pattern_list)
    
    all_patterns = []
    all_patterns.append({1: pattern_to_search})
    pattern_number = 1
    pattern_found = False
    number_of_patterns = 1
    for pattern in pattern_list:
        pattern_number = pattern_number + 1
        if pattern_found == False:
            for i in range(4):
                print(i)
                print(pattern_to_search)
                print(pattern)
                if np.all(pattern_to_search==pattern):
                    print("WE HAVE A PATTERN")
                    pattern_found = True
                else:
                    #we need to label each pattern
                    pattern_to_search = np.roll(pattern_to_search, 1)
                    patterntoappend = {pattern_number: pattern}
            
            if pattern_found == False:
                all_patterns.append(patterntoappend)
                number_of_patterns = number_of_patterns + 1

                
        #we are checking for the pattern we will roll 5 times 
        
    print(all_patterns)

    second_reversed = []

    for i in range(second.size):
        second_reversed.append(second[second.size - (i + 1)])
    
    print(first)
    print("first_done")
    print(second_reversed)
    
    all_data = []
    for i in first:
        all_data.append(i)
    for j in second_reversed:
        all_data.append(j)

    all_data_numpy = np.array(all_data)        
    print("")
    print("")
    print(all_data_numpy.size)
    
    
    #now we need to tag each one with their respective patttern        
    print(all_patterns)
    
    #lets take the middle one and move right by the number of patterns
    
    print(number_of_patterns)
    pattern_max = 28 + number_of_patterns
    print(pattern_max)
    
    pattern_recognition = []
    
    counter = 0
    for i in all_data_numpy:
        if counter >= 29 and counter <= pattern_max:
            pattern_recognition.append(i)
        counter = counter + 1
        
    pattern_recognition = np.array(pattern_recognition)
    #now we need to see which one matches the pattern
    
    
    pattern_size = pattern_to_search.size
    
    final_match_index = 0
    match_index = 28
    for pattern in pattern_recognition:
        match_index = match_index + 1
        print(pattern[:pattern_size])
        print(pattern_to_search)
        for i in range(8):
            if np.all(pattern_to_search==pattern[:pattern_size]):
                print("WE HAVE A PATTERN")
                final_match_index = match_index
                #pattern_found = True
            else:
                #we need to label each pattern
                pattern_to_search = np.roll(pattern_to_search, 1)
    
    print(final_match_index)
    #pattern 1 matches index 30 so we need to iterate over all others
    #and index them 
    
    #we need to take all elements after 30
    #and take all elements before 30 
    
    before_match_list = all_data_numpy[:final_match_index]
    after_match_list = all_data_numpy[final_match_index:]
    
    print(before_match_list)
    print("")
    print("")
    print(after_match_list)
    
    pattern_index_list = np.zeros((all_data_numpy.size,), dtype=int)
    #print(pattern_index_list)
    
    #now we need to loop through each and assign pattern value to each
    idx = (before_match_list.size)-1
    patternidx = 1
    for l in before_match_list:
        
        pattern_index_list[idx] = patternidx
        
        if patternidx == number_of_patterns:
            patternidx = 1
        else:
            patternidx = patternidx + 1
            
        idx = idx - 1


    
    idx = (after_match_list.size)+2
    patternidx = 1
    print(pattern_index_list)
    for l in after_match_list:
        
        
        pattern_index_list[idx] = patternidx
        
        if patternidx == number_of_patterns:
            patternidx = 1
        else:
            patternidx = patternidx + 1
            
        idx = idx + 1
        
        

    print(pattern_index_list)
    
    return x


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
    #for x, y in zip(train_input, train_output):
        #yhat = solve(x)
        #show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        #show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
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

