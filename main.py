from hasy_tools import *
import numpy
import trainNN
import testParams

#able to "replay"
numpy.random.seed(7)

WIDTH, HEIGHT = 32, 32

index, latex_index = generate_index("hasy-data-labels2.csv")
print("index generated")

reversed_index = {}
for k, v in index.items():
    reversed_index[v] = k

(img_src, img_id) = load_images("hasy-data-labels2.csv", index)

print("images loaded")

X = np.zeros((len(img_id), WIDTH * HEIGHT))
for i in range(0, len(img_id)):
    img = np.zeros(WIDTH * HEIGHT)
    cmpt = 0

    for j in img_src[i]:
        for k in j:
            img[cmpt] = 1 if (k[0] > 1) else 0
            cmpt += 1

    X[i] = img

base_params = (WIDTH, HEIGHT, X, img_id, reversed_index, latex_index)


best_params = testParams.testParams(base_params)
print(best_params)
