import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageChops
import os
import numpy as np
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


im1 = Image.open(im1_path)
im2 = Image.open(im2_path)

return np.array(ImageChops.difference(im1, im2)).max()
