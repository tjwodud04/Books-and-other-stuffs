import numpy as np
from DefinitionOfAll import MatMul

c = np.array([1,0,0,0,0,0,0])
W = np.random.randn(7,3)
h = np.matmul(c,W)
print(h)
#예시 결과: [ 1.74947221 -1.82072491 -0.35537239]

c = np.array([1,0,0,0,0,0,0])
W = np.random.randn(7,3)
layer = MatMul(W)
h = layer.forward(c)
print(h)
#예시 결과: [-0.06390762 -0.41596388 -2.45394715]
