import os
import numpy as np
import matplotlib.pylab as plt
from skimage.io import imread
from VOClabelcolormap import color_map
from anno import ImageAnnotation


if __name__ == "__main__":
    fdir = 'examples'
    fname_anno = '2010_000145.mat'
    fname_im = '2010_000145.jpg'

    an = ImageAnnotation(
        os.path.join(fdir, fname_im),
        os.path.join(fdir, fname_anno))

    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    ax1.imshow(an.im)
    ax1.set_title('Image')
    ax1.axis('off')
    ax2.imshow(an.cls_mask, cmap=color_map(N=np.max(an.cls_mask) + 1))
    ax2.set_title('Class mask')
    ax2.axis('off')
    ax3.imshow(an.inst_mask, cmap=color_map(N=np.max(an.inst_mask) + 1))
    ax3.set_title('Instance mask')
    ax3.axis('off')
    if np.max(an.part_mask) == 0:
        ax4.imshow(an.part_mask, cmap='gray')
    else:
        ax4.imshow(an.part_mask, cmap=color_map(N=np.max(an.part_mask) + 1))
    ax4.set_title('Part mask')
    ax4.axis('off')
    plt.show()
