'''
>>> JAAR
>>> 07/26/2023
>>> Practicing Fundamentals Program 11
>>> Version 1
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


def special_char_input() :
    '''
    >>> Takes a list of special characters from the user. If the characters contain integers or letters, will prompt the user to reenter the list of special characters.

    >>> Return: (str) special_characters
    '''
    while True :
        special_char = input('Enter each special character sequentially: ').replace(' ', '')
        if special_char.isalnum() :
            print('Your input must only contain special characters!')
            continue
        return special_char

def number_of(char_type : str)->int :
    '''
    >>> Asks the user for the number of a character types specified needed for password requirements.

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

def create_password(password_requirements : dict, length : int, special_char : str)->str :
    '''
    >>> Creates a random password for the user based on the users specifications.

    >>> Param: (dict) password_requirements, (int) length, (str) special_char
    >>> Return: (str) password
    '''
    character_list = ''
    if password_requirements['special'] :
        character_list += special_char
    if password_requirements['integer'] :
        character_list += string.digits
    if password_requirements['uppercase'] :
        character_list += string.ascii_uppercase
    if password_requirements['lowercase'] :
        character_list += string.ascii_lowercase
    print(character_list)
    while True :
        password = ''.join(random.choice(character_list) for _ in range(length))
        if password_requirements['special'] and sum(1 for ch in password if ch in special_char) < password_requirements['special'] :
                continue
        if password_requirements['integer'] and sum(1 for ch in password if ch.isnumeric()) < password_requirements['integer'] :
                continue
        if password_requirements['lowercase'] and sum(1 for ch in password if ch.islower()) < password_requirements['lowercase'] :
                continue
        if password_requirements['uppercase'] and sum(1 for ch in password if ch.isupper()) < password_requirements['uppercase'] :
                continue
        return password

def main() :
    print("Lets come up with a strong password together.")
    password_requirements = {}
    password_requirements['special'] = number_of('special characters')
    password_requirements['uppercase'] = number_of('uppercase characters')
    password_requirements['integer'] = number_of('integers')
    password_requirements['lowercase'] = number_of('lowercase characters')
    length = input_length(sum(password_requirements.values()))
    if password_requirements['special'] :
        special_char = special_char_input()
    print(create_password(password_requirements, length, special_char))

if __name__ == '__main__' :
    main()