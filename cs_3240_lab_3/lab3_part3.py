from Crypto.Hash import SHA256

import os, json


def store_file_hash():

    store_to_json = {}

    for name in os.listdir('.'):
        if os.path.isfile(name):
            file_text = open(name).read()
            file_hash = SHA256.new(file_text).hexdigest()

            store_to_json[name] = file_hash

    with open('file_info_encryption.txt', 'w') as write_file:
        json.dump(store_to_json, write_file)



def check_file_alteration():
    name_of_this_file = 'lab3_part3.py'

    file_info = 'file_info_encryption.txt'

    with open (file_info) as read_file:
        read_dict = json.loads(read_file.read())

    for name in read_dict:
        if os.path.isfile(name):
            read_data = open(name).read()
            hash_current = SHA256.new(read_data).hexdigest()
            hash_json = read_dict[name]

            if hash_current != hash_json:
                print name + ' has been altered!'


if __name__ == '__main__':
    check_file_alteration()
    store_file_hash()