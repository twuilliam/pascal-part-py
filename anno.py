import numpy as np
from scipy.io import loadmat
from skimage.io import imread
from skimage.measure import regionprops
from part2ind import get_pimap


PIMAP = get_pimap()


class ImageAnnotation(object):
    def __init__(self, impath, annopath):
        # read image
        self.im = imread(impath)
        self.impath = impath
        self.imsize = self.im.shape

        # read annotations
        data = loadmat(annopath)['anno'][0, 0]
        self.imname = data['imname'][0]
        self.annopath = annopath

        # parse objects and parts
        self.n_objects = data['objects'].shape[1]
        self.objects = []
        for obj in data['objects'][0, :]:
            self.objects.append(PascalObject(obj))

        # create masks for objects and parts
        self._mat2map()

    def _mat2map(self):
        ''' Create masks from the annotations
        Python implementation based on
        http://www.stat.ucla.edu/~xianjie.chen/pascal_part_dataset/trainval.tar.gz

        Read the annotation and present it in terms of 3 segmentation mask maps (
        i.e., the class maks, instance maks and part mask). pimap defines a
        mapping between part name and index (See part2ind.py).
        '''
        shape = self.imsize[:-1]  # first two dimensions, ignore color channel
        self.cls_mask = np.zeros(shape, dtype=np.uint8)
        self.inst_mask = np.zeros(shape, dtype=np.uint8)
        self.part_mask = np.zeros(shape, dtype=np.uint8)
        for i, obj in enumerate(self.objects):
            class_ind = obj.class_ind
            mask = obj.mask

            self.inst_mask[mask > 0] = i + 1
            self.cls_mask[mask > 0] = class_ind

            if obj.n_parts > 0:
                for p in obj.parts:
                    part_name = p.part_name
                    pid = PIMAP[class_ind][part_name]
                    self.part_mask[p.mask > 0] = pid


class PascalBase(object):
    def __init__(self, obj):
        self.mask = obj['mask']
        self.props = self._get_region_props()

    def _get_region_props(self):
        ''' useful properties
        It includes: area, bbox, bbox_Area, centroid
        It can also extract: filled_image, image, intensity_image, local_centroid
        '''
        return regionprops(self.mask)[0]


class PascalObject(PascalBase):
    def __init__(self, obj):
        super(PascalObject, self).__init__(obj)

        self.class_name = obj['class'][0]
        self.class_ind = obj['class_ind'][0, 0]

        self.n_parts = obj['parts'].shape[1]
        self.parts = []
        if self.n_parts > 0:
            for part in obj['parts'][0, :]:
                self.parts.append(PascalPart(part))


class PascalPart(PascalBase):
    def __init__(self, obj):
        super(PascalPart, self).__init__(obj)
        self.part_name = obj['part_name'][0]
