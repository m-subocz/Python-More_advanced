import os
import time
import string
from random import *
from faker import Faker
Faker.seed(0)
fake = Faker()

def menu():
    print('1. Phone passwords generator(4 digits)')
    print('2. Random name generator')
    print('3. Random password generator')
    print('4. Simple password cracker')
    print('0. exit')


def spacer():
    spc = '----------------'
    print(spc)
    print('DONE - saved to file')
    print(spc)
    print('\n')


def phone_passwordGEN():
    file = open('phone_passwords.txt', 'w')
    has = int(0)
    while has != 10000:
        file.writelines(str(has).zfill(4))
        file.writelines('\n')
        has = has + 1
    file.close()
    if has == 10000:
        os.system('clear')


def nameGEN():
    file = open('names.txt','w')
    opt_ilo = 1
    opt_ilo = int(input('Number of names: '))
    os.system('clear')
    for _ in range(opt_ilo):
        file.writelines(str(fake.name()))
        file.writelines('\n')
    file.close()


def passGEN():
    file = open('random_password.txt','w')
    leng = int(input('Number of characters: '))
    os.system('clear')
    
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    nu = string.digits
    sy = string.punctuation
    fu = lc + uc + nu + sy

    temp = random.sample(fu,leng)
    RPAS = "".join(temp)
    file.writelines(str(RPAS))
    file.writelines('\n')
    file.close()


def cracker():
    os.system('clear')
    user_pass = input("Enter your password: ")
    print('cracking ...')
    password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', '0']

    guess = ""
    start = time.time()
    while (guess != user_pass):
        guess = ""
        for letter in range(len(user_pass)):
            guess_letter = password[randint(0, 35)]
            guess = str(guess_letter) + str(guess)
    end = time.time()
    os.system('clear')
    print("Your password is",guess)
    print('cracking took:', start - end)

    
def Quitter():
    os.system('clear')
    os.system('exit')


os.system('clear')
opt = ''
while opt != '0':
    menu()
    opt = input('Choose operation: ')

    if opt == '1':
        phone_passwordGEN()
        spacer()    
    if opt == '2':
        nameGEN()
        spacer()
    if opt == '3':
        passGEN()
        spacer()
    if opt == '4':
        cracker()

Quitter()
