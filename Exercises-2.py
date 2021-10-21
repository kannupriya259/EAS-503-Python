#!/usr/bin/env python
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[118]:


NAME = "KANNU PRIYA"
COLLABORATORS = ""


# ---

# In[119]:


# Exercise 1
def is_palindrome(input_string):
    # Complete this function to determine if the input_string is a palindrome. Return True or False
    # Use square brackets to reverse the input_string! Make sure to lower the input string before testing!
    
    # YOUR CODE HERE
    input_string = input_string.lower()
    if input_string == input_string[::-1]:
        return True
    else:
        return False
    raise NotImplementedError()


# In[120]:


# Test cell  for exercise 1
assert is_palindrome("Kayak") == True
assert is_palindrome("Rotator") == True
assert is_palindrome("AACA") == False


# In[121]:


# Test cell  for exercise 1 (hidden)


# In[122]:


# Exercise 2: Season from Month and Day
def determine_season(month, day):

    # The year is divided into four season: spring, summer, fall (or autumn) and winter.
    # While the exact dates that the seasons change vary a little bit from year to
    # year because of the way that the calender is constructed, we will use the following
    # dates for this exercise:

    # Season  -- First Day
    # Spring  -- March 20
    # Summer  -- June 21
    # Fall  -- September 22
    # Winter    -- December 21

    # Complete this function which takes in as inputs a month and day. It should
    # output the season.
    # input 1: month -- str
    # input 2: day -- int

    # output: month -- str (Spring, Summer, Fall, Winter)

    # YOUR CODE HERE
    #asking user name of the month 
    d = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September":9 , "October": 10, "November": 11, "December": 12}
    # using if-else conditions, return the corresponding season name
    if (d[month] == 3 and day >= 20) or 4 <= d[month] <= 5 or (d[month] == 6 and day < 21):
        return 'Spring'
    if (d[month] == 6 and day >= 21) or 7 <= d[month] <= 8 or (d[month] == 9 and day < 22):
        return 'Summer'
    if (d[month] == 9 and day >= 22) or 10 <= d[month] <= 11 or (d[month] == 12 and day < 21):
        return 'Fall'
    else:
        return 'Winter'


# In[123]:


# Test cell  for exercise 2
assert determine_season('March', 21) == 'Spring'
assert determine_season('June', 21) == 'Summer'
assert determine_season('November', 21) == 'Fall'
assert determine_season('January', 21) == 'Winter'


# In[124]:


# Test cell  for exercise 2 (hidden)


# In[125]:


#Exercise 3: Check a password

def check_password(password):

    # In this exercise you will complete this function to determine whether or not
    # a password is good. We will define a good password to be a one that is at least
    # 8 characters long and contains at least one uppercase letter, at least one lowercase
    # letter, and at least one number. This function should return True if the password
    # passed to it as its only parameter is good. Otherwise it should return False. 
    #
    # input: password (str)
    # output: True or False (bool)


    # YOUR CODE HERE
    password=list(password)
    upper,low,digit=0,0,0
    for item in password:
        if item >='A' and item <='Z':
            upper=upper+1
        if item >='a' and item <='z':
            low=low+1
        if item >='0' and item <= '9':
            digit=digit+1
    if len(password)>=8 and upper>=1 and low>=1 and digit >=1:
        flag=True
    else:
        flag=False
    
    return flag




# In[126]:


# Test cell  for exercise 3
assert check_password('test1234') == False
assert check_password('password123') == False
assert check_password('SuperPasswrd90') == True
assert check_password('letmein!') == False


# In[127]:


# Test cell  for exercise 3


# In[128]:


# Exercise 4
def average_word_len_in_sentence(sentence):
    # Complete this function to calculate the average
    # word length in a sentence
    # Input: sentence
    # Output: average word length in sentence
    # Hint: count punctuations with whatever word they are `touching`
    # Hint: round the average to two decimal places
   
    # YOUR CODE HERE
    avg_word_length=0
    length=0
    for word in sentence.split():
        length+=len(word)
    avg_word_length=length/len(sentence.split())
    return round(avg_word_length,2)

    


# In[129]:


# Text cell for Exercise 4 
assert average_word_len_in_sentence('This is a test sentence!') == 4


# In[130]:


# Text cell for Exercise 4(hidden)


# In[131]:


