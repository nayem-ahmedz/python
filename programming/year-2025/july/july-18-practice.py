age = 25
name = 'Nayem Ahmed'
weight = 67.5

# print(f"Hey, I am {name}, and I am {age} years old, and my weight is {weight}")

# print(type(weight))

floatAge = float(age)
# print(floatAge, type(floatAge))
# print(int('101'))
# print(bool('101'))

# print(10/2)
# print(10//2)

# print(name[0])
# print(name[-1])

sentence = 'My loved one named Hajifa Jui'
wife = sentence[19:29]
# print(wife)
# print(len(wife))

wife = 'Hajifa'
# print(wife)
# wife[0] = 'J' // error

upperCase = wife.upper()
# print(upperCase)
lowerCase = upperCase.lower()
# print(lowerCase)

sentence = 'He is the Boss, and he have the right to change the boster Coal'
# print(sentence)
sentence = sentence.lower().replace('b', '-').capitalize()
# print(sentence)

# print(sentence.find('Change'))
# print(sentence.find('change'))

# loc = 'C:\\home\downloads'
loc = r'C:\\home\downloads'
print(loc)