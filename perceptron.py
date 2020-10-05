import random


class Perceptron:
    def __init__(self, _entry_count, _learning_factor):
        self.entry_values = []
        self.entry_weights = []
        self.entry_values.append(1)
        self.entry_weights.append(random.random() / 10)
        for i in range(_entry_count):
            self.entry_values.append(0)
            self.entry_weights.append(random.random() / 10)
        self.learning_factor = _learning_factor

    def bipolar_function(self, _sum):
        return (1 if _sum > self.bias else -1)

    def entry_function(self, _entry_values):
        for i in range(len(self.entry_values)):
            self.entry_values[i] = 1 if _entry_values[i] > 0 else -1

    def sum(self):
        sum = 0;
        for i in range(len(self.entry_values)):
            sum += self.entry_values[i] * self.entry_weights[i]
        return sum

    def weight_change(_label, _entry_value, _final_value):
        return (_label - _final_value) * _entry_value

    def learn(self, _learning_set):
        epoch = 1
        is_learning_error = True
        while (is_learning_error):
            for i in range(len(_learning_set)):
                label, entry_values = _learning_set[0], _learning_set[1:]
                self.entry_function(entry_values)
                sum = self.sum()
                output = self.bipolar_function(sum)
                for j in range(entry_values):
                    change = self.weight_change(label, entry_values[j], output)
                    if (change != 0):
                        self.entry_weights[j] = self.entry_weights[j] + self.learning_factor * change
                        is_learning_error = True
                    else:
                        is_learning_error = False
            epoch += 1
            print('.')
        print(epoch)
        print(self.entry_weights)
