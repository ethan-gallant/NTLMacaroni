import os
import sys

ENCODED_PATH = sys.argv[1]


def check_file_path():
    if not os.path.exists(ENCODED_PATH):
        print("Error file specified does not exist. Please use argument one as a file path")
        exit()
    print("File found. Proceeding")


def write_kv_notation(user,hash):
    output_file = open(os.path.basename(ENCODED_PATH) + ".formatted", "a+")
    output_file.write(user+":"+hash + "\n")
    output_file.close()


def parse_line(ltp):
    # Remove the domain name from the dump
    no_domain = ltp[str.find(ltp, '\\') + 1:]
    if not no_domain:  # If there is no domain specified in the first place lets avoid an AIOOB
        no_domain = ltp
    print(no_domain)
    seperated_vals = str.split(no_domain, ':')
    write_kv_notation(seperated_vals[0], seperated_vals[3])


check_file_path()

input_file = open(ENCODED_PATH, "r")
counter = 0

for line in input_file:
    parse_line(line)
    ++counter
    if counter % 100 == 0:
        print("Entries Formatted" + counter)

print("New file created with k:v format. The file is called " + os.path.basename(ENCODED_PATH) + ".formatted")

