def main():
    #create a method to compute the average of two numbers
    average = 0
    #get input 1
    inputx = int (input("Input X:"))
    #get input 2
    inputy = int (input("Input Y:"))
    #get the average of the two numbers
    average = (inputx + inputy)/2
    print("The average of X and Y is", average)

if __name__=="__main__":
    #run the main method to print out the text
    main()