while True:
        a=int(input('Enter the 1st Number: '))
        b=int(input('Enter the 2nd Number: '))
        print('What would you like to do ?...\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.quit')
        choice=int(input('Enter your choice number: '))
        if choice==1:
            print('Answer is:' ,a+b)
        elif choice==2:
            print('Answer is:' ,a-b)
        elif choice==3:
            print('Answer is:' ,a*b)
        elif choice==4:
            print('Answer is:' ,a/b)
        elif choice==5:
            print('Thank you...')
            break
        else:
            print('INVALID CHOICE :Please enter a valid choice.')


    
        
