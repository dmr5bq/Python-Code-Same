from Crypto.Hash import SHA256


def read_values():

    encrypted_empty_str = encrypt_string('')
    ret_dict = {}

    while 1:
        print( 'Please enter your username and password, hit return twice to exit.')
        tmp_username = raw_input('Username: ')
        tmp_password = raw_input('Password: ')
        print('')

        tmp_username = tmp_username.strip()
        tmp_password = tmp_password.strip()

        tmp_password = encrypt_string(tmp_password)

        if tmp_password == encrypted_empty_str:
            break

        ret_dict[tmp_username] = tmp_password

    return ret_dict


def check_credentials(username, password, user_list = {}):

    found_match_user = False
    found_match_pass = False

    password = encrypt_string(password)

    if username in user_list:
        found_match_user = True
        if password == user_list[username]:
            found_match_pass = True

    if found_match_user and found_match_pass:
        print('login succeeds')
    elif found_match_user and not found_match_pass:
        print('login fails')
    else:
        print('user not found')


def encrypt_string(raw_string):
    return SHA256.new(raw_string).hexdigest()


if __name__ == '__main__':
    list = read_values()
    check_credentials(raw_input('Enter Username: '), raw_input('Enter Password: '), list)