#!/usr/bin/python3

def my_function(name, age):
    print("Hello, " + name + ". You're " + str(age) + " years old.")
    print(f'Hello, {name}. You\'re {age} years old.')

my_function("Test_Name", 100)

def my_age(age):
    print ("You are " + str(age))
    print ("You are", age)

my_age(32)