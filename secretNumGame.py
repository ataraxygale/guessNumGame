def secretNumGame():
    secret_number = 777

    print(
        """
        +========================================+
        | Welcome to: 🧙‍♂️ SORCERER'S PUZZLE TOWER |
          What is my secret number?!             |
        | Enter an integer and guess.            |
        | Guess wrong: YOU ARE TRAPPED           |
        | Guess correctly: YOU ARE FREE          |
        +========================================+
        """)


    def INTERNALSCREAMINGBUBBLE():
        while True:
            try:
                return int(input("ENTER A NUMBER: \n"))
            except ValueError:
                print("YOU WILL STAY HERE FOREVER. TRY AGAIN MORTAL\n")


    numGuess = INTERNALSCREAMINGBUBBLE()
    guessCount = 1

    """
                numGuess = int(input("GUESS MY SECRET NUMBER. MUAHAHA. ENTER A NUMBER BETWEEN 1 AND 1000. *DIABOLICAL CACKLING*\n"))
    """
    while numGuess != 777:
        try:
            numGuess = int(input("Ha ha! You're stuck in my loop FOREVER\n"))
        except ValueError:
            print("Invalid input: Please enter an integer FOOL\n")
        guessCount += 1

    print("WELL DONE, FELLOW SORCERER/ESS 🪄 \n")

    if guessCount > 5:
        print(f"You took {guessCount} human attempts. PATHETIC")
    else:
        print(f"You took {guessCount} human attempt/s. ACCEPTABLE")

    YN = input("Would you like to play again? Y/N\n").strip().lower()

    if YN == 'y':
        secretNumGame()
    else:
        print("\nFarewell, mortal")
        exit()

if __name__ == "__main__":
    secretNumGame()
    
