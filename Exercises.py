#!/usr/bin/env python
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[1]:


NAME = "Kannu Priya"
COLLABORATORS = ""


# ---

# In[1]:


def count_number_of_characters_in_string(input_string):
    """
    This function takes in one input string. Complete this function to PRINT
    the input string and the number of characters in the input string.
    Sample Input: Amherst
    Expected Print Statement: The input string ‘Amherst’ has 7 characters. 
    - Use f-string
    """
 
    # YOUR CODE HERE
    a=len(input_string)
    print(f"The input string '{input_string}' has {a} characters.")
    


# In[2]:


from unittest.mock import patch
with patch('__main__.print') as mock_print:
    count_number_of_characters_in_string('Buffalo')
mock_print.assert_called_once_with("The input string 'Buffalo' has 7 characters.")

with patch('__main__.print') as mock_print:
    count_number_of_characters_in_string('University at Buffalo')
mock_print.assert_called_once_with("The input string 'University at Buffalo' has 21 characters.")

with patch('__main__.print') as mock_print:
    count_number_of_characters_in_string('Center for Computational Research (CCR)')
mock_print.assert_called_once_with("The input string 'Center for Computational Research (CCR)' has 39 characters.")


# In[3]:


def mad_lib(noun, verb, adjective, adverb):
    """
    This function takes in four input strings. Complete this function to PRINT
    a sentence using the four input strings
    Input Strings: noun, verb, adjective, adverb
    Expected print Statement: Do you <verb> your <adjective> <noun> <adverb>? That's hilarious!
    - Use f-string
    """
    
    # YOUR CODE HERE
    print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")
    


# In[4]:


from unittest.mock import patch
with patch('__main__.print') as mock_print:
    mad_lib('dog', 'walk', 'blue', 'quickly')
mock_print.assert_called_once_with("Do you walk your blue dog quickly? That's hilarious!")

with patch('__main__.print') as mock_print:
    mad_lib('cat', 'walk', 'brown', 'slowly')
mock_print.assert_called_once_with("Do you walk your brown cat slowly? That's hilarious!")


# In[55]:


def retirement_calculator(current_age, age_at_retirement, current_year):
    """
    This function takes in three numbers as input arguments: current_age, age_at_retirement, and current_year. 
    Complete this function to PRINT the expected output. 
      
    If current_age = 36, age_at_retirement = 72, and current_year = 2021
    
    Expected output:
    Your current age is: 36.
    You would like to retire at: 72.
    You have 36 years left until you can retire.
    It's 2021, so you can retire in 2057.
    
    - Use f-string
    """
    
    # YOUR CODE HERE
    print(f"Your current age is: {current_age}.\n"+f"You would like to retire at: {age_at_retirement}.\n"+f"You have {age_at_retirement-current_age} years left until you can retire.\n"+f"It's {current_year}, so you can retire in {age_at_retirement-current_age+current_year}.")
    


# In[56]:


from unittest.mock import patch
with patch('__main__.print') as mock_print:
    retirement_calculator(25, 65, 2015)
mock_print.assert_called_once_with("""Your current age is: 25.
You would like to retire at: 65.
You have 40 years left until you can retire.
It's 2015, so you can retire in 2055.""")

with patch('__main__.print') as mock_print:
    retirement_calculator(36, 72, 2021)
mock_print.assert_called_once_with("""Your current age is: 36.
You would like to retire at: 72.
You have 36 years left until you can retire.
It's 2021, so you can retire in 2057.""")


# In[54]:


def area_of_a_rectangular_room(length, width):
    """
    This function takes in the length and width in feet. 
    Complete this function to PRINT the expected output. 
    Use formula -- m^2 = f^2 * 0.09290304 to convert feet^2 to meter^2
    
    If length = 15 and width = 20
    
    Expected output:
    
    The length of the room in feet is 15.
    The width of the room in feet is 20.
    The dimension of the room is 15 by 20 feet.
    The area is
    300 square feet
    27.87 square meters

    - Use f-string
    """
    
    # YOUR CODE HERE
    area_in_square_feet = length * width
    area_in_square_meter = area_in_square_feet * 0.09290304

    # printing using f string
    print(f'The length of the room in feet is {length}.\nThe width of the room in feet is {width}.\nThe dimension of '
          f'the room is {length} by {width} feet.\nThe area is\n{area_in_square_feet} square feet'
          f'\n{area_in_square_meter:.2f} square meters') 
    


# In[10]:


from unittest.mock import patch
with patch('__main__.print') as mock_print:
    area_of_a_rectangular_room(15, 20)
mock_print.assert_called_once_with("""The length of the room in feet is 15.
The width of the room in feet is 20.
The dimension of the room is 15 by 20 feet.
The area is
300 square feet
27.87 square meters""")

