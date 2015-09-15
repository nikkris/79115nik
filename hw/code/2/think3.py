__author__ = 'Nikhil Krishnan'

# Exercise 3.5
def do_twice(f,val):
    f(val)
    f(val)

def do_four(f,val):
    do_twice(f,val)
    do_twice(f,val)

def print_once(st):
    print(st)

print('+----+----+')
do_four(print_once,"|    |    |")
print('+----+----+')
do_four(print_once,'|    |    |')
print('+----+----+')





