import random
import time
import json
import base64

# Todo Shuffle Answers
KEY = 'LS0gKGMpIDIwMjMgQWxleCBWZXJnYXJhIC0t'

FILENAME = "QA.json"

def Main():
    print(base64.b64decode(KEY))
    MODE = input("Select a mode: (ADD) (STUDY) \n")
    A = "ADD"; B = "STUDY"
    if MODE.lower() == A.lower():
        print("~ ADDING MODE ~ \n")
        AddMode()
    elif MODE.lower() == B.lower():
        print("~ STUDY MODE ~ \n")
        StudyMode()

def AddMode():
    QUESTION = input("Input Question: ")
    NUM_ANSWERS = input("Input # of Answers (max=4): ")
        
    if (NUM_ANSWERS.isdigit() and int(NUM_ANSWERS) <= 4):
        TEMP_ARRAY = []
        for i in range(int(NUM_ANSWERS)):
            ANSWER = input("Input an Answer: ")
            TEMP_ARRAY.append(ANSWER)
        
        # Evaluate which answer is the correct one & store that
        ITTR_VALUE = 0
        for text in TEMP_ARRAY:
            ITTR_VALUE+=1
            print("(" + str(ITTR_VALUE) + ") '" + text + "'")
            
        CORRECT_ANSWER = input("Indicate which answer is correct by typing it's corresponding number: ")
        if (CORRECT_ANSWER.isdigit() and int(CORRECT_ANSWER) <= int(NUM_ANSWERS)):
            print("The correct answer is: '" + TEMP_ARRAY[int(CORRECT_ANSWER)-1] + "'\n")
            #ANSWER_TITLE = TEMP_ARRAY[int(CORRECT_ANSWER)-1]
            
        RESULT = {"question":str(QUESTION),
                  "answers":TEMP_ARRAY,
                  "correct_answer":CORRECT_ANSWER#ANSWER_TITLE
                  }
        
        Write_JSON(RESULT)
        # Ask if the user would like to add more
        CONTINUE = input("Would you like to continue? (y/n/s) \n")
        if CONTINUE.lower() == "y":
            AddMode()
        elif CONTINUE.lower() == "n":
            exit()
        elif CONTINUE.lower() == "s":
            StudyMode()
    else:
        print("Invalid Input")
        exit()
            
PREVIOUS_QUESTIONS = []
COUNT = 0
RIGHT_CNT = 0
WRONG_CNT = 0
TRACK_QUESTIONS = 0

def EvalChoices():
    global RIGHT_CNT
    global WRONG_CNT
    TOTAL = RIGHT_CNT+WRONG_CNT
    if TOTAL != 0:
        RATIO = RIGHT_CNT/TOTAL
        print("You Finished! - Right: " + str(RIGHT_CNT) + ", Wrong: " + str(WRONG_CNT) + ", Total Questions: " + str(TOTAL))
        print("Final Score: " + str(round(RATIO, 2)*100) + "%")
    elif TOTAL == 0:
        print("No questions were answered.")

def StudyMode():
    global COUNT
    global TRACK_QUESTIONS
    global FILENAME
    with open(FILENAME, "r") as f:
        QA = json.load(f)

    for x in QA['problems']:
        # Pick a random problem
        RAND = random.choice(list(QA['problems']))
        
        #print(PREVIOUS_QUESTIONS)
        if str(RAND).lower() not in PREVIOUS_QUESTIONS:
            print("PROBLEMS LEFT = " + str(len(QA['problems'])-TRACK_QUESTIONS) + "\n")
            #print("CURRENT_QUESTION= " + str(RAND) + " PREVIOUS_QUESTION= " + PREVIOUS_QUESTIONS + "\n")
            print("Question: " + RAND['question'])
                
            ITTR_VALUE = 0
            # Display all answers
            for text in RAND['answers']:
                ITTR_VALUE+=1
                print("(" + str(ITTR_VALUE) + ") '" + text + "'")
                
            def CheckInput():
                global RIGHT_CNT
                global WRONG_CNT
                global TRACK_QUESTIONS
                RESULT = input("Answer (q=quit): ")
                # Check if RESULT is the correct answer
                if (RESULT.isdigit() and int(RESULT) <= ITTR_VALUE and int(RESULT) > 0):
                  
                    #print("RESULT = " + RESULT)
                    #print("CORRECT_ANSWER = " + str(RAND['correct_answer']))

                    if (int(RESULT) == int(RAND['correct_answer'])):
                        RIGHT_CNT+=1
                        print("You got it RIGHT! \n")
                    elif (int(RESULT) != int(RAND['correct_answer'])):
                        WRONG_CNT+=1
                        print("You got it WRONG. The answer was: '" + str(RAND['correct_answer']) + "'\n")
                    TRACK_QUESTIONS+=1 #ADD TO TRACK QUESTIONS
                elif (RESULT.lower() == "q"):
                    EvalChoices()
                    exit()
                else:
                    print("Invalid Input. \n")
                    CheckInput()
            CheckInput()
                    
        elif str(RAND).lower() in PREVIOUS_QUESTIONS:
            #print("SAME QUESTION")
            #print(len(QA['problems']))
            if COUNT >= len(QA['problems'])*5: #THIS MULTIPLE IS IMPORTANT
                EvalChoices()
                exit()
            COUNT+=1
            StudyMode()
        PREVIOUS_QUESTIONS.append(str(RAND).lower())

def Write_JSON(new_data, filename=FILENAME):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.s
        file_data = json.load(file)
        # Join new_data with file_data
        file_data["problems"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
        
Main()