import os, json


def get_number_of_lines_in_directory():

    store_to_json = {}
    count_lines = 0

    for name in os.listdir('.'):
        if os.path.isfile(name):
            num_lines = sum(1 for line in open(name))
            store_to_json[name] = num_lines
            count_lines += num_lines

    with open('file_info.txt', 'w') as write_file:
        json.dump(store_to_json, write_file)

    return count_lines


def check_number_of_lines():

    file_info = 'file_info.txt'

    with open (file_info) as read_file:
        read_dict = json.loads(read_file.read())

    for file_name in read_dict:
        if os.path.isfile(file_name):
            num_lines = sum(1 for line in open(file_name))
            len_current = num_lines
            len_json = read_dict[file_name]

            if len_current != len_json:
                print file_name + ' has an altered number of lines.'


if __name__ == '__main__':
    check_number_of_lines()
    get_number_of_lines_in_directory()