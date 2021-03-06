import numpy
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Dropout
import os
from keras.optimizers import SGD

def trainNN(base_params, neural_params, save = False):
    print("starting neural training")

    (WIDTH, HEIGHT, X, img_id, test, img_id_test, reversed_index, latex_index) = base_params
    (array_layers, dropout, epochs, batch_size) = neural_params

    # Create model
    model = Sequential()

    model.add(Dense(array_layers[0], input_dim=WIDTH * HEIGHT, activation='relu'))

    for i in range(1, len(array_layers)):
        model.add(Dense(array_layers[i], activation='relu'))
        #model.add(Dropout(dropout))

    model.add(Dense(len(img_id[0]), activation='softmax'))

    #sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train
    model.fit(X, img_id, epochs=int(epochs), batch_size=batch_size, verbose=2)

    # evaluation
    scores = model.evaluate(X, img_id)
    print("\ntrain : %s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

    # evaluation
    scores = model.evaluate(test, img_id_test)
    print("\ntest : %s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

    if save:
        # serialize model to JSON
        model_json = model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        model.save_weights("model.h5")
        print("Saved model to disk")

    return scores[1]


def UseNN(X):  #, img_id, reversed_index, latex_index):
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")

    # evaluate loaded model on test data
    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


    prediction = loaded_model.predict(X)

    # for i in range(0, len(prediction)):
    #     index1 = numpy.where(img_id[i] == 1)[0][0]
    #     str_index = reversed_index[index1]
    #     print(latex_index[str_index])
    #
    #     indexResult = numpy.where(prediction[i] == max(prediction[i]))[0][0]
    #     str_index_res = reversed_index[indexResult]
    #     print(latex_index[str_index_res])
    #     print(max(prediction[i]))
    #     print("----------------------------")

    print(prediction)
    print(prediction[0])
    return prediction[0]
