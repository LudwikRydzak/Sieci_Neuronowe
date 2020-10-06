import random
import numpy as np

class Perceptron:
    def __init__(self, _entry_count, _learning_factor):
        self.entry_values = []
        self.entry_weights = []
        self.entry_values.append(1)
        self.bias = 5
        self.entry_weights.append(random.random() / 10)

        for i in range(_entry_count):
            self.entry_values.append(0)
            self.entry_weights.append(random.random() / 10)
        self.learning_factor = _learning_factor

    def bipolar_function(self, _sum):
        return 1 if _sum > 0 else -1

    def entry_function(self, _entry_values):
        for i in range(len(_entry_values)):
            self.entry_values[i+1] = 1 if _entry_values[i] > 0 else -1

    def sum(self):
        sum = 0;
        for i in range(len(self.entry_values)):
            sum += self.entry_values[i] * self.entry_weights[i]
        return sum

    def weight_change(self, _label, _entry_value, _final_value):
        return (_label - _final_value) * _entry_value

    def learn(self, _learning_set):
        epoch = 1
        display_epoch =''
        is_learning_error = True
        while (is_learning_error and epoch<20000):
            is_learning_error = False
            display_epoch = display_epoch+'.'
            for i in range(len(_learning_set)):
                set = _learning_set[i]
                label, entry_values_set = set[0], set[1:]
                self.entry_function(entry_values_set)
                sum = self.sum()
                output = self.bipolar_function(sum)
                for j in range(len(self.entry_values)):
                    change = self.weight_change(label, self.entry_values[j], output)
                    if (change != 0):
                        self.entry_weights[j] = self.entry_weights[j] + self.learning_factor * change
                        is_learning_error = True
            print(epoch)
            epoch += 1

        print(display_epoch)
        print(self.entry_weights)
