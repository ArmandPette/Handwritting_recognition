from hasy_tools import *
import numpy
import trainNN
import testParams
from our_database import *
from reconstructWord import *

train_NN = True

def concatenate(tab1, tab2):
    temp = []
    temp.extend(tab1)
    temp.extend(tab2)
    return np.array(temp)

def train():
    numpy.random.seed(7)

    WIDTH, HEIGHT = 32, 32

    index, latex_index = generate_index("hasy-data-labels2.csv")
    print("index generated")

    reversed_index = {}
    for k, v in index.items():
        reversed_index[v] = k

    (img_src1, img_id1) = load_images("hasy-data-labels2.csv", index)

    (img_src2, img_id2) = get_letters("Resultat")


    img_src = concatenate(img_src1, img_src2)
    img_id = concatenate(img_id1, img_id2)

    print("images loaded")

    length = len(img_id)
    length_test = int(0.1 * length) + 1

    img_id_test = np.zeros((length_test, len(img_id[0])))
    X = np.zeros((length - length_test, WIDTH * HEIGHT))
    test = np.zeros((length_test, WIDTH * HEIGHT))


    cmpt_X = 0
    cmpt_test = 0
    cmpt_del_elem = 0

    for i in range(0, length):
        img = img_src[i]

        if i%10 == 0:
            test[cmpt_test] = img
            temp = img_id[i - cmpt_del_elem]
            img_id_test[cmpt_test] = temp
            img_id = numpy.delete(img_id, i - cmpt_del_elem, 0)
            cmpt_del_elem += 1
            cmpt_test += 1
        else:
            X[cmpt_X] = img
            cmpt_X += 1

    base_params = (WIDTH, HEIGHT, X, img_id, test, img_id_test, reversed_index, latex_index)

    #best_params = testParams.testParams(base_params)

    best_params = [[1020, 1020, 1020, 1020], 0, 500, 70]

    acc = trainNN.trainNN(base_params, best_params, True)

    print(best_params)


if train_NN:
    train()
else:
    folder_name = "Input"
    folders = [f for f in listdir(folder_name) if not isfile(join(folder_name, f))]

    for folder in folders:
        files = [f for f in listdir(folder) if isfile(join(folder, f))]

        letters_probabilities = []

        for file in files:
            img = scipy.ndimage.imread(file,
                                       flatten=False,
                                       mode='L') / 255
            img = img.flatten()

            letter_probabilities = trainNN.UseNN([img])
            letters_probabilities.append(letter_probabilities)

        wordConstruction(letters_probabilities)


