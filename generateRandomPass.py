import random
import string

def rand_pass(size):
    generate_pass = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
    return generate_pass


def main():
    s =int(input("Enter size to create random password: "))
    password = rand_pass(s)
    print(password)

if __name__=="__main__":
    main()
