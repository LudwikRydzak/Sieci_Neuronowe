import random
import numpy as np

class Perceptron:
    def __init__(self, _entry_count, _learning_factor, _max_epochs, _weight_range_begin, _weight_range_stop):
        self.entry_values = []
        self.entry_weights = []
        self.entry_values.append(1)
        self.weight_range = _weight_range_begin, _weight_range_stop
        self.bias = 1
        self.entry_weights.append(random.random() * (_weight_range_stop-_weight_range_begin) + _weight_range_begin)
        # for example i need value from range [-0.5, 0.5]
        # [0,1]*(0.5-(-0.5))+(-0.5) = [0,1]*1-0.5 = [-0.5,0.5]
        self.max_epoch = _max_epochs

        for i in range(_entry_count):
            self.entry_values.append(0)
            self.entry_weights.append(random.random() * (_weight_range_stop-_weight_range_begin) + _weight_range_begin)
        self.learning_factor = _learning_factor

    def bipolar_function(self, _sum):
        return 1 if _sum > 0 else -1

    def unipolar_function(self, _sum):
        return 1 if _sum > 0 else 0

    def output(self, _sum, _uni0_bi1):
        if _uni0_bi1 == 0:
            return self.unipolar_function(_sum)
        if _uni0_bi1 == 1:
            return self.bipolar_function(_sum)


    def entry_function(self, _entry_values):
        for i in range(len(_entry_values)):
            self.entry_values[i + 1] = _entry_values[i]

    def sum(self):
        sum = 0.0;
        for i in range(len(self.entry_values)):
            sum += self.entry_values[i] * self.entry_weights[i]
        return sum

    def weight_change(self, _label, _entry_value, _final_value):
        return (_label - _final_value) * _entry_value

    def learn(self, _learning_set, _uni0_bi1):
        epoch = 1
        is_learning_error = True
        while (is_learning_error and epoch<self.max_epoch):
            is_learning_error = False
            for i in range(len(_learning_set)):
                set = _learning_set[i]
                label, entry_values_set = set[0], set[1:]
                self.entry_function(entry_values_set)
                sum = self.sum()
                output = self.output(sum, _uni0_bi1)
                for j in range(len(self.entry_values)):
                    change = self.weight_change(label, self.entry_values[j], output)
                    if (change != 0):
                        self.entry_weights[j] = self.entry_weights[j] + self.learning_factor * change
                        is_learning_error = True
            epoch += 1
        # print(f'Liczba epok uczenia: {epoch}')
        # print(self.entry_weights)
        return epoch

    def prediction(self, _test_set, _uni0_bi1):
        self.entry_function(_test_set)
        sum = self.sum()
        output = self.output(sum, _uni0_bi1)
        return output
    def test_perceptron(self, _test_sets, _uni0_bi1):
        correct_answers = 0
        wrong_answers = 0
        for i in range(len(_test_sets)):
            test_set = _test_sets[i]
            label, set = test_set[0], test_set[1:]
            output = self.prediction(set, _uni0_bi1)
            if(output == label):
                correct_answers += 1
            else:
                wrong_answers += 1
        percent = round(correct_answers/(correct_answers+wrong_answers), 4) *100
        return percent