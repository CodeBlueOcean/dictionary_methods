# Dictionary
user = {
    'basket' : [1,2,3],
    'greet' : 'hello'
}

print(user.get('age'))

# Dictionary another example default value 55
user = {
    'basket' : [1,2,3],
    'greet' : 'hello'
}

print(user.get('age', 55))

# Dictionary another example 
user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age': 20
}

print(user.get('age', 55))


# Dictionary another example
user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age': 20
}

# not very common way but works below
user2 = dict(name='JohnJohn')

print(user2)





