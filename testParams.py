import trainNN

def testParams(base_params):
    (WIDTH, HEIGHT, X, img_id, reversed_index, latex_index) = base_params
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

    for layer1 in (range(start, stop, step)):
        for layer2 in range(start, stop, step):
            for layer3 in (range(start, stop, step)):
                for layer4 in range(start, stop, step):
                    for dropout in range(0, 1):
                        for epochs in range(50, 51):

                            array_layers = (layer1 * int(wh/5), layer2 * int(wh/5),
                                            layer3 * int(wh/5), layer4 * int(wh/5))
                            neural_params = (array_layers, dropout, epochs, batch_size)
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
