'''
    @author : Thomas, thomas.wangsa@gmail.com
    Des     : technical test part 1
'''

# change the variable to check the quality of this application
value = 8

# main function for this exercise, return void
def fivaa(value) :
    print("Process is start") # flag start
    check = validation(value) # validation function
    # use while since python didn't support for(i)
    while(check) :
        fivaa_response(value) # fivaa_response function
        value -= 1
        if(value == 0) :
            break
    print("Process is done") # flag done

# print the result as expectation, return void
def fivaa_response(value) :
    new_value = value+2
    i = 0 # incremental variable
    result = ""
    while(new_value > i) :
        i = i+1
        if(i == 1 or i == 2) :
            result += str(value-1)
        else :
            result += str(value+1)
        if(i >= new_value) :
            print(result)

# validation function, return boolean
def validation(value) :
    check_type = isinstance(value, int) # return boolean
    if (check_type):
        if (value <= 0): # check the value whether positive or negative
            print("Sorry, input must be a positive integer, try again")
        else :
            return True
    else :
        print("That's not an int!")

# Here is the function
fivaa(value)