# Treina uma rede neural por algum tempo
import numpy as np

from math import sqrt
import cPickle as pickle
import neurolab as nl

train_file = 'training_data_1_2999_sample_0.1s.txt'
validation_file = 'training_data_1_2999_sample_0.1s.txt'
output_model_file = 'model_1_training_data_1_50_hidden_200_epochs_without_i_neurolab.pkl'

hidden_size = 50
epochs = 200

train = np.loadtxt(train_file, delimiter = ' ')
#train = train[:, 1:]
validation = np.loadtxt(validation_file, delimiter = ' ' )
print validation.shape
validation = validation[:, 1:]


x_train = train
y_train = validation


input_size = x_train.shape[1]
target_size = validation.shape[1]

print input_size


net = nl.net.newelm([[-5, 5]] * input_size, [input_size*200, target_size], [nl.trans.TanSig(), nl.trans.PureLin()])
# Set initialized functions and init
net.layers[0].initf = nl.init.InitRand([-0.1, 0.1], 'wb')
net.layers[1].initf= nl.init.InitRand([-0.1, 0.1], 'wb')

error = net.train(train, validation, epochs=500, show=30, goal=0.001)

#Add layers to the neural net module

pickle.dump(net, open(output_model_file, 'wb'))
