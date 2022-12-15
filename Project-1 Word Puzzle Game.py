import random

def shuffleword(wrd):
    pw=random.sample(wrd,k=len(wrd))
    return''.join(pw)

def printpuzzlequestion(word, score):
    problemword=shuffleword(word)
    print("\n Arrange letters to form valid word:")
    print(problemword)
    userword=input()
    print()
    if userword.upper()==word:
        print("Correct")
        score+=1
    else:
        print("Wrong")
        score-=1
    return score

def main():
    score=0
    words=["PROBLEM","BREAK","STUDENT",'KNOWLEDGE',"PUZZLE"]
    words=random.sample(words,k=len(words))
    
    for word in words:
        score = printpuzzlequestion (word,score)
    
    print("Your Score is ", score)
    print()

main()