from Crypto.Cipher import DES

def read_in():
    print 'Enter your key: '
    key = raw_input()

    if len(key) > 8:
        raise KeyError
    if len(key) % 8 != 0 :
        key = key.zfill(8)

    print ''

    print 'Enter the message to be encrypted: '
    message = raw_input()

    if len(message) % 8 != 0:
        message = message.zfill(len(message) + 8 - len(message)%8)


    print ''

    return key, message

def encrypt(message, key):
    des = DES.new(key)
    cipher_text = des.encrypt(message)

    return cipher_text


def decrypt(cipher_text, key):
    des = DES.new(key)
    message = des.decrypt(cipher_text)

    return message

if __name__ == '__main__':
    vals = read_in()
    key = vals[0]
    message = vals[1]

    cipher_text = encrypt(message, key)
    print cipher_text
    clear_text = decrypt(cipher_text, key)
    print clear_text