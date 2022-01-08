word = input("What word would you like to give: ")
limit = int(input("How many chances would you like to give: "))
print("Guesses Left: {}".format(limit))

guesses = []

finish = False 

while not finish: 

    for letter in word: 
        if letter in guesses: 
            print (letter, end=" ")
        else: 
            print ("_ ", end=" ")
    print (" ")
    guess = input("Your Guess: ")
    guesses.append(guess)
    if guess in word: 
        print("Correct")
    else:
        print("Incorrect. Letter is not in the word.")
        print("you have", limit,"guesses left")
        limit -= 1
        if limit == 0: 
            break
    
    finish = True

    for letter in word: 
        if letter not in guesses: 
            finish = False

if finish == True: 
    print("Congratulations, you found the word!")
else: 
    print ("Game Over")
