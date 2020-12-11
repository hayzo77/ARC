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
                    get_new_location("")
                    value = xcounter - xcentre
                    xnew = xcentre - value
                    
                    if x[ycounter-1][xnew] ==  9:
                        value = ycounter - ycentre
                        ynew = ycentre - value
                        x[yval][xval] = x[ynew][xcounter-1]    
                    else:
                        x[yval][xval] = x[ycounter-1][xnew]
                        
                #outside square 1 to the left side
                elif xcounter <= xmin and ycounter > ymin and xcounter <= 16 and ycounter <= 16:
                    value = ycounter - ycentre
                    ynew = ycentre - value
                    x[yval][xval] = x[ynew][xcounter-1]     
                    
                    
                    
                #square 2 
                elif xcounter >= 16 and ycounter <= 16:
                    value = xcounter - xcentre
                    xnew = xcentre - value
                    
                    if x[ycounter-1][xnew] ==  9:
                        value = ycounter - ycentre
                        ynew = ycentre - value
                        x[yval][xval] = x[ynew][xcounter-1] 
                    else:
                        x[yval][xval] = x[ycounter-1][xnew]    
                        square = 2

                    
                #square 3 
                elif xcounter <= 16 and ycounter >= 16  and xcounter > xmin:
                    value = xcounter - xcentre
                    xnew = xcentre - value
                    
                    if x[ycounter-1][xnew] == 9:
                        value = ycounter - ycentre
                        ynew = ycentre - value
                        x[yval][xval] = x[ynew][xcounter-1] 
                    else:
                        x[yval][xval] = x[ycounter-1][xnew]
                        
                #outside square 3 to the left side
                elif xcounter <= xmin and ycounter > ymin and xcounter <= 16 and ycounter >= 16:                    
                    value = ycounter - ycentre
                    ynew = ycentre - value
                    x[yval][xval] = x[ynew][xcounter-1] 
                    
                    
                    
                #square 4
                elif xcounter >= 16 and ycounter >= 16:
                    value = xcounter - xcentre
                    xnew = xcentre - value
                    if x[ycounter-1][xnew]  == 9:
                        value = ycounter - ycentre
                        ynew = ycentre - value
                        x[yval][xval] = x[ynew][xcounter-1] 
                    else:
                        x[yval][xval] = x[ycounter-1][xnew] 
                    
                    
            xcounter = xcounter + 1 
        ycounter = ycounter + 1 

    return x


def get_new_location(xy, x, value, centre, counter):
    if xy == "x":
        value = counter - centre
        xnew = centre - value
        return xnew
    elif xy == "y":
        value = counter - centre
        ynew = centre - value
        return ynew


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
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
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

