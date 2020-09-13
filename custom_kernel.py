from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


image_name = input("Enter image path(relative or full): ")

im = Image.open(image_name)
arr = np.array(im)

kernel_size = int(input("Enter kernel size: "))

kernel = []
for i in range(kernel_size ** 2):
    kernel.append(int(input()))

filt = np.array(kernel)
filt = filt.reshape(kernel_size, kernel_size)


def apply_filter(arr, filt):
    filt = np.expand_dims(filt, 2)
    # print(filt.shape)
    filter_size = filt.shape[0]
    ret = np.zeros((arr.shape[0]-filter_size + 1,
                    arr.shape[1]-filter_size + 1, 4))
    # print(arr[0:0+filter_size, 0:0+filter_size].shape)
    # print(arr[0:0+filter_size, 0:0+filter_size, 0:4]*filt)
    # print(np.round(np.sum(np.sum(arr[0:0+filter_size,0:0+filter_size,0:3]*filt,axis=0,keepdims=True),axis=1,keepdims=True)))
    for i in range(ret.shape[0]):
        for j in range(ret.shape[1]):
            ret[i, j, :] = np.round(
                np.sum(np.sum(arr[i:i+filter_size, j:j+filter_size, :]*filt, axis=0), axis=0))
            # ret[i,j,3] = np.round(np.sum(np.sum(arr[i:i+filter_size,j:j+filter_size,3]*filt,axis=0),axis=0))
            # ret[i, j, 3] = 255
    ret = ret.astype('int')
    return ret


output = apply_filter(arr, filt)


output_image = Image.fromarray(output)

output_image = output_image.save("custom_kernel_output.jpg")
