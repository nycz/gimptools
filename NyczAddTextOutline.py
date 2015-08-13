#!/usr/bin/env python2

from gimpfu import *

## WORKFLOW
#
# Right-click on layer -> alpha to selection
# Grow selection by 1 pixel
# Make a new empty layer
# Fill selection with black
# Move new layer below old layer
# Merge down old layer


def add_text_outline(image, layer):
    gimp.pdb.gimp_image_undo_group_start(image)
    layer_name = layer.name
    gimp.pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, layer)
    if gimp.pdb.gimp_selection_is_empty(image):
        return
    gimp.pdb.gimp_selection_grow(image, 1)
    new_layer = gimp.Layer(image, 'outline', image.width, image.height, RGBA_IMAGE, 100, NORMAL_MODE)
    top_pos = image.layers.index(layer)
    image.add_layer(new_layer, top_pos+1)
    gimp.pdb.gimp_edit_fill(new_layer, BACKGROUND_FILL)
    gimp.pdb.gimp_selection_none(image)
    final_layer = gimp.pdb.gimp_image_merge_down(image, layer, NORMAL_MODE)
    final_layer.name = layer_name
    gimp.pdb.gimp_image_undo_group_end(image)
    return

register(
    "nycz_add_text_outline",
    "Add black outline to a text layer",
    "Add black outline to a text layer",
    "Nycz",
    "Nycz",
    "August 2015",
    "<Image>/Nycz/Outline text",
    "RGBA*",
    [],
    [],
    add_text_outline,
    )

main()
