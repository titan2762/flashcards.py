# making a flashcard application to quiz users on questions

# ---- store flash cards
# ---- present flashcards randomly
# make multichoice answers display with correct question
# accept answers multichoice
# check if answer is correct for the flashcard.
# user can change what flashcard is displayd by "pass", or if commplete auto next
# keep score or correct vs total numbers.
# option to replay question we got wrong.
# if question has been answered correctly twice. do not show again
    #

import random as r

stop = False

flashcards = [
    "test Q1\ntest A1\ntest A2\ntest A3\ntest A4\n",
    "test Q2\ntest A1\ntest A2\ntest A3\ntest A4\n",
    "test Q3\ntest A1\ntest A2\ntest A3\ntest A4\n"
]

flashcard_answers = ["1", "2", "3"]

flashcard_incorrect = ["placeholder"]


def maincards(flashcards):
    index = -1
    correct_answers = 0
    while True:
        global flashcard_incorrect, stop
        total_cards = len(flashcards) - 1
        displayed = flashcards[r.randint(0, total_cards)]# randomly picks a card to be displayed from total number of cards
        print(displayed)

        index = -1
        correct_answers = 0

        



        for card in flashcards: #goes through cards and counts which card it is at
            index += 1
            if card == displayed:
                print(flashcard_answers[index])
                
                #prompt
                answer = input("what is the answer? >> ")
                


                    # correct answer sequence
                if flashcard_answers[index] == answer:
                    correct_answers += 1
                    print("good shit my guy\n")
                    continue
                
                # incorrect answer sequence
                elif flashcard_answers[index] != answer:
                    flashcard_incorrect.append(displayed)
                    print("nice try\n")
                    continue

                if answer.lower() == 'quit':
                    print("Quitting the flashcards program.")
                    stop = True
            else:
                continue

def end():
    print("end")

maincards(flashcards)
print(flashcard_incorrect)