from itertools import product


def prob(x):
    global omega
    return len(x)/len(omega)



def cond_prob(x,y):
    ''' prob of x if we have seen y return the len of intersection divided by len y'''
    return len(x & y) / len(y)
    

def are_indep(x,y):
    return prob(x & y) == prob(x) * prob(y)

    

print(list(product([1,2], ['a','b','c'])))

# cartesian product


# create sample space serch of all possible outcomes

# tossing a coin several times the space is the set of all
# possible sequences of HT that could arise

n = 3 # number of coin tosses

o = list(product(['H','T'], repeat = n))  ## as a list
omega = set(product(['H','T'], repeat = n)) ## as a set

print(o, len(o))

print(omega, len(omega))

# condition a: that first toss of 3 tosses is a tail


a = {om for om in omega if om[0] == 'T'}

print(a)

# condition b: that there are exactly 2 tails

b = {om for om in omega if om.count('T') ==2}

print(b)

print('prob a', prob(a), 'prob b',prob(b))

print("conditional probability of a (first is T) given b (exactly 2 tails)", cond_prob(a,b))

## a and b are not independant

## we can check the probability of their intersection

print("prob of a and b intersection", prob(a & b))

## and check the product of prob a and b

print("prob(a) * prob(b)", prob(a)*prob(b))

## thoese are different so they are not independant

## see the function at the top

print('are_indep(a,b)', are_indep(a,b))

# independant event
# that the second toss is a heads
c = {om for om in omega if om[1] == 'H'}
print('c: that second toss is a head\n',c)

print('a: first is a T given c: second toss is a H are independant')
print('are_indep(a,c)',are_indep(a,c))






