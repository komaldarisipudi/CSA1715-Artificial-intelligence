import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def feed_forward_nn(input_data, weights, biases):
    layer_input = input_data
    for w, b in zip(weights, biases):
        layer_output = np.dot(w, layer_input) + b
        layer_input = sigmoid(layer_output)
    return layer_input

# Example Usage
input_data = np.array([0.1, 0.2, 0.7])
weights = [np.array([[0.1, 0.2, 0.3], [0.2, 0.3, 0.4], [0.3, 0.4, 0.5]]),
           np.array([[0.5, 0.6, 0.7], [0.6, 0.7, 0.8]])]
biases = [np.array([0.1, 0.2, 0.3]), np.array([0.4, 0.5])]

output = feed_forward_nn(input_data, weights, biases)
print(output)
