import random

memoryBank = {}

def player(prev_play, opponent_history=[]):
  global memoryBank

  # to beat abbey consistently, i had to add a little randomness to my guesses
  if random.randint(0, 2000) == 0:
    choices = ['S', 'P', 'R']
    guess = choices[random.randint(0, 2)]
    return guess
  
  # sets how far back in the history the player will look for patterns
  n = 3

  # add to opponent history
  if prev_play in ["R","P","S"]:
    opponent_history.append(prev_play)

  guess = "R" # default guess

  # limit length of opponent_history by deleting the oldest
  if len(opponent_history)>n + 1:
    opponent_history.pop(0)

    # this is the sequence we'll use to test the possible next opponent hand
    sequenceToTest = "".join(opponent_history[-n:])
    # this is the sequence we'll store in the memoryBank
    sequenceToStore = "".join(opponent_history[-(n+1):])
    if sequenceToStore in memoryBank.keys():
      memoryBank[sequenceToStore]+=1
    else:
      memoryBank[sequenceToStore]=1

    # list of all possible next choices by the opponent
    possible = [sequenceToTest+"R", sequenceToTest+"P", sequenceToTest+"S"]

    # if the possible sequence isn't in the memoryBank already, add it with a value of 0
    for i in possible:
      if not i in memoryBank.keys():
        memoryBank[i] = 0

    # most likely next choice by the opponent based on previous choices
    mostLikely = max(possible, key=lambda key: memoryBank[key])[-1:]
    
    if mostLikely == "P":
      guess = "S"
    if mostLikely == "R":
      guess = "P"
    if mostLikely == "S":
      guess = "R"

  return guess