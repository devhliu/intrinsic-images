# Allen Ma 2019

import numpy as np 
import sys
import pyexr
import matplotlib
matplotlib.use("tkagg")
import matplotlib.pyplot as plt
import os.path
import cv2
import imageio

basepath = "/Volumes/gilmore/intrinsic-images/data/"

def ppm_to_numpy(fname):
    ''' reads in a ppm image and returns a numpy array'''
    if fname[-3:] != "ppm":
        print("Image {} is not ppm format".format(fname))
        raise(AssertionError)
    else:
        return plt.imread(fname)

def tiff_to_numpy(fname):
    ''' reads in a 16 bit tiff image and returns a numpy array of dtype float32'''
    if not (fname.lower().endswith("tiff") or fname.lower().endswith("tif") ) :
        print("Image {} is not tiff format".format(fname))
        raise(AssertionError)
    else:
        # 16 bit, linear, preserve rgb channel
        img = cv2.imread( fname, -1 )
        # convert bgr to rgb
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

def numpy_to_exr(img, out_name):
    ''' converts numpy arr to exr file 
        img - numpy arr
        out_name - the output filename
    '''
    imageio.imwrite(f'{out_name}.exr', img)

def convert_save_tiff_npy(basepath, outpath):

    # for 16 bit images
    max_val = 2**16 - 1
 
    count = 0
    for d in os.listdir(basepath):
        fname = os.path.join(basepath, d)
        out_name = d[:-5]
        if fname.lower().endswith(".tiff"):
            out_name = d[:-5]
        elif fname.lower().endswith(".tif"):
            out_name = d[:-4]
        else:
            print(f"{d} is not a tiff file")
            continue
        img = tiff_to_numpy(fname)
        img = img.astype(np.float32)
        img /= max_val
        assert(np.max(img) <= 1.0 and np.min(img) >= 0.0)
        output_fname = os.path.join(outpath, out_name)
        np.save(output_fname, img)
        count += 1
    print(f"total: {count} converted")

def convert_save_ppm_npy(basepath, outpath):
    max_val = 2**8 - 1
    count = 0
    for d in os.listdir(basepath):
        fname = os.path.join(basepath, d)
        if fname.lower().endswith(".ppm"):
            out_name = d[:-4]
        else:
            print(f"{d} is not a ppm file")
        img = ppm_to_numpy(fname)
        img = img.astype(np.float32)
        img /= max_val
        assert(np.max(img) <= 1.0 and np.min(img) >= 0.0)
        output_fname = os.path.join(outpath, out_name)
        np.save(output_fname, img)
        count += 1
    print(f"total: {count} converted")


def main(argv):
    basepath = argv[1]
    outpath = argv[2]
    convert_save_ppm_npy(basepath, outpath)

if __name__ == "__main__":
    main(sys.argv)


