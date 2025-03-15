from os import path
import random



# Loading the Data
def load_questions():
    """Load questions from quest_load.txt file into a dictionary."""
    questions = {}
    
    # Check if file exists and read it
    if not path.exists('quest_load.txt'):
        print("\nError: quest_load.txt file not found!")
        return {}
        
    with open('quest_load.txt', 'r') as file:
        for line in file:
            if '|' not in line:
                continue
            question, answer, points = line.strip().split('|')
            if points.isdigit():
                questions[question] = [answer, int(points)]
    
    if questions:
        print("\nQuestions loaded successfully!")
    else:
        print("\nWarning: No valid questions found in file")
    
    return questions



# Adding my questions
def add_question():
    """Add a new question to the quest_load.txt file."""
    question = input("\nEnter the question: ")
    answer = input("Enter the answer: ")
    points = input("Enter the points value: ")
    
    # Simple validation for points
    if not points.isdigit():
        print("\nError: Points must be a number!")
        return
    
    # Write to file
    with open('quest_load.txt', 'a') as file:
        file.write(f"\n{question}|{answer}|{points}")
    print("\nQuestion added successfully!")



# Displaying all questions present in Questions Dictonary.
def show_questions(questions):
    """Display all questions and their point values."""
    if not questions:
        print("\nNo questions loaded! Please load questions first.")
        return
    
    print("\n=== Questions List ===")
    for question, (answer, points) in questions.items():
        print(f"\nQuestion: {question}")
        print(f"Points: {points}")
    print("=" * 20)




# Loading and presenting leadership board from the File "LEADERS>TXT"
def load_leaderboard():
    """Load the leaderboard from leaders.txt file."""
    leaderboard = {}
    
    if not path.exists('leaders.txt'):
        print("\nNote: No leaderboard file found. A new one will be created.")
        return leaderboard
        
    with open('leaders.txt', 'r') as file:
        for line in file:
            if '|' in line:
                name, score = line.strip().split('|')
                if score.isdigit():
                    leaderboard[name] = int(score)
    
    return leaderboard



# Wrting to "Leader.txt' to save player,
def save_leaderboard(leaderboard):
    """Save the leaderboard to leaders.txt file."""
    with open('leaders.txt', 'w') as file:
        # Sort by score before saving
        sorted_scores = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        for name, score in sorted_scores:
            file.write(f"{name}|{score}\n")



# Dosplaying all scores/
def show_score():
    """Display the leaderboard in descending order."""
    leaderboard = load_leaderboard()
    if not leaderboard:
        print("\nNo scores recorded yet!")
        return
    
    print("\n<<< LEADER BOARD >>>")
    for name, score in sorted(leaderboard.items(), key=lambda x: x[1], reverse=True):
        print(f"{name:<10}\t{score}")



# ACTUAL and main game 
def play_game(questions, player_name):
    """Play the trivia game."""
    if not questions:
        print("\nNo questions loaded! Please load questions first.")
        return
    
    # Set up player score
    leaderboard = load_leaderboard()
    previous_score = leaderboard.get(player_name, 0)
    
    # Welcome message
    if player_name in leaderboard:
        print(f"\nWelcome back {player_name}! Your previous score was {previous_score}")
    else:
        print(f"\nWelcome to Trivia Madness, {player_name}!")
    
    playing = True
    while playing:
        # Get number of questions
        max_questions = len(questions)
        num_questions = input(f"\nHow many questions would you like to try? (1-{max_questions}): ")
        
        if not num_questions.isdigit():
            print("\nPlease enter a valid number!")
            continue
            
        num_questions = int(num_questions)
        if num_questions < 1 or num_questions > max_questions:
            print(f"\nPlease select a number between 1 and {max_questions}")
            continue
        
        # Game loop
        score = previous_score
        game_questions = random.sample(list(questions.items()), num_questions)
        
        for question, (answer, points) in game_questions:
            print(f"\n{question}")
            user_answer = input().strip().lower()
            
            if user_answer == answer.lower():
                print("Correct!")
                score += points
            else:
                print("Incorrect Response")
            
            print(f"Your current score is {score}.")
        
        # Update score and ask to play again
        leaderboard[player_name] = score
        save_leaderboard(leaderboard)
        
        play_again = input("\nDo you want to play again? Y to play, Q to quit: ").upper()
        if play_again != 'Y':
            playing = False




# Start
questions = {}

while True:
    print("\nPlease select an item from the menu below")
    print("1- Load Questions")
    print("2- Add question")
    print("3- Show Questions")
    print("4- Play game")
    print("5- Show Score")
    print("6- Quit")
    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == '1':
        questions = load_questions()
        
        
    elif choice == '2':
        add_question()
        
        
    elif choice == '3':
        show_questions(questions)
        
        
    elif choice == '4':
        if not questions:
            print("\nPlease load questions first!")
            continue
        player_name = input("\nPlease enter your first name: ").capitalize()
        play_game(questions, player_name)
        
        
    elif choice == '5':
        show_score()
        
        
    elif choice == '6':
        print("\nThanks for playing! Goodbye!")
        break
    
    
    else:
        print("\nInvalid choice! Please select 1-6")