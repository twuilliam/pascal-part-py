# pascal-part-py

Helpers in python to manipulate the annotations of the [Pascal-Part](http://www.stat.ucla.edu/~xianjie.chen/pascal_part_dataset/pascal_part.html) dataset.

## Usage

```python
an = ImageAnnotation(image_path, annotation_matrix_path)

an.im  # image

an.objects  # list of objects in the image
an.objects[0].parts  # list of parts that belong to the first object

an.objects[0].mask  # mask of the first object
an.objects[0].parts[0].mask  # mask of the first part of the first object
                             # (see part2ind.py for index encoding)

an.objects[0].props  # properties of the first object (e.g. bbox coordinates, centroid...)
an.objects[0].parts[0].props  # properties of the first part
                              # of the first object (e.g. bbox coordinates, centroid...)
```

## See also

[pascal-part-classes](https://github.com/tsogkas/pascal-part-classes)
