import string, random

def passgenerator(type, length):
    if type =='nl':
        password = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(length))
    if type == 'nls':
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(length))
        return password

print(passgenerator(str(input('Enter type  ')), int(input('Enter pass length  '))))

