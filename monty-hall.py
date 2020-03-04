"""
This program is a Monty Hall Problem simulator
"""
##imports
import numpy as np
import random

## functions
def montyHallGame (totalGames, totalDoors, totalRevealed):
    """
    Inputs:
    totalGames is the number of times you want the simulation to be run
    totalDoors is the number of doors you want in the simulation
    totalRevealed is the number of doors you want to be revealed

    This function will run a Monty Hall simulation and return results summarizing
    how many times the initial choice was correct and how many times the switched
    choice is correct.
    """
    numberOfGames = 0
    choice = 0
    switch = 0

    while numberOfGames < totalGames:

        revealedSoFar = 0

        # create array of doors labelled from 1-100
        doors = list(range(1,totalDoors + 1))

        # shuffle doors
        random.shuffle(doors)
        # insert prize into random door
        prizeLocation = random.randint(0,len(doors) - 1)
        # choose a random door
        choiceLocation = random.randint(0,len(doors) - 1)

        # store the value of the prize and choice
        prizeValue = doors[prizeLocation]
        choiceValue = doors[choiceLocation]

        # remove it from the potential pool of doors to be revealed
        # if the choice and location are the same, only remove it once
        if prizeLocation == choiceLocation:
            doors.remove(prizeValue)
        else:
            doors.remove(prizeValue)
            doors.remove(choiceValue)


        # reveal another door that is different from the prize and choice door (removed from the pool)
        # if we are revealing more than 1 door, only reveal new doors that have not yet been revealed (by removing the doors from the pool)
        while revealedSoFar < totalRevealed:
            # position in the doors array to reveal
            revealLocation = random.randint(0,(len(doors) - 1))
            # store the revealed value to remove from the available doors
            revealValue = doors[revealLocation]
            revealedSoFar += 1
            doors.remove(revealValue)


        # add the doors removed earlier back to the pool
        # ONLY add one of the doors back to the pool if the prize and choice location are the same
        if prizeValue == choiceValue:
            doors.append(prizeValue)
        else:
            doors.append(prizeValue)
            doors.append(choiceValue)


        # then switch to a door different from the one picked
        while True:
            switchLocation = random.randint(0,len(doors) - 1)
            switchValue = doors[switchLocation]
            if switchValue == choiceValue:
                continue
            else:
                break

        if choiceValue == prizeValue:
            choice += 1
        elif switchValue == prizeValue:
            switch +=1

        numberOfGames += 1

    #print out results of the simulation
    print("Results of " + str(totalGames) + " games - " + str(totalDoors) + " Doors")
    print("Total times original choice was correct: " + str(choice) + " (" + str(round(((choice/totalGames)*100),2)) +"%)")
    print("Total times switched choice was correct: " + str(switch) + " (" + str(round(((switch/totalGames)*100),2)) +"%)\n")

## run simulations
# run the simulation with different # of doors and # of revealed doors
montyHallGame(1000000, 100, 98)
montyHallGame(1000000, 10, 8)
montyHallGame(1000000, 3, 1)