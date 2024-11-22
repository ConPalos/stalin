# gulag.py
# a python module that will check your code for errors
# and if it sees one, will send it to the gulag
# inspired by fuckit.js
# by Ethan Cohen

from random import randint
import re
import sys
import traceback

recovery_string = 'release'

messages = [
    "Don't worry, I've already taken care of it.",
    "It's okay, he will never make another mistake again."
]

args = sys.argv

# null check
if len(args) == 1:
    raise ValueError(f'Please specify either a file to run or "{recovery_string}" to release your prisoners')

module_with_args = args[1:]
module = args[1]

# if we want to recover files, note that here
if len(args) == 2 and module == recovery_string:
    # TODO
    pass

if len(module_with_args) > 1:
    args = module_with_args[1:]

else:
    args = []

# try to run the code (hopefully it works)
try:
    sys.argv = module_with_args
    data = open(module, 'r').read()
    exec(data)

except Exception as e:
    # uh oh, time to send some code to the gulag!
    tb = traceback.format_exc()

    lines = re.findall(r'\n.*".*".*line \d+, in .*\n', tb)

    print(lines)

    # filter out anything that includes this file (no destroying ourselves)
    lines = [line for line in lines if 'gulag.py' not in line]

    # edge condition: that's it!
    if not lines:
        raise Exception('You have sent all of your code to gulag. Good job!')

    # now only consider the last line of code
    line = lines[-1]

    # get the file name and line in the file
    file_name = re.findall(r'".*"', line)[0].strip('"')
    line_number = re.findall(r'\d+', line)[0]
    line_number = int(line_number)

    # edge case: the file might be the one called initially
    if file_name == '<string>':
        file_name = module

    # read in the file
    f = open(file_name)
    code = f.readlines()
    f.close()
    
    # extract the relevant line of code
    prisoner = code.pop(line_number - 1)

    # write it to the gulag
    gulag = open('gulag.ussr', 'at')
    gulag.write(f'{file_name}#{line_number}#{prisoner}')
    gulag.close()

    # write most of the data back to the file (with one line conspicuously absent)
    f = open(file_name, 'w')
    for snippet in code:
        f.write(snippet)

    f.close()

    # and now print the traceback
    print(tb)
    msg_idx = randint(0, len(messages) - 1)
    message = messages[msg_idx]
    print(f'{message}')