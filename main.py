from names import nameList
import random

characterset = ['@','_','$','&','!']
domain_list = ['@gmail.com','@hotmail.com','@yahoo.com','@protonmail.com']
def email_generator():
    email = random.choice(nameList)
    number = random.randint(1,10000)
    domain = random.choice(domain_list)
    print(email+str(number)+domain)

def password_generator():
    paswword = random.choice(nameList)
    number = random.randint(1,1000)
    character = random.choice(characterset)
    print(paswword+character+str(number))


if __name__ == "__main__":
    size = int(input("Enter the number of emails and passwords you need : "))
    for i in range(1,size):
        email_generator()
        password_generator()