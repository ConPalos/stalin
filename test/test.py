# a simple test to make sure everything is working properly

import sys

if __name__ == '__main__':
    print('Name is main!')
    print(sys.argv)
    raise ValueError('Exception needs to occur!')

else:
    print(f'Name is not main, but is {__name__}!')
    print(sys.argv)
    raise ValueError('Something horrible has happened!')