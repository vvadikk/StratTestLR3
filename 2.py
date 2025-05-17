import random
import string
letters = string.ascii_letters
digits = string.digits
special = '@#%_^!)(*?'
all_char = letters + digits + special
mandatory = [random.choice(letters), random.choice(digits), random.choice(special)] #Чтобы в пароле обязательно былы спец символы, цифры и буквы
passw = ''.join(random.sample(all_char, 9)) + ''.join(mandatory)
while len(set(passw)) != len(passw): #Проверка на повторяющиеся символы
    passw = ''.join(random.sample(all_char, 9)) + ''.join(mandatory)
print('Пароль:', passw)
