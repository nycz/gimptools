#!/usr/bin/env python2

from gimpfu import *

from itertools import cycle

def parse_pattern(pattern, offset, end):
    if end <= offset:
        return []
    if '1' not in pattern:
        return []
    out = []
    for n, x in enumerate(cycle(pattern), offset):
        if n > end or n > 10000: #failsafe
            break
        if x == '1':
            out.append(n)
    return out


def mass_duplicate_layers(image, layer, pattern, offset, defaultend, lastlayer):
    pdb = gimp.pdb
    if offset < 0 or offset >= len(image.layers):
        return
    if not defaultend and layer == lastlayer:
        return
    pdb.gimp_image_undo_group_start(image)
    # Copy the old layer so counting will be easier
    newlayer = layer.copy()
    newlayer.name = layer.name
    image.remove_layer(layer)
    if defaultend:
        end = len(image.layers)
    else:
        end = image.layers.index(lastlayer)
    patternlist = parse_pattern(pattern, offset, end)
    for i in patternlist[::-1][:-1]:
        l = newlayer.copy()
        image.add_layer(l, i)
    image.add_layer(newlayer, offset)
    pdb.gimp_image_undo_group_end(image)
    return

register(
    "nycz_mass_duplicate_layers",
    "Mass duplicate layers",
    "Duplicate a layer and place it at specific intervals among the existing layers",
    "Nycz",
    "Nycz",
    "August 2015",
    "<Image>/Nycz/Mass duplicate layers...",
    "RGBA*",
    [
        (PF_STRING, "pattern", "Pattern (1 shows, 0 hides):", "1"),
        (PF_INT, "offset", "Offset to use:", 0),
        (PF_TOGGLE, "defaultend", "Ignore end point:", 1),
        (PF_LAYER, "lastlayer", "Last layer to use:", None),
    ],
    [],
    mass_duplicate_layers,
    )

main()
