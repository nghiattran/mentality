import random


class Connection(object):
    def __init__(self, from_neuron, to_neuron, weight = 0):
        # if type(from_neuron) is not Neuron or type(to_neuron) is not Neuron:
        #     raise ValueError('A neuron must be a "Neuron" instance')
        self.from_neuron = from_neuron
        self.to_neuron = to_neuron
        self.weight = weight
        self.delta_weight = 0
        self.id = '{0}-{1}'.format(self.from_neuron.id, self.to_neuron.id)
        self.from_neuron.next.append(self)
        self.to_neuron.previous.append(self)

    def initialize(self, cb = None):
        if cb is None:
            self.threshold = random.uniform(-0.5, 0.5)
            print(self.threshold)
            return self

        self.threshold = cb()
        return self

    def to_json(self):
        return {
            'from': self.from_neuron.id,
            'to': self.to_neuron.id,
            'weight': self.weight
        }

    def calculate_weight_correction(self, learning_rate):
        # eq 6.12
        self.delta_weight = learning_rate * self.from_neuron.activation * self.to_neuron.error_gradient
        return self.delta_weight

    def update(self):
        self.weight += self.delta_weight
        return self

    def get_state(self):
        return self.weight * self.from_neuron.activation

    def get_error(self):
        return self.weight * self.to_neuron.error_gradient