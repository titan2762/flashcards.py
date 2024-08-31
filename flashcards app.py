# making a flashcard application to quiz users on questions

# ---- store flash cards
# ---- present flashcards randomly
# ---- make multichoice answers display with correct question
# ---- accept answers multichoice
# ---- check if answer is correct for the flashcard.
# ---- user can change what flashcard is displayd by "pass", or if commplete auto next
# ---- keep score of correct vs total numbers.
# ---- option to replay questions we got wrong.
    # ---- assign to new list (flashcard_incorrect)
    # ---- if "review" is entered switch what list is being shown from maincards to incorrect cards
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

    correct_answers_crate1 = []
    correct_answers_crate2 = []

    global flashcard_incorrect, correct_answers, total_displayed
    correct_answers = 0
    total_displayed = 0
    while True:
        total_cards = len(flashcards) - 1
        displayed = flashcards[r.randint(0, total_cards)]  # randomly picks a card to be displayed from total number of cards
        print(displayed)

        index = -1

        for card in flashcards:  # goes through cards and counts which card it is at
            index += 1
            if card == displayed:
                if card in correct_answers_crate2:
                    continue
                else:
                    print(flashcard_answers[index])
                    total_displayed += 1
                
                    # prompt
                    answer = input("... IN MAIN ...What is the answer? (type 'quit' to exit) >> ")
                
                    if answer.lower() == "rev":
                        print("going to review incorrect answers")
                        incorrectcards()

                    if answer.lower() == "quit":
                        total_displayed -= 1
                        print(correct_answers)
                        print(total_displayed)
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
                        if card in correct_answers_crate1:
                            correct_answers_crate2.append(card)
                        else:
                            correct_answers_crate1.append(card)
                        continue
                
                    # incorrect answer sequence
                    else:
                        flashcard_incorrect.append(displayed)
                        print("Nice try\n")
                        continue                
            else:
                continue

def incorrectcards():
    global flashcard_incorrect, correct_answers, total_displayed
    correct_answers = 0
    total_displayed = 0
    if not flashcard_incorrect:
        print("There are no incorrect cards to review.")
        return
    while True:
            total_cards_incorrect = len(flashcard_incorrect) - 1
            displayed = flashcard_incorrect[r.randint(0, total_cards_incorrect)]  # Randomly pick a card from incorrect ones

            # Find the index of the displayed card in the original flashcards list
            for i, card in enumerate(flashcards):
                if card == displayed:
                    break   # add logic to find same one in flashcards list

            print(displayed)
            print(flashcard_answers[i])
            answer_for_incorrect = flashcard_answers[i]  # Use the correct index to get the answer
            total_displayed += 1

                # prompt
            answer = input("... IN REV ...What is the answer? (type 'quit' to exit) >> ")
                
            if answer.lower() == "main":
                print("going to main study")
                maincards(flashcards)

            if answer.lower() == "quit":
                total_displayed -= 1
                print(correct_answers)
                print(total_displayed)
                print("Quitting the flashcards program.")
                return correct_answers # Exits the function

            if answer.lower() == "pass":
                total_displayed -= 1
                print("Passing\n")
                continue

                # correct answer sequence
            if answer_for_incorrect == answer:
                correct_answers += 1
                print("Good job!\n")
                continue
                
                # incorrect answer sequence
            else:
                print("Nice try\n")
                continue                

maincards(flashcards)