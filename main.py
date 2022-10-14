# Display the title of the game as 'Hulk Smash' using an Art Generator
print(r"""

 __ __  __ __  _      __  _       _____ ___ ___   ____  _____ __ __  __ 
|  T  T|  T  T| T    |  l/ ]     / ___/|   T   T /    T/ ___/|  T  T|  T
|  l  ||  |  || |    |  ' /     (   \_ | _   _ |Y  o  (   \_ |  l  ||  |
|  _  ||  |  || l___ |    \      \__  T|  \_/  ||     |\__  T|  _  ||__j
|  |  ||  :  ||     T|     Y     /  \ ||   |   ||  _  |/  \ ||  |  | __ 
|  |  |l     ||     ||  .  |     \    ||   |   ||  |  |\    ||  |  ||  T
l__j__j \__,_jl_____jl__j\_j      \___jl___j___jl__j__j \___jl__j__jl__j
                                                                        
""")
# Display a message telling the user the instructions on how to play the game
print("Welcome to Hulk Smash!  Today you will answer a few questions to test")
print("how much you know about the Hulk.  Let's see if you're a true HULK fan!")
print("You will answer a few TRUE or FALSE questions. Please ONLY enter T or F")
print("when it's your turn to answer.  Have fun!")
print()
# Create a variable in a tuple that holds the 3 quiz questions
questions = ("Q1. The Hulk's real name is Bruce Banner", "Q2. The Hulk turns purple when he gets upset", "Q3. The Hulk is a member of the Marvel Comic Universe")
# Create a variable in a tuple that holds the answers 'T' or 'F' for each question
answers = ("T", "F", "T")
# Create a variable that holds a default value for the 2 answer options
answerOptions = ""
# Create a variable that holds the number of attempts
count = 0
# Create a variable that counts the number of questions in the tuple
numberQuestions = len(questions)
# Create a for loop with indexing notations for the 3 questions
for index in range(numberQuestions):
  print(questions[index])
  # Create a while loop that loops as long as the users answer does NOT equal 'T' and 'F'
  while(answerOptions != "T" and answerOptions != "F"):
    # Tell the user to input 'T' or 'F' and store as a variable
    answerOptions = input("Please enter 'T' for TRUE or 'F' for FALSE: ")
    # Compare and track if the users answer is the same as the 'answers' tuple 
    if(answerOptions == answers[index]):
      count += 1
  # Create a variable that holds a default value for the the answer options inside the for loop
  answerOptions = "" 
# Display a message telling the user how many attempts they took
print(f"You got {count} out of {numberQuestions} correct.  Thanks for playing!")