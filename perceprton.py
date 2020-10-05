import random

class Perceptron:

    entry_values = [1]
    entry_weights = []
    learning_factor = 0.2
    error = False

def __init__(self, _entry_count, _learning_factor):
    self.entry_values.append(random.random()/10)
    for i in range(_entry_count):
        self.entry_values.append(0)
        self.entry_weights.append(random.random()/10)
    self.learning_factor = _learning_factor

def bipolar_function(self, _sum):
    return (1 if _sum > self.bias else -1)

def entry_function(self):
    for i in range(self.entry_values):
        self.entry_values[i] = 1 if self.entry_values[i] > 0 else -1

def sum(self):
    sum = 0;
    for i in range(self.entry_values):
        sum += self.entry_values[i] * self.entry_weights[i]
    return sum
def weight_change(_label, _entry_value, _final_value):
    return  (_label - _final_value)  * _entry_value

def learning(self, learning_set):
     label,entry_values = learning_set