with patch('__main__.print') as mock_print:
    area_of_a_rectangular_room(45, 35)
mock_print.assert_called_once_with("""The length of the room in feet is 45.
The width of the room in feet is 35.
The dimension of the room is 45 by 35 feet.
The area is
1575 square feet
146.32 square meters""")


# In[11]:


def pizza_party(number_of_people, number_of_pizzas):
    """
    This function takes in the number of people and the number of pizzas. Assume each pizza has 8 slices. 
    
    Complete this function to PRINT the expected output. 

    If number_of_people = 8 and number_of_pizzas = 2
    
    Expected output:
    
    There are 8 with 2 pizzas.
    Each person gets 2 pieces of pizza.
    There are 0 leftover pieces.

    - Use f-string
    """
    
    
    # YOUR CODE HERE
    total_pieces = number_of_pizzas * 8
    each_person_pizzas = total_pieces // number_of_people
    left = total_pieces - (number_of_people * each_person_pizzas)

    # printing
    print(f'There are {number_of_people} with {number_of_pizzas} pizzas.\nEach person gets {each_person_pizzas}'
          f' pieces of pizza.\nThere are {left} leftover pieces.')
    


# In[12]:


from unittest.mock import patch
with patch('__main__.print') as mock_print:
    pizza_party(8, 2)
mock_print.assert_called_once_with("""There are 8 with 2 pizzas.
Each person gets 2 pieces of pizza.
There are 0 leftover pieces.""")

with patch('__main__.print') as mock_print:
    pizza_party(20, 6)
mock_print.assert_called_once_with("""There are 20 with 6 pizzas.
Each person gets 2 pieces of pizza.
There are 8 leftover pieces.""")


# In[13]:


def paint_calculator(length, width):
    """
    This function takes in the length and width in feet of a ceiling. You need to calculate the number
    of gallons needed to paint the ceiling. Assuming one gallon can paint 350 square feet. 
    
    Complete this function to PRINT the expected output. 

    If length = 12 and width = 30
    
    Expected output:
    
    You will need to purchase 2 gallons of paint to cover 360 square feet.

    - Use f-string
    - HINT: You need to use the math.ceil function to round up
    """
    
    import math
    # YOUR CODE HERE
    area = length * width
    no_of_gallons = math.ceil(area / 350)

    print(f'You will need to purchase {no_of_gallons} gallons of paint to cover {area} square feet.')
    


# In[14]:


from unittest.mock import patch
with patch('__main__.print') as mock_print:
    paint_calculator(12, 30)
mock_print.assert_called_once_with('You will need to purchase 2 gallons of paint to cover 360 square feet.')

with patch('__main__.print') as mock_print:
    paint_calculator(25, 35)
mock_print.assert_called_once_with('You will need to purchase 3 gallons of paint to cover 875 square feet.')


# In[15]:


def f_string_exercise1(value):
    """
    You must use f-string formatting to get the output shown in the next cell. This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output.   
    """

    # YOUR CODE HERE
    print(f'The value is: {value:.4f}.')
        


# In[16]:


from unittest.mock import patch
with patch('__main__.print') as mock_print:
    value = 3.14159
    f_string_exercise1(value)
mock_print.assert_called_once_with('The value is: 3.1416.')


# In[17]:


# Hidden test for f_string_exercise1


# In[18]:


def f_string_exercise2(value):
    """
    You must use f-string formatting to get the output shown in the next cell. This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output.   
    """
    
    print(f'The value is: {value:10.4f}.')
    


# In[19]:


from unittest.mock import patch
with patch('__main__.print') as mock_print:
    value = 3.14159
    f_string_exercise2(value)
mock_print.assert_called_once_with('The value is:     3.1416.')


# In[20]:


# Hidden test for f_string_exercise2


# In[21]:


def f_string_exercise3(value):
    """
    You must use f-string formatting to get the output shown in the next cell. This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output.   
    """

    # YOUR CODE HERE
    print(f'The value of PI is: {value:.6f}...')
    return(value)

    raise NotImplementedError()


# In[22]:


from unittest.mock import patch
with patch('__main__.print') as mock_print:
    value = 3.14159
    f_string_exercise3(value)
mock_print.assert_called_once_with('The value of PI is: 3.141590...')


# In[23]:


# Hidden test for f_string_exercise3


# In[24]:


def f_string_exercise4(value):
    """
    You must use f-string formatting to get the output shown in the next cell. This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output.   
    """
    # YOUR CODE HERE
    
    print(f"The value is: --"+f'{value:.6f}'+f'--.')
  
    


# In[25]:


from unittest.mock import patch
with patch('__main__.print') as mock_print:
    value = 3.14159
    f_string_exercise4(value)
