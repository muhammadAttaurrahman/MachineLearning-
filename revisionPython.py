
import  math
import  time
class     allMathOpt():

            def __init__(self,choice):
                self.choice = choice ;
                pass

            def  resultOfGivenInput (self ,num1 , num2):
                if (choice==1):
                    print("Choice is :Addition " )
                    sum = num1 + num2 ;
                    print("Sum is : ", sum)
                    print("The power of sum is : ",pow(sum,2))
                if (choice==2):
                    print("Choice is :Subtraction " )
                    res = num1 - num2
                    print("Result is :",res)
                if (choice==3):
                    print("Choice is :Multification " )
                    res = num1 * num2
                    print("Result is :",res)
                if (choice==4):
                    print("Choice is :Division" )
                    try:
                            res = num1 / num2
                            print("Result is :",res)
                    except:
                        print ("You cant devide a number by '0'")


                        # class is closed 


print ("\n Do You want to continue : type (y)Yes , (n)No")
choice = input()

if (choice =='n' or choice =='N'):
    print("\t \t Application closed :) ")
    

while(choice == 'Y' or choice =='y' ):
    print ("\n 1)Addition \t 2)Subtraction \t 3)Multification \t 4) Division \t 0)Exit \n Chose your choice :")
    choice = int (input())

    if (choice== 0):
        time.sleep(2)
        print("\t\t Thank you for using our programe \n \t\t Application is exiting")
        
        break;

    elif( choice >=5):
        print("Invalid choice ")
        print ("\n Do You want to continue : type (y)Yes , (n)No")
        choice = input()

    else:
        num1 = int(input("Enter Num1 : "))
        num2 = int (input ("Enter Num2 :"))
        sub = allMathOpt (choice)
        sub.resultOfGivenInput(num1,num2)
        time.sleep(3)
        print("Thank you for using our programe")
        time.sleep(3)
        print ("\n Do You want to continue : type (y)Yes , (n)No")
        choice = input()
        if (choice =='n' or choice =='N'):
            print("\t \t Application closed :) ")
    
