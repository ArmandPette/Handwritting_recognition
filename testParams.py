import trainNN
import numpy as np

def testParams(base_params):
    (WIDTH, HEIGHT, X, img_id, test, img_id_test, reversed_index, latex_index) = base_params
    wh = WIDTH * HEIGHT
    array_layers = (3 * wh, wh, int(wh / 2), int(wh / 2))
    dropout = 0
    epochs = 50
    batch_size = 90

    max_accuracy = 0
    best_params = None

    start = 1
    step = 5
    stop = 2*step + start + 1

    param_list = recursiveList(dropout_range=[0, 0.5],
                               epoch_range=[100],
                               nb_layer_range=[2, 5, 7],
                               layer_range=[0.5, 5])

    for param in param_list:

        array_layers = []
        for i in range(2, len(param)):
            array_layers.append(i * int(wh/5))

        neural_params = (array_layers, param[0], param[1], batch_size)
        acc = trainNN.trainNN(base_params, neural_params)
        print("\n%.2f%%" % (acc * 100))
        if (acc > max_accuracy):
            max_accuracy = acc
            best_params = neural_params
        print("best_params :")
        print(best_params)
        print(max_accuracy)
        print("-------------------------------")

    return best_params


def recursiveList(dropout_range, epoch_range, nb_layer_range, layer_range):

    result = []

    for i in nb_layer_range:
        array = np.zeros(i + 2)
        result.extend(build_list(dropout_range, epoch_range, layer_range, array, 0))

    return result


def build_list(dropout_range, epoch_range, layer_range, array_format, indice):

    result = []

    if(indice == 0):
        array = np.array(array_format)
        for i in dropout_range:
            array[indice] = i
            result.extend(build_list(dropout_range, epoch_range, layer_range, array, indice+1))
    elif(indice == 1):
        array = np.array(array_format)
        for i in epoch_range:
            array[indice] = int(i)
            result.extend(build_list(dropout_range, epoch_range, layer_range, array, indice+1))
    else:
        array = np.array(array_format)
        for i in layer_range:
            array[indice] = int(i)
            if indice == (len(array) - 1):
                result.append(tuple(array))
            else:
                result.extend(build_list(dropout_range, epoch_range, layer_range, array, indice+1))
    return result



