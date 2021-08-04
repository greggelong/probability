import scipy.stats as stats

## probability mass function
## Checkpoint 1
# calculating P(4-6 heads) = p(4 heads) + p(5 heads) + p(6 heads)
# 
prob_1 = stats.binom.pmf(4,n=10, p=.5) + stats.binom.pmf(5,n=10, p=.5)+ stats.binom.pmf(6,n=10, p=.5)
print(prob_1)

## Checkpoint 2
'''
Use the 1 minus the sum of some values of stats.binom.pmf() method to set prob_2 to the probability of observing more than 2 heads from 10 coin flips.

'''
# 1 minus the sum of some values
prob_2 =  1- (stats.binom.pmf(0,n=10,p=.5)+stats.binom.pmf(1,n=10,p=.5)+stats.binom.pmf(2,n=10,p=.5))
print(prob_2)