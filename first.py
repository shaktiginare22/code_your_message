questions=[["1. Which keyword is used for function in Python language? ","Function","def","Fun","Define",2],
["2. Which of the following character is used to give single-line comments in Python?","//","#","!","/*",2],
["3.Which of the following functions is a built-in function in python?","factorial()","print()","seed()","sqrt()",2],
["4.Which of the following statements is used to create an empty set in Python?","( )","[ ]","{ }","set()",4],
["5.Which of the following is a Python tuple?","{1, 2, 3}",str("{}"),"[1, 2, 3]","(1, 2, 3)",4]]

level=[10000,50000,100000,500000,5000000]

money=0
for i in range (0 ,len(questions)):
    question=questions[i]
    print(f"\nA question for RS. {level[i]}")
    print(f"\n{question[0]}")
    print(f"\n1.{question[1]}                2.{question[2]} ")
    print(f"3.{question[3]}                  4.{question[4]} ")
    reply=int(input("enter your answer (1-4) or press 0 to quit = "))


    if (reply==question[-1]):
        print(f"\nwright answer you won {level[i]}")
        if (i==2):
            money=100000

        
        if(reply==0):
            money=level[i-1]
            print("thanks for playing quiz")
            break
    
        elif(i==4):
            money=5000000
    else:
        print("\nyou choose wrong answer !")
        break


print("**************************************")
print(f"\nyout total wining amount RS. {money}")



