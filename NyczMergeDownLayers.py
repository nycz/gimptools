#!/usr/bin/env python2

from gimpfu import *


def merge_down_layers(image, layer, name):
    gimp.pdb.gimp_image_undo_group_start(image)
    # Make sure there is something to merge
    while len(image.layers) > 1:
        for l in image.layers[:-1]:
            if l.name.startswith(name):
                gimp.pdb.gimp_image_merge_down(image, l, NORMAL_MODE)
                break
        else:
            break
    gimp.pdb.gimp_image_undo_group_end(image)
    return

register(
    "nycz_merge_down_layers",
    "Merge down specific layers",
    "Merge down layers whose names begins with a specified string",
    "Nycz",
    "Nycz",
    "August 2015",
    "<Image>/Nycz/Merge down layers...",
    "RGBA*",
    [
        (PF_STRING, "name", "Layers to merge begins with:", "merge")
    ],
    [],
    merge_down_layers,
    )

main()
