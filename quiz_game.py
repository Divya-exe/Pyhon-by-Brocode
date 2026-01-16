questions=  ("what is fairness metrics used for? ",
            "which of the following is debising technique",
            "Data privacy in AI refers to :",
            "Which regulation focus on data protection and privacy",
            "Transparency in AI means:")
options=(("A.Model accuracy","B.Energy efficiency","C.ABC ","D.ACD"),
        ("A.Model accuracy ","B.Energy efficiency","C.aBC ","D.ACD"),
        ("A.Model accuracy ","B.Energy efficiency","C.bC ","D.ACD"),
        ("A.Model accuracy ","B.Energy efficiency","C.AC ","D.ACD"),
        ("A.Model accuracy ","B.Energy efficiency","C.ABc ","D.ACD"))
answers=("C","A","D","B","C")
guesses= []
score= 0
question_num=0

for question in questions:
    print("-----------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess=input("enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    
print("-----------------------------------")
print("              RESULTS              ")
print("-----------------------------------")
    
print("answers:",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("Guesses:",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score =  int(score / len(questions) * 100)
print(f"your score is :{score} %")
        
    