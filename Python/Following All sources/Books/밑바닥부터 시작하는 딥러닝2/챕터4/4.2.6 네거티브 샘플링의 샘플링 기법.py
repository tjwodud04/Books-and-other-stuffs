import numpy as np

print(np.random.choice(10))
print(np.random.choice(10))
print()

words = ['you', 'say', 'goodbye', 'I', 'hello', '.']
print(np.random.choice(words))
print()

print(np.random.choice(words, size=5))
print(np.random.choice(words, size=5, replace=False))
print()

p = [0.5, 0.1, 0.05, 0.2, 0.05, 0.1]
print(np.random.choice(words, p=p))
print()

p = [0.7, 0.29, 0.01]
new_p = np.power(p, 0.75)
new_p /= np.sum(new_p)
print(new_p)