import uuid, random

def uuid1():
    return str(uuid.uuid1())

def uuid3():
    return str(uuid.uuid3())

def uuid5():
    return str(uuid.uuid5())

def uuid4():
    return str(uuid.uuid4())

def imei():
    def checksum(number, alphabet='0123456789'):
        n = len(alphabet)
        number = tuple(alphabet.index(i)
                    for i in reversed(str(number)))
        return (sum(number[::2]) +
                sum(sum(divmod(i * 2, n))
                    for i in number[1::2])) % n

    def calc_check_digit(number, alphabet='0123456789'):
        """Calculate the extra digit."""
        check_digit = checksum(number + alphabet[0])
        return alphabet[-check_digit]
    
    imei = '99001201' + str(random.randint(000000, 999999))
    return imei + calc_check_digit(imei)