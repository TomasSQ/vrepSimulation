# Treina uma rede neural por algum tempo
import numpy as np
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from math import sqrt
import cPickle as pickle
from pybrain.structure import LinearLayer, SigmoidLayer, RecurrentNetwork
from pybrain.structure import FullConnection
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.validation import CrossValidator

train_file = 'training_data_1_2999_sample_01_random.txt'
validation_file = 'verifing_data_1_2999_sample_01_random.txt'


hidden_size = 10
epochs = 600
recurrent = False

output_model_file = 'model_1_{}_{}_hidden_{}_epochs_without_i.pkl'.format(train_file, hidden_size, epochs)

train = np.loadtxt(train_file, delimiter = ' ')
train = train[:, 1:]
validation = np.loadtxt(validation_file, delimiter = ' ' )
print validation.shape
validation = validation[:, 1:]


x_train = train
y_train = validation


input_size = x_train.shape[1]
target_size = validation.shape[1]

#print train

ds = SDS(input_size, target_size)
ds.setField('input',train)
ds.setField('target', validation)


net = buildNetwork(input_size, hidden_size, target_size, bias = True, recurrent = recurrent)


trainer = BackpropTrainer(net,ds, verbose = True, learningrate = 0.3)


print "training for {} epochs...".format(epochs)

for i in range(epochs):
	mse = trainer.train()
	rmse = sqrt(mse)
	print "training RMSE, epoch {}: {}".format(i + 1, rmse)
        #perform crossvalidation
        pickle.dump(net, open(output_model_file, 'wb'))



pickle.dump(net, open(output_model_file, 'wb'))
