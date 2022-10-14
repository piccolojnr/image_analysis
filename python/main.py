import os
import glob
import sys
from PIL import Image


for infile in sys.argv[1:]:
    e, f = os.path.splitext(infile)
    if f == ".jpg":
        try:
            with Image.open(infile) as im:
                upper = 0
                lower = im.width//4
                n = 0
                hh = (im.width, im.height)
                for i in range(4):
                    l = im.width//4
                    right = im.height//4
                    left = 0
                    for j in range(4):
                        box = (upper, left, lower, right)
                        region = im.crop(box)
                        outfile = f"images/img-{n}.jpg"
                        region.save(outfile)
                        print(box, "done", hh, outfile)
                        left += right
                        right += right
                        n += 1
                    upper += l
                    lower += l

        except OSError:
            print("cannot create thumbnail for", infile)
