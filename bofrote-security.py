import hashlib
from random import randrange

NO_OF_ROTATIONS = 5000000

# TODO md5 has to be replaced with a custom encryption method.
# I used md5 becaudse of its irreversibilty. In an environment like this app, IRREVERSIBILITY is the key

# TODO Develop an API out of this

def encrypt():
    # create a random number for ranges in iterations
    no_of_iterations = randrange(NO_OF_ROTATIONS)

    text_value = "whatever"

    for x in range(0, no_of_iterations):
        new_text_value = hashlib.md5(text_value.encode('utf-8')).hexdigest()

        text_value = new_text_value

    return text_value



def decrypt():
    hashed_password = "0f6510fc3e1c4d9e32850ffd3412f6e2"
    try_password = "whatever"

    for x in range(0, NO_OF_ROTATIONS):
        new_try_password = hashlib.md5(try_password.encode('utf-8')).hexdigest()
        # print new_try_password
        try_password = new_try_password

        if try_password == hashed_password:
            return "Password Found"

    return "Password not found"


name = encrypt()
print name
