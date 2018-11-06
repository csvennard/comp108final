# -*- coding: utf-8 -*- hello
"""
Created on Fri Nov  2 22:28:31 2018

@author: Chris Vennard
"""
import matplotlib.pyplot as plt
import numpy as np
import random

def display_env(env):#NOT ALTERED FROM PCUTTER #commented out to speed up processing
    plt.imshow(env)
    plt.show()
    plt.pause(0.00001)
    

"""
    Randomly initialize a 2d array to represent empty and tree
    distribution 0's will represent empty space and 1 will represent trees
    PARAMS:
        width: width of the environment(2D array).
        height: height of the environment(2D array).
        prop_empty: beginning proportion of empty cells.
        prop_trees: beginning proportion of trees.
        prop_burning: beginning proportion of burning trees
    RETURNS:
        env - the initialized environment(2D array).
    """
def initial_env(width, height, prop_trees, prop_burning):
   
    if (prop_trees + prop_burning) > 1:
        raise ValueError('Percentage burning plus percentage trees for initial ' +
                         'environment is greater than 100%!')
    else:
        arr = np.random.choice([0, 1, 2],size=(width,height),p=[1-(prop_burning+prop_trees),prop_trees,prop_burning])
        return arr
    
def neighbors(env, r, c):
    neighboring = np.zeros(4)
    neir = [-1, 1, 0, 0] 
    neic = [0, 0, -1, 1] 
    for i in range(4):
        neighboring[i] = env[neir[i]][neic[i]]
    return neighboring

"""
    Give a randomly selected cell a chance to burn if it contains trees and is next to fire
    PARAMS:
        env: A two dimensional array representing the environment
        b: probability that neighboring trees will also catch on fire
    """
def burn(env,b):
    next_env = np.zeros((len(env),len(env)))
    for row in range(len(env)):
        for col in range(len(env[row])):
            if env[row][col] == 1:
                neighboring = neighbors(env, row, col)
                if any(neighboring) == 2:
                    next_env[row][col] = 2
            else:
                next_env[row][col] = env[row][col]
    return next_env

#def quench(env, w):
    
    #print


def pop_count(env):
    tree_count = 0 #starting values of 0 for each species
    fire_count = 0
    empty_count = 0
    for i in range(env.shape[0]): #loop will go through each cell and count how many of each species there is
        for j in range(env.shape[1]):
            if env[i][j] == 1:
                tree_count = tree_count +1
            elif env[i][j] == 2:
                fire_count = fire_count +1
            elif env[i][j] == 0:
                empty_count = empty_count +1
    return tree_count, fire_count, empty_count


def Burnbaby(n_days, b, w, prop_trees, prop_burning, env_rows, env_cols):
    # Initialize the environment with prey and predator.
    env = initial_env(env_rows, env_cols, prop_trees, prop_burning)
    empty_pop = []
    tree_pop = []
    fire_pop = []

    # Simulation for n days.
    for day in range(n_days):
        for i in range((env_rows * env_cols)):
            burn(env, b)
            #quench(env, w)
        #env = next_env
        tree_count, fire_count, empty_count = pop_count(env) #calls the population counting function
        tree_pop.append(tree_count) #appends the result to the list which can then be graphed
        fire_pop.append(fire_count)
        empty_pop.append(empty_count)
        display_env(env)#commented out to make it run faster
        #print   # Put a blank line between environments
    
    days = range(n_days)
    '''everything below is used to create a graph of each of the populations over time'''
    plt.plot(range(len(days)), tree_pop, 'g-', range(len(days)), fire_pop, 'r-', range(len(days)), empty_pop, 'b-')
    plt.title('forest fires')
    plt.xlabel('Day')
    plt.ylabel('Number of sq miles')
    plt.legend(['trees', 'fires', 'Empty'])

    

