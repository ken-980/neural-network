import numpy as np

#neural network class 
class neuralNetwork:
    def __init__(self,inputnodes, hiddennodes, outputnodes,learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        #learning rate
        self.lr = learningrate

        # link weight matrics,wih : w_input_to_hidden_layer
        # who: w_hidden_to_output_layer
        self.wih = (np.random.rand(self.hnodes, self.inodes) - 0.5)
        self.who = (np.random.rand(self.onodes, self.hnodes) - 0.5)

    def train():
        pass

    def query():
        pass
        