#Exercise 5
def wc(filename):
    # Complete this function to count the number of lines, words, and chars in a file. 
    # Input: filename
    # Output: a tuple with line count, word count, and char count -- in this order

    # YOUR CODE HERE
    lines,words,chars=0,0,0
    with open(filename,"r")as file:
        for line in file:
            lines+=1
            words+=len(line.split())
            chars+=len(line)
    return(lines,words,chars)


# In[132]:


# Text cell for Exercise 5 
assert wc('ex5_data.txt') == (50, 643, 4298)


# In[133]:


# Exercise 6 
def is_leap(year):
    # Complete this function to check if year is a leap year
    # Input: year
    # Output: True or False (Boolean)

    # YOUR CODE HERE
    
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));
 
# Driver Code
    year = 2000
    if(checkYear(year)):
        return True
    else:
        return False
     


# In[134]:


# Text cell for Exercise 6
assert is_leap(1800) == False
assert is_leap(1900) == False
assert is_leap(1600) == True
assert is_leap(2000) == True


# In[135]:


# Exercise 7
def is_date_valid(month, day, year):
    # Complete this function to check if a data is valid, given month, day, and year.  
    # For example, 5/24/1962 is valid, but 9/31/2000 is not
    # Inputs: month, day, year
    # Output: True or False (Boolean)
    # Hint: Use is_leap() year function from previous exercise

    # YOUR CODE HERE
    if(month < 1 or month > 12):
        return False
    if(day < 1 or day > 31):
        return False
    #if month is feb
    if(month == 2):
        #if leap year, 29 day is valid
        if is_leap(year) == True:
            if(day <= 29):
                return True
        # if not leap more that 28 invalid
        elif(day > 28):
            return False
       
    # if month has 30 day
    if(month == 4 or month == 6 or month == 9 or month == 11):
        if(day <= 30):
            return True
        else:
            return False
    #if reach here means date is valid
    #return true
    return True
    raise NotImplementedError()


# In[136]:


# Text cell for Exercise 7
assert is_date_valid(5, 24, 1962) == True
assert is_date_valid(9, 31, 2000) == False


# In[137]:


# Text cell for Exercise 7 (hidden)


# In[138]:


# Exercise 8
def day_number(month, day, year):
    # Complete this function to calculate the day_number given month, day, and year.
    # Information: The days of the year are often numbered from 1 through 365 (or 366).
    # This number can be computed in three steps using int arithmetic:
    # (a) - day_num = 31 * (month - 1) + day
    # (b) - if the month is after February subtract (4*(month)+23)//10
    # (c) - if it's a leap year and after February 29, add 1
    # Hint: First verify the input date is valid, return False if it is not valid; use is_date_valid
    # Hint: Also use the is_leap function
    # Inputs: month, day, year
    # Output: the day number or False (boolean) if the date is invalid. 

    # YOUR CODE HERE
    check_year=is_leap(year)
    check_date=is_date_valid(month,day,year)
    if not check_date:
        day_num=False
    elif check_date and not check_year:
        day_num=(31*(month-1)+day)
    elif check_date and check_year and month==2:
        day_num=(31*(month-1)+day)
    elif check_date and check_year and month>2 and month<=12:
        day_num=((31*(month-1)+day)-((4*(month)+23)//10))+1
    return day_num 


# In[139]:


# Text cell for Exercise 8
assert day_number(9, 31, 2000) == False
assert day_number(2, 13, 2020) == 44


# In[140]:


# Text cell for Exercise 8 (hidden)


# In[141]:


# Exercise 9
def years_to_double_investment(apr):
    # Complete this function to use a while loop to determine how long it takes for an investment 
    # to double at a given interest rate. The input to this function, apr, is the annualized interest rate
    # and the output is the number of years it takes an investment to double. Note: The amount of the initial 
    # investment (principal) does not matter; you can use $1. 
    # Hint: principal is the amount of money being invested. 
    # apr is the annual percentage rate expressed as a decimal number.  
    # Relationship: value after one year is given by principal * (1+ apr)
    
    # YOUR CODE HERE
    #initial principal
    principal = 1
    # year count = 0
    year = 0
    
    #while principal is less than double of principal
    while(principal < 2):
        # calculate principal after year
        principal = principal * (1 + apr)
        #increase year by 1
        year = year + 1
    #return
    return year

    raise NotImplementedError()


# In[142]:


# Text cell for Exercise 9
assert years_to_double_investment(0.06) == 12
assert years_to_double_investment(0.1) == 8


# In[143]:


# Exercise 10
def stopping_time(n):
    # Complete this function to return the number of steps taken to reach 1 in
    # the Collatz sequence (https://en.wikipedia.org/wiki/Collatz_conjecture)

    # YOUR CODE HERE
    cnt=0
    while n>1:
        if n%2==0:
            n=n//2
            cnt+=1
        else:
            n=(3*n)+1
            cnt+=1
    return cnt


# In[144]:


# Text cell for Exercise 10
assert stopping_time(12) == 9
assert stopping_time(27) == 111


# In[145]:


# Text cell for Exercise 10 (hidden)


# In[146]:


# Exercise 11
def is_prime(n):
    # A positive whole number > 2 is prime if no number between 2 and sqrt(n)
    # (include) evenly divides n. Write a program that accepts a value of n as
    # input and determine if the value is prime. If n is not prime, your program should
    # return False (boolean) as soon as it finds a value that evenly divides n.
    # Hint: if number is 2, return False

    import math
     # If n = 2 then returning False
    if n == 2:
        return False
  # If n > 2 then checking if any number between n and sqrt(n) evenly divides n.
  # This approach has very less time complexity as compared to other approaches
  # to check prime 
    elif n > 2:
    # Looping from 2 to sqrt(n)
    # Here, added int(math.sqrt(n)) + 1 because sqrt(n) should be inclusive
    # but in for loop its exclusive, so added 1 to make sqrt(n) as inclusive
      for i in range(2, int(math.sqrt(n)) + 1):
      # If any number between 2 and sqrt(n) evenly divides n returning False
        if n % i == 0:
            return False
    # If no number between 2 and sqrt(n) evenly divides n returning True
      return True
    
    # YOUR CODE HERE
    raise NotImplementedError()


# In[147]:


assert is_prime(2) == False
assert is_prime(3) == True
assert is_prime(5) == True
assert is_prime(25) == False


# In[148]:


# Exercise 12
def all_primes(n):
    # Complete this function to return all the primes as a list less than or equal to n
    # Input: n
    # Output: a list of numbers

    # YOUR CODE HERE
    prime=[]
    for i in range(2,n+1):
        if is_prime(i):
            prime.append(i)
    return prime


# In[149]:


assert all_primes(5) == [3, 5]
assert all_primes(25) == [3, 5, 7, 11, 13, 17, 19, 23]


# In[150]:


# Exercise 13
def gcd(m,n):
    # Complete this function to determine the greatest common divisor (GCD). 
    # The GCD of two values can be computed using Euclid's algorithm. Starting with the values
    # m and n, we repeatedly apply the formula: n, m = m, n%m until m is 0. At this point, n is the GCD
    # of the original m and n. 
    # Inputs: m and n which are both natural numbers
    # Output: gcd

    # YOUR CODE HERE
    #repeatedly apply the given formula n,m = m,n%m until m is 0 and return the value of n when this condition fails.
    while m != 0:
        n,m = m, n%m
    return n

    def main():
   #prints the followin line
     print("Euclid's GCD algorithm\n")
   #take two inputs separated by a comma, split them and assign the inputs to variables
    m, n = input("Enter two natural numbers (n1, n2): ").split(",")
   #call the gcd function with the inputs as parameters converted into int type and print the result
    print("The GCD of", m, "and", n, "is", gcd(int(m), int(n)))
  
    


# In[151]:


# Exercise 13 test cell
assert gcd(25,75) == 25
assert gcd(3,13) == 1


# In[152]:


# Exercise 13 test cell (hidden)


# In[153]:


# Exercise 14 
def determine_min_max_average(filename):
    # Complete this function to read grades from a file and determine the student with the highest average 
    # test grades and the lowest average test grades. 
    # Input: filename
    # Output: a tuple containing four elements: name of student with highest average, their average, 
    # name of the student with the lowest test grade, and their average. Example ('Student1', 99.50, 'Student5', 65.50)
    # Hint: Round to two decimal places

    # YOUR CODE HERE
    marks=[]
    with open(filename,'r')as file:
        lines=file.readlines()
        for line in lines:
            if len(line)>1:
                marks.append(line.strip().split(","))
    final={}
    i=0
    for line in marks:
        total=len(line)-1
        avg=sum(list(map(int,line[1:])))/total
        final[line[0]]=avg
    max_key=max(final,key=final.get)
    min_key=min(final,key=final.get)
    max_val=round(final[max_key],2)
    min_val=round(final[min_key],2)
    return(max_key,max_val,min_key,min_val)
            
    
    


# In[154]:


# Exercise 14 test cell
assert determine_min_max_average('ex14_data.txt') == ('student733', 86.2, 'student202', 65.4)


# In[155]:


# Ex15:Is a License Plate Valid?

def is_license_plate_valid(plate):

    # In a particular jurisdiction, older license plates consist of three uppercase
    # letters followed by three digits. When all of the license plates following
    # that pattern had been used, the format was changed to four digits followed by
    # three uppercase letters. 

    # Complete this function whose only input is a license plate and its output
    # is: 1) Older/Valid 2) Newer/Valid 3) Invalid
    # input: plate (str)
    # output: 'Older/Valid' or 'Newer/Valid' or 'Invalid'

    # YOUR CODE HERE
    import re
    regex1=("^([A-Z]{3}[0-9]{3}$)")
    regex2=("^([0-9]{4}[A-Z]{3}$)")
    p = re.compile(regex1)
    q = re.compile(regex2)

    if(plate==None):
        return "Invalid"
        
    if(re.search(p, plate)):
        return "Older/Valid"
    elif(re.search(q, plate)):
        return "Newer/Valid"
    else:
        return "Invalid"
    raise NotImplementedError()


# In[156]:


# Exercise 15 test cell
assert is_license_plate_valid('ABC123') == 'Older/Valid'
assert is_license_plate_valid('GHE952') == 'Older/Valid'
assert is_license_plate_valid('1934ABT') == 'Newer/Valid'
assert is_license_plate_valid('bTR342') == 'Invalid'


# In[157]:


# Exercise 15 test cell (hidden)


# In[158]:


# Ex16: Magic dates

def is_magic_date(date):
    # A magic date is a date where the day multiplied by the month is equal 
    # to the two digit year. For example, June 10, 1960 is a magic date because
    # June is the sixth month, and 6 times 10 is 60, which is equal to the two
    # digit year. Complete this function to determine whether or not a date is
    # a magic date.

    # input: date (str -- month/day/year)
    # output: True or False (bool)


    # YOUR CODE HERE
    month, day, year = date.split('/')
    last_two_digit_of_year = int(year)%100
    if(int(month)*int(day) == last_two_digit_of_year):
        return True
    return False
    
    raise NotImplementedError()


# In[159]:


# Exercise 16 test cell
assert is_magic_date('6/10/1960') == True
assert is_magic_date('6/8/1948') == True


# In[160]:


# Ex17
def remove_outliers(data, num_outliers):
    # When analyzing data collected as a part of a science experiment it 
    # may be desriable to remove the most extreme values before performing
    # other calculations. Complete this function which takes a list of
    # values and an non-negative integer, num_outliers, as its parameters.
    # The function should create a new copy of the list with the num_outliers 
    # largest elements and the num_outliers smallest elements removed. 
    # Then it should return teh new copy of the list as the function's only 
    # result. The order of the elements in the returned list does not have to
    # match the order of the lemetns in the original list.
    # input1: data (list)
    # input2: num_outliers (int)

    # output: list
    


    # YOUR CODE HERE
    input_data=sorted(data)
    del input_data[0:num_outliers]
    end_ele=(len(input_data)-num_outliers)
    del input_data[end_ele:]
    return input_data


# In[161]:


# Exercise 17 test cell
import random
random.seed(1234)
data = [random.randint(50, 150) for ele in range(100)]
data[45] = 1
data[46] = 2
data[90] = 250
data[34] = 300

result = [50, 50, 51, 52, 52, 52, 53, 53, 54, 
55, 55, 55, 55, 56, 58, 58, 59, 59, 59, 60, 61, 61, 
61, 62, 64, 64, 64, 68, 68, 68, 69, 69, 69, 70, 71, 
72, 73, 75, 77, 80, 81, 81, 84, 84, 84, 85, 88, 88, 89, 
92, 94, 94, 95, 95, 98, 103, 106, 108, 108, 109, 109, 109, 
110, 111, 111, 112, 113, 114, 115, 115, 117, 117, 119, 121, 
124, 124, 125, 126, 128, 129, 132, 132, 133, 134, 135, 135, 
135, 136, 138, 140, 141, 148, 148, 149, 149, 150]

assert remove_outliers(data, 2) == result


# In[162]:


# Exercise 17 test cell (hidden)


# In[163]:


# Ex18: Removing duplicates

def remove_duplicates(words):
    # Complete this function to remove duplicates from the words list using a loop
    # input: words (list)
    # output: a list without duplicates
    # MUST USE loop and NOT set!

    # YOUR CODE HERE
    list_without_duplicates = []
    for element in words:
        if element not in list_without_duplicates:
            list_without_duplicates.append(element)

    return list_without_duplicates

    raise NotImplementedError()


# In[164]:


# Exercise 18 test cell
assert remove_duplicates([1,2,3,3,3,4,5,6,7,7,8]) == [1, 2, 3, 4, 5, 6, 7, 8]


# In[165]:


# Exercise 18 test cell (hidden)


# In[166]:


# Ex19: List of proper divisors

def proper_divisors(n):
    # A proper divisor ofa  positive integer, n, is a positive integer less than n which divides
    # evenly into n. Complete this function to compute all the proper divisors of a positive
    # integer. The integer is passed to this function as the only parameter. The function will
    # return a list of containing all of the proper divisors as its only reult. 

    # input: n (int)
    # output: list

    # YOUR CODE HERE
    range_of_pos = range(1,n)
    prop_div = []
    for i in range_of_pos:
        if n % i == 0:
            prop_div.append(i)
            
    return prop_div
    raise NotImplementedError()


# In[167]:


# Exercise 19 test cell
assert proper_divisors(28) == [1, 2, 4, 7, 14]


# In[168]:


# Exercise 19 test cell (hidden)


# In[169]:


#Ex20: Perfect Numbers
def is_number_perfect(n):
    # An integer, n, is said to be perfect when the sum of all of the proper divisors 
    # of n is equal to n. For example, 28 is a perfect number because its proper divisors
    # are 1, 2, 4, 7, and 14 = 28 
    # Complete this function to determine if a the number a perfect number or not. 
    # input: n (int)
    # output: True or False (bool)
    res=sum(proper_divisors(n))
    if res==n:
        output=True
    else:
        output=False
        
    return output

    # YOUR CODE HERE
    


# In[170]:


# Exercise 20 test cell
assert is_number_perfect(28) == True
assert is_number_perfect(76) == False


# In[171]:


# Exercise 20 test cell (hidden)


# In[172]:


# Ex21: Line of Best Fit
def best_line(points):
    # Complete this function to determine the best line. 
    # https://www.varsitytutors.com/hotmath/hotmath_help/topics/line-of-best-fit
    # input: points (list of tuples contain x, y values)
    # output: (m, b) # round both values to two decimal places

    # YOUR CODE HERE
    x = []
    y = []
    for i in points:
        
        x.append(i[0])
        y.append(i[1])
    
    avg_x = sum(x)/len(x)
    avg_y = sum(y)/len(y)

    x_minus_xbar = []
    for i in x:
        x_minus_xbar.append(i-avg_x) 

    y_minus_ybar = []
    for i in y:
        y_minus_ybar.append(i-avg_y)    

    product_of_norm_xy = []
    for i,j in zip(x_minus_xbar,y_minus_ybar):
        product_of_norm_xy.append(i*j)    

    x_minus_x_avg_sq = []

    for i in x:
        x_minus_x_avg_sq.append(i-avg_x)

    x_minus_x_avg_sq = [i**2 for i in x_minus_x_avg_sq]


    slope = sum(product_of_norm_xy)/sum(x_minus_x_avg_sq)

    y_intercept = avg_y - (slope*avg_x)

    return (round(slope,2),round(y_intercept,2))
    raise NotImplementedError()


# In[173]:


# Exercise 21 test cell
points = (
    (8, 3),
    (2, 10),
    (11, 3),
    (6, 6),
    (5, 8),
    (4, 12),
    (12, 1),
    (9, 4),
    (6, 9),
    (1, 14),
)

assert best_line(points) == (-1.11, 14.08)


# In[174]:


# Exercise 21 test cell (hidden)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




