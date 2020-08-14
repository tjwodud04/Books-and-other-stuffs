items = 'zero one two three'.split()

print(items)
'''
['zero', 'one', 'two', 'three']
'''

example = 'python,jquery,javascript'

print(example.split(","))
'''
['python', 'jquery', 'javascript']
'''

a, b, c = example.split(",")

example2 = 'cs50.gachon.edu'

subdomain, domain, tld = example2.split(".")