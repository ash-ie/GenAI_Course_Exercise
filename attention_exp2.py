import numpy as np

Q = np.array([
    [1,0],
    [0,1]
])

k = np.array([
    [1,0],
    [0,1]
])

v = np.array([
    [10,20],
    [30,40]
])

print(f"Q: {Q}")
print(f"k: {k}")
print(f"v: {v}")

d_k = k.shape[-1]

scores = (Q @ k.T) / np.sqrt(d_k)

print(f"attention scores: {scores}")

def softmax(x):
    exp = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp / exp.sum(axis=-1, keepdims=True)

attention_weight = softmax(scores)

print(f"attention weight: {attention_weight}")

output = attention_weight @ v

print(f"attention output: {output}")