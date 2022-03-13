# Visuals and Arts

## Image Analysis

Up to now we have mainly used this session to introduce how to produce visuals of data. This is important but there is also the analysis of images and other multimedia. Next, we talk therefore about a few simple exercises to work with images. We will see that basic image manipulation is actually quite simple because images are matrixes and can be manipulated just like any other matrix. You might remember matrixes from the introductions? If not, it is good to look them up again. They are similar to data frames but simpler. They contain only one type for all columns. In the case of images, these are pixel values.

First we load our standard libraries again. Run the code and observe that we also load imshow directly. We will use it to display our images.

#Keep cell
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import seaborn as sns
%matplotlib inline


Pillow (https://pypi.org/project/Pillow/) is the most commonly used library to process images. Load its image part with `from PIL import Image`.

from PIL import Image

Because we are from Amsterdam, we will work with the famous self-portrait of van Gogh. With PIL's `Image.open()`, we load an image. With requests, we ensure that we can read the image from a URL.

import requests

Gogh_re = requests.get('https://tinyurl.com/yntmv8z2', stream=True).raw

Gogh = Image.open(Gogh_re)

First, we need to understand what images actually are in the eye of the computer. As said, they are first and foremost matrixes containing pixel values. 

Colour images will also include Red-Green-Blue (RGB) information. These RGB channels quantify any colour. Check out https://www.tutorialspoint.com/python_pillow/python_pillow_colors_on_an_image.htm for a detailed explanation and especially the red, green and blue colour coding. A combination of RGB defines any colour for the human eye. This means we need to store all pixels of the image according to its height and width axes and this has to happen three times, because we need one matrix for each RGB colour channel. We need one matrix each for red, green and blue. This leads to a three-dimensional matrix: https://en.wikipedia.org/wiki/Channel_(digital_image).

Let's check it by running:
```
nGogh = np.array(Gogh)
np.shape(nGogh)
```

shape returns the shape of a numpy array.

nGogh = np.array(Gogh)
np.shape(nGogh)

As expected, vanGogh is a 3-dimensional numpy array. It is a 768 by 608 image (first 2 components of the array). The last dimension of this array is the channel with 3 values (1 for red, 2 for green, 3 for blue).

Let's use `imshow(nGogh)` to display this array as the actual image that it is.

imshow(nGogh)

That’s van Gogh. 

If we handle the image as a numpy array we can also manipulate it as we would a numpy array, by for example cropping it. An image crop reduces the width and height. You apply crops often if images are too large to handle. We can easily crop an image in Python by using the fact that it is an array. Try: 
```
crop = nGogh[100:400,100:400,:]
np.shape(crop)
```

crop = nGogh[100:400,100:400,:]
np.shape(crop)

Remember that images are matrixes of pixels! In this case, we cut out everything apart from pixels 100 to 400-1, leading to a 300 by 300 image. We kept all 3 colour channels by using the third comma with an ':'.

Let's take a look at crop with imshow. Do you know how?

imshow(crop)

Rotation of images is also a fun things to do. 
The relevant NumPy function is np.rot90(), so let us rotate the master with it. Check out the documentation how and then also display rotated_gogh by running the code below.

rotated_gogh = np.rot90(nGogh)
imshow(rotated_gogh)

Next we filter out the blue and the green colour channels so that we are left only with the red. This time we want to operate directly on the numpy array. So, first we make a copy with `red = nGogh.copy()`.

red = nGogh.copy()

How do we eliminate colours? Remember they are channels or the third dimension of our arrays. So, we just have to set green and blue to 0. The red channel is dimenions 0. Run `red[:,:,1] = 0 ` to set the green channel to 0.

red[:,:,1] = 0 # set green to zero

Can you also set the blue channel to 0? Hint: It is channel 2.

red[:,:,2] = 0 # set blue to zero

Please, display red.

imshow(red)

As an exercise, please create now a green image of vanGogh. You can do this in one piece of code below.

blue = nGogh.copy()
blue[:,:,0] = 0 # set red to zero
blue[:,:,2] = 0 # set blue to zero
imshow(blue)

Finally, we would like to produce a black and white van Gogh. A black and white image consists of a single pixel value for all RGB channels. For each of the channels, we simply need to calculate the average of all three colour channels. First, let us make a copy again with `BW = nGogh.copy()`.

BW = nGogh.copy()

Then, we calculate the average of all three RGB channels and assign it to the first channel, which is the red one. Numpy's mean does the job for us: https://numpy.org/doc/stable/reference/generated/numpy.mean.html. Wit axis=2, we indicate that we want to take the average of the other dimensions, which are the various pixel values. Run `BW = np.mean(BW, axis=2)` to create the average.

BW = np.mean(BW, axis=2)
np.shape(BW)

Run `imshow(BW, cmap = plt.get_cmap('gray'))` to tell Python to display the image in gray-scale mode.

imshow(BW, cmap = plt.get_cmap('gray'))

I think you got the idea that images are pixel matrixes/arrays based on colour channels that you can manipulate like any other matrix of numbers. Using this knowledge, you could analyse, for instance, digital images of paintings to find out whether they are by the same artist. Take a look at a Kaggle competition (https://www.kaggle.com/c/painter-by-numbers), which promises to develop an algorithm to detect art forgeries. The algorithm is supposed to assess with certainty that paintings are by van Gogh or not. For the competition, they use images freely available from https://www.wikiart.org/. You could also download a few from the site and apply your newly learned skills.