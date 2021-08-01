# probability
a place to hold some code in python for calculating probability  with sets


adding mutually exclusive or non mutually exclusive events

P(A or B) = P(A)+P(B) - P(A and B)

for non M.E. events  P(A and B) is the intersection of A and B

Which yo can do with the set data structure in Python

eg:

A = rolling an odd number on a die

B = rolling a number > two

so in python that is 

a = {1,3,5}

b = {3,4,5,6}

they are not mutually exclusive as there intersection len is greater >0

```python
>>> a.intersection(b)
{3, 5}
```
