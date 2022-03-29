from tokenize import String


class Q3 :
    
    #
    def q2b() :
        # i=i-1 is i-- and i=i+1 is i++
        i = 102
        while (i >= 66) :
            print("In descending order: " + str(i))
            i -= 1
    
    def q2c( ) :

        
        modcode = input("Enter the module code : ")
     
        if modcode=="CSC1010":
         print("Computer Networks") 
        elif modcode=="CSC1006": 
         print("Mathematics 2")
        elif modcode=="CSC1009":
         print("Object-Oriented Programming")
        else:
         print("Unknown Module")
        print("Program Terminated Successfully")
    

if __name__=="__main__":
    print("\nThis is Question 2b in python")
    Q3.q2b()
    print("\nThis is Question 2c in python")
    Q3.q2c()