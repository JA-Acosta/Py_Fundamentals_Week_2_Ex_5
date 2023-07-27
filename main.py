'''
>>> JAAR
>>> 07/26/2023
>>> Practicing Fundamentals Program 11
>>> Version 2
'''

'''
>>> Generates a program that will create a random password for the user based on the parameters provided by the user.
'''

import random
import string

def input_length(minimum_characters : int)->int :
    '''
    >>> Asks the user to input the length of the password as an integer that is at least the minimum length required to meet all the parameters of the password. Otherwise, ask the user to enter another length.

    >>> Return: (int) length
    '''
    while True :
        try :
            length = int(input('Enter password length: '))
            if length < minimum_characters :
                raise IndexError
        except ValueError :
            print('The length must be an integer.')
        except IndexError :
            print(f'The length must contain at least {minimum_characters}.')
        else:
            return length


def special_char_input()->str :
    '''
    >>> Takes a list of special characters from the user. If the characters contain integers or letters, will prompt the user to reenter the list of special characters.

    >>> Return: (str) special_characters
    '''
    while True :
        special_char = input('Enter each special character sequentially: ').replace(' ', '')
        if not special_char :
            print('Enter at least one special character.')
            continue
        if any(char.isalnum() for char in special_char) :
            print('Please only enter special characters.')
            continue
        return special_char

def number_of(char_type : str)->int :
    '''
    >>> Asks the user for the minimum number of a character type required for the password.

    >>> Param: (str) char_type
    >>> Return: (int) response
    '''
    while True :
        try :
            response = int(input(f'Enter the minimum number of {char_type} required: '))
        except ValueError :
            print('Your input is invalid!')
        else :
            return response

def create_password(requirements : dict, length : int)->str :
    '''
    >>> Creates a random password for the user based on the users specifications.

    >>> Param: (dict) password_requirements, (int) length
    >>> Return: (str) password
    '''
    character_list = ''.join(requirements[key][1] for key in requirements.keys() if requirements[key][0])

    while True :
        password = ''.join(random.choice(character_list) for _ in range(length))
        for key in requirements.keys() :
            requirements[key][2] = sum(1 for ch in password if ch in requirements[key][1])
        if any(requirements[key][0] < requirements[key][2] for key in requirements.keys()) :
            continue
        return password

def main() :
    print("Lets come up with a strong password together.")
    requirements = {} # Value = [(int) type requirement, (str) char of type, (int) password type occurrence]
    requirements['special'] = [number_of('special characters'), '', 0]
    requirements['uppercase'] = [number_of('uppercase characters'), string.ascii_uppercase, 0]
    requirements['lowercase'] = [number_of('lowercase characters'), string.ascii_lowercase, 0]
    requirements['integer'] = [number_of('integers'), string.digits, 0]
    length = input_length(sum( requirements[key][0] for key in requirements.keys() if requirements[key][0]))
    if requirements['special'][0] :
        requirements['special'][1] = special_char_input()
    print(create_password(requirements, length))

if __name__ == '__main__' :
    main()