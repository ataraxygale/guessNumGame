# guessNumGame
- A fun guess the number game in a puzzle tower
- This game integrates: user input and input validation/exception error handling and attempt counters
- Also integrated: a while loop which only ends when the game has been solved

## 📦 Notes
- This is part of a growing set of small programs documenting my Python learning journey


## 🧠 How It Works
- Prompts the user to guess a secret number
- If they guess wrong, they are prompted again in an infinite loop until they guess correctly
- If they enter something other than an integer, they are reminded to enter an integer from the villain of the puzzle tower
- Once the secret number is guessed, the player is prompted to play again or exit the game


## 🧪 Example Output
```
        +========================================+
        | Welcome to: 🧙‍♂️ SORCERER'S PUZZLE TOWER |
          What is my secret number?!             |
        | Enter an integer and guess.            |
        | Guess wrong: YOU ARE TRAPPED           |
        | Guess correctly: YOU ARE FREE          |
        +========================================+
        
ENTER A NUMBER: 
789
Ha ha! You're stuck in my loop FOREVER
444
Ha ha! You're stuck in my loop FOREVER
777
WELL DONE, FELLOW SORCERER/ESS 🪄 

You took 3 human attempt/s. ACCEPTABLE
Would you like to play again? Y/N
n

Farewell, mortal

Process finished with exit code 0
```


