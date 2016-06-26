# Treina uma rede neural de acordo com os paramtros passados
# basicamente pode-se customizar os valores mais importantes da rede neural, como camadas escondidas e taxa de aprendizado
import numpy as np
from itertools import product
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from math import sqrt
import cPickle as pickle
import argparse

# Valores default
DEFAULT_HIDDEN_LAYERS = [1, 3, 10]
DEFAULT_EPOCHS = [10, 30, 50]
DEFAULT_VALIDATION_FILE = ['verifing_data_1_2999_sample_01_random.txt']
DEFAULT_TRAIN_FILE = ['training_data_1_2999_sample_01_random.txt']
DEFAULT_LEARNING_RATES  = [0.3, 0.01]
DEFAULT_ADD_I = [False]

# Parser dos comandos
parser = argparse.ArgumentParser(description='Treina uma rede neural.')
parser.add_argument('--hidden-layers','-H', type=int, nargs='+', default = DEFAULT_HIDDEN_LAYERS,
                    help='hidden layers para a rede neural')
parser.add_argument('--epochs', '-E', type=int, nargs = '+', default = DEFAULT_EPOCHS,
                    help='Quantidade de epocas')
parser.add_argument('--train-file', '-T', nargs = 1, default = DEFAULT_TRAIN_FILE,
                    help='Arquivo de entradas para treinar')
parser.add_argument('--validation-file', '-V',  nargs = 1, default = DEFAULT_VALIDATION_FILE,
                    help='Arquivo de validacao para treinar')
parser.add_argument('--learning-rates', '-L', type=float, nargs = '+', default = DEFAULT_LEARNING_RATES,
                    help='Taxas de aprendizagem')
parser.add_argument('--add-i', '-I', type=bool, nargs = 1, default = DEFAULT_ADD_I,
                    help='Adiciona o Id do movimento no treinamento')



if __name__ == '__main__':
        args = parser.parse_args()
        train_file = args.train_file[0]
        hidden_size = args.hidden_layers
        validation_file = args.validation_file[0]
        learning_rates = args.learning_rates
        epochs = args.epochs
        add_i = args.add_i[0]


        # Carrega os arquivos com dataser
        train = np.loadtxt(train_file, delimiter = ' ')
        if not add_i:
                train = train[:, 1:]
        validation = np.loadtxt(validation_file, delimiter = ' ' )
        validation = validation[:, 1:]


        x_train = train
        y_train = validation


        input_size = x_train.shape[1]
        target_size = validation.shape[1]

        ds = SDS(input_size, target_size)
        ds.setField('input',train)
        ds.setField('target', validation)


        # executa pra cada conjunto de combinacoes de parametros
        for hidden_layer, epoch, learning_rate in product(hidden_size, epochs, learning_rates):
                output_model_file = 'model_{}-{}_learning-rate-{}_hidden-{}_epochs-{}.pkl'.format(train_file, learning_rate, hidden_layer, epoch,  "with_i" if add_i  else "without-i")
                output_data = 'model_result_{}-{}_learning_rate-{}_hidden-{}_epochs.txt'.format(train_file, learning_rate, hidden_layer, epoch, "with_i" if add_i else "without-i")

                net = buildNetwork(input_size, hidden_layer, target_size, bias = True)

                trainer = BackpropTrainer(net, ds, learningrate = learning_rate)

                print "Training for {} epochs with learning_rate={}, hidden_layer={} ...".format(epoch, learning_rate, hidden_layer)
                mse = 0

                # treina durante uma epoca
                for i in range(epoch):
	                mse = trainer.train()
	                rmse = sqrt(mse)
	                print "Training RMSE, epoch {}: {}".format(i + 1, rmse)
                        pickle.dump(net, open(output_model_file, 'wb'))

                # grava as estatisticas finais
                model_data = open(output_data, 'wb')
                model_data.write("rmse: {}".format(sqrt(mse)))
                model_data.close()


                # dump final do objeto que representa a rede neural
                pickle.dump(net, open(output_model_file, 'wb'))