mock_print.assert_called_once_with('The value is: --3.141590--.')


# In[26]:


# Hidden test for f_string_exercise4


# In[27]:


def total_wages_for_the_week(hours, wage):
    # Many companies pay time-and-a-half for any hours worked above 40 in a given week.
    # Complete this function whose inputs are hours worked (hours) and the hourly rate (wage) to
    # calculate the total wages for the week. 
    # YOUR CODE HERE
        if hours <= 40:
            return hours * wage
        else:
            return (40 * wage) + (hours - 40) * wage * 1.5






   


# In[28]:


# Test cell for exercise 1
assert total_wages_for_the_week(40, 25) == 1000
assert total_wages_for_the_week(65, 63.4) == 4913.5


# In[29]:


# Hidden test cell for total_wages_for_the_week


# In[30]:


def convert_quiz_score_to_letter_grade(score):
    # A certain CS professor gives five-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F.
    # Complete this function which accepts a quiz score as an input and uses a decision structure to calculate the corresponding
    # grade. 
    # YOUR CODE HERE
    if score==5:
        return "A"
    elif score==4:
        return "B"
    elif score==3:
        return "C"
    elif score==4:
        return "F"
    elif score==2:
        return "D"
    elif score==1:
        return "F"
    elif score==0:
        return "F"


# In[31]:


# Test cell  for convert_quiz_score_to_letter_grade 
assert convert_quiz_score_to_letter_grade(0) == "F"
assert convert_quiz_score_to_letter_grade(1) == "F"
assert convert_quiz_score_to_letter_grade(2) == "D"
assert convert_quiz_score_to_letter_grade(3) == "C"
assert convert_quiz_score_to_letter_grade(4) == "B"
assert convert_quiz_score_to_letter_grade(5) == "A"


# In[32]:


def convert_exam_score_to_letter_grade(score):
    # A certain CS professor gives 100-point exams that are graded on the scale 90-100: A, 80-89: B, 70-79: C,
    # 69-69: D, < 60: F. Complete this function which accepts an exam score as input and uses a decision structure 
    # to calculate the corresponding grade. 
    # YOUR CODE HERE
     if 90 <= score <= 100:
        return "A"
     elif 80 <= score <= 89:
        return "B"
     elif 70 <= score <= 79:
        return "C"
     elif 60 <= score <= 69:
        return "D"
     else:
        return "F"

    


# In[33]:


assert convert_exam_score_to_letter_grade(55) == "F"
assert convert_exam_score_to_letter_grade(35) == "F"
assert convert_exam_score_to_letter_grade(65) == "D"
assert convert_exam_score_to_letter_grade(73) == "C"
assert convert_exam_score_to_letter_grade(87) == "B"
assert convert_exam_score_to_letter_grade(92) == "A"


# In[34]:


# Hiddent test cell for convert_exam_score_to_letter_grade


# In[35]:


# Exercise 4
def calculate_class_standing_from_credits(credits):
    # A certain college classifies students according to credits earned. A student with less than 7 credits is a Freshman.
    # At least 7 credits are required to be a Sophomore, 16 to be a Junior and 26 to be classifed as Senior. 
    # Complete this function which calculates the class standing from the number of credits earned. 
    # YOUR CODE HERE
    if credits >= 26:
        return('Senior')
    elif credits >= 16:
        return('Junior')
    elif credits >= 7:
        return('Sophomore')
    else:
        return('Freshman')
   
    


# In[36]:


assert calculate_class_standing_from_credits(6) == "Freshman"
assert calculate_class_standing_from_credits(13) == "Sophomore"
assert calculate_class_standing_from_credits(23) == "Junior"
assert calculate_class_standing_from_credits(45) == "Senior"


# In[37]:


# Hidden cell for calculate_class_standing_from_credits


# In[38]:


# Exercise 5
def calculate_fine(limit, speed):
    # The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph over the limit plus a 
    # penalty of $200 for any speed over 90 mph. Complete this function which accepts a speed limit and a clocked
    # speed and either return the string `Legal` or the amount of fine, if the speed is illegal. 

    # YOUR CODE HERE
    if speed <= limit:
        return f'Legal'

    # else calculating fine
    elif limit < speed < 90:
        fine = 50 + (speed - limit) * 5
    else:
        fine = 50 + 200 + (speed - limit) * 5

    return fine
    
    
    raise NotImplementedError()


# In[39]:


assert calculate_fine(55, 85) == 200
assert calculate_fine(55, 45) == 'Legal'
assert calculate_fine(55, 100) == 475


# In[40]:


# Hidden cell for calculate_fine


# # Reserving 22 points to manually go over the homework. I will take points off if you didn't use f-string for ALL the print exercises. 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




