'''
Recieve input from user
Convert the input to integer
Use mod operator to check if the remainder is 0
'''

# number=int(input("Type in number here "))
# print(number % 2)
# number2=number%2
# if number2==0:
#     print("this number is even")
# else:
#     print("this number is odd")
# def function():
#     print("DHJDWFILKFE")
#
# function()
# listt=[12,14,12,12,12]
# summ=0
#
# for i in listt:
#     summ += i
#
# avg=summ
#
#
# avg /= len(listt)
#
# print(str(avg)+" is the avg of the list.")
# # print(str(summ)+" is the sum of the list. ")
# '''///////////////////////////////New Task////////////////////////////////////'''
# from modukes import Adddd
# var = 3476783910327683928756481943793874382364738746547382376456378273
#
#
# print(Adddd(var,647384754839473829376573829374654378297364278746738297364738217365721897363728374567))
#
# 1real_answer="sky blue"
# questionNumber=0
#
# def question_maker(question,options,questionNum):
#     print("Question number "+str(questionNum))
#     print("\n")
#     print(question)
#     print(options)
#
#     return input("What is the answer")
#
#
# question_maker("What is the color of an integer?","OPTIONS: black,black,orange,tomato,sky blue,tomaoto",1)
# questionNumber+=1
# answer=question_maker()
# if questionNumber == 1 :
#     if answer == "sky blue":
#         print("correct")
#     else:
#         print("incorrect, go away")
#
# print(answer)

def myQuiz():
    score = 0
    questions = [
        {
            "question": "What is the capital of the united states?",
            "options": ["london", "New york", "washington DC", "canada"],
            "answer": "washington DC"
        }, {
            "question": "What is the color of a carrot?",
            "options": ["purple", "red", "orange", "blue"],
            "answer": "blue"
        },
        {
            "question": "is cat a mammal?",
            "options": ["No", "yes"],
            "answer": "yes"
        },
        {
            "question": "WWhat is the circumference of a circle if the diameter is 3?",
            "options": ["6", "12", "9.42", "90"],
            "answer": "9.42"
        }
    ]
    for qst in questions:
        print(qst["question"])
        for i in  range(len(qst["options"])):
            print(str(i+1)+" "+qst["options"][i])
        user_input = input("choose an answer: ")


        if user_input.lower() == qst["answer"].lower():
            print("you got it right\n")
            score += 1
        else:
            print("Incorrect answer\n")
    print("your total score is "+str(score))

myQuiz()









































































































































































































