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

length = len(img_id)
length_test = int(0.1 * length) + 1

img_id_test = np.zeros((length_test, len(img_id[0])))
X = np.zeros((length - length_test, WIDTH * HEIGHT))
test = np.zeros((length_test, WIDTH * HEIGHT))


cmpt_X = 0
cmpt_test = 0
cmpt_del_elem = 0

for i in range(0, length):
    img = np.zeros(WIDTH * HEIGHT)
    cmpt_base = 0
    for j in img_src[i]:
        for k in j:
            img[cmpt_base] = 1 if (k[0] > 1) else 0
            cmpt_base += 1

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

best_params = testParams.testParams(base_params)
print(best_params)
