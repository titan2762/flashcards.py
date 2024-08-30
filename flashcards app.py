# making a flashcard application to quiz users on questions

# ---- store flash cards
# ---- present flashcards randomly
# ---- make multichoice answers display with correct question
# ---- accept answers multichoice
# ---- check if answer is correct for the flashcard.
# ---- user can change what flashcard is displayd by "pass", or if commplete auto next
# ---- keep score of correct vs total numbers.
# option to replay questions we got wrong.
    # assign to new list (flashcard_incorrect)
    # if "review" is entered switch what list is being shown from maincards to incorrect cards
# if question has been answered correctly twice. do not show again
    # put in new list for answer right once.
    # if correct and already in 1 right list (try/except: .find()) 
    # put in new list for answer right twice
    # if question in 2 right list do not show
        # if all == do not show. end with congrats message

import random as r

flashcards = [
    "test Q1\n\ntest A1\ntest A2\ntest A3\ntest A4\n",
    "test Q2\n\ntest A1\ntest A2\ntest A3\ntest A4\n",
    "test Q3\n\ntest A1\ntest A2\ntest A3\ntest A4\n"
]

flashcard_answers = ["1", "2", "3"]

flashcard_incorrect = []

def maincards(flashcards):
    global flashcard_incorrect, correct_answers, total_displayed
    correct_answers = 0
    total_displayed = 0
    while True:
        global flashcard_incorrect
        total_cards = len(flashcards) - 1
        displayed = flashcards[r.randint(0, total_cards)]  # randomly picks a card to be displayed from total number of cards
        print(displayed)

        index = -1

        for card in flashcards:  # goes through cards and counts which card it is at
            index += 1
            if card == displayed:
                print(flashcard_answers[index])
                total_displayed += 1
                
                # prompt
                answer = input("What is the answer? (type 'quit' to exit) >> ")
                
                if answer.lower() == "quit":
                    print("Quitting the flashcards program.")
                    return flashcard_incorrect, correct_answers # Exits the function

                if answer.lower() == "pass":
                    total_displayed -= 1
                    print("Passing\n")
                    continue

                # correct answer sequence
                if flashcard_answers[index] == answer:
                    correct_answers += 1
                    print("Good job!\n")
                    continue
                
                # incorrect answer sequence
                else:
                    flashcard_incorrect.append(displayed)
                    print("Nice try\n")
                    continue                
            else:
                continue

def incorrectcards():
    print("End")

maincards(flashcards)
print(correct_answers)
print(flashcard_incorrect)
