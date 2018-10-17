""" NTLMacaroni is a tool for parsing NTLM hash files """
import os
import sys

# Check if the correct number of arguments where provided
try:
    ENCODED_PATH = sys.argv[1]
except:
    print("Invalid use of this command. Pass a file path as first argument")
    exit(1)

def check_file_path(path: str):
    """ Checks if a file exsists with specified path. If not, exit """
    if not os.path.exists(path):
        print("Error file specified does not exist. Please use argument one as a file path")
        exit(1)

def parse_line(ltp: str):
    """ Takes in a single line of a file, and formats it in k:v notation """
    # Remove the domain name from the dump
    no_domain = ltp[str.find(ltp, '\\') + 1:]
    if not no_domain:  # If there is no domain specified in the first place lets avoid an AIOOB
        no_domain = ltp
    print(no_domain)
    seperated_vals = str.split(no_domain, ':')
    return str(seperated_vals[0])+ ":" +str(seperated_vals[3])+ "\n"


# Check if the file exsists
check_file_path(ENCODED_PATH)
print("Loading file: "+ str(ENCODED_PATH.split("/")[len(ENCODED_PATH) - 1]) )

input_file = open(ENCODED_PATH, "r")
i = 0
output = ""

for line in input_file:
    output += parse_line(line)
    i += 1
    
    # Prtinting to stdout takes a lot of cpu / kernel time. Only do it once per 50 lines
    if counter % 50 == 0:
        print("Entries Formatted: " + str(i), end="\r")

# Write file once at end of program (Less file I/O = faster)
file = open(str(os.path.basename(ENCODED_PATH)) + ".formatted", "a+")
file.write(output)
file.close()

print("New file created with k:v format. The file is called " + os.path.basename(ENCODED_PATH) + ".formatted")
exit(0)
