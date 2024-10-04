from math import sqrt
from operator import add

# run this script, analyze the output 
# fix the codes based on the instructions given

# 1. Given char1 and num1, edit line 11 
#    to generate the string 'EEE111' and assign it to eee111String variable
char1 = 'e'
num1 = 1 
eee111String = (char1.capitalize())*3 + str(num1)*3
print(eee111String)

# 2. Given num1 and num2, edit line 18
#    to get their corresponding sum as integer (e.g. num1 + num2 = 333)
num1 = '111'
num2 = '222'
sum12 = int(num1) + int(num2)
print(sum12)

# 3. edit the hypotenuse function below using only sqrt(), add() and pow() functions
def hypotenuse(param_a, param_b):
    result_c = sqrt(add(pow(param_a,2),pow(param_b,2)))
    return result_c

arg_a = 4
arg_b = 3
hypo_c = hypotenuse(arg_a, arg_b)  
msg = f'side_a = {arg_a} side_b = {arg_b} hypo_c = {hypo_c} '
print(msg)

#4. edit the following line below to create a getHypo function
getHypo = hypotenuse

arg_a = 5
arg_b = 12
hypo_c = getHypo(arg_a, arg_b)
msg = f'side_a = {arg_a} side_b = {arg_b} hypo_c = {hypo_c} '
print(msg)

#Final Output - Commit Hash "Week 1 and 2"