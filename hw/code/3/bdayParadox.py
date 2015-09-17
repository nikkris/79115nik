__author__ = 'nkrishn'

from random import randint

def has_duplicates(lst):
    for item in lst:
        indices = [ind for ind, x in enumerate(lst) if x == item]
        if len(indices) > 1:
            return True
    return False


# Part 1: test has_duplicates
testlist = [[12,31], [11,30],[2,11],[12,31]]
Status = has_duplicates(testlist)
print('Part 1#')
if Status:
    print "The list has duplicates"
else:
    print "The list does not have duplicates"

# Part 2:
num_expts = 10000
num_has_duplicates = 0
for expt in range(num_expts):
    bday_list = []
    for Lp in range(23):
        indi_bday = [randint(1,12)]
        assert isinstance(indi_bday, list)
        if (indi_bday[0] == 1 or indi_bday[0] ==3
            or indi_bday[0] ==5 or indi_bday[0] ==7
            or indi_bday[0] ==8 or indi_bday[0] ==10
            or indi_bday[0] ==12):
            indi_bday.append(randint(1,31))
        elif (indi_bday[0] == 4 or indi_bday[0] ==6
              or indi_bday[0] ==9 or indi_bday[0] ==11):
            indi_bday.append(randint(1,30))
        else:
            indi_bday.append(randint(1,28))
        bday_list.append(indi_bday)
    # print ("Loop: ", expt, "/n")
    # print (bday_list)
    if (has_duplicates(bday_list)):
        num_has_duplicates+= 1

Probdup = float(num_has_duplicates)/num_expts
print('Part 2#')
print"Probability of repeated birthdays in a " \
     "group of 23 people = ", Probdup


