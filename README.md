# Intrinsic Image Decomposition

- The overall goal of our summer research is to determine whether raw images perform better at the task of intrinsic image decomposition

- We define an intrinsic image as follows, definition from [here](http://www-oldurls.inf.ethz.ch/personal/pomarc/courses/CompPhoto/cpv07.pdf)
    - the illumination map is the lighting having irrespective of surface material?
    - what is the surface reflectance, irrespective of lighting?

Work sponsored by Colby College Computer Science Department

Members:
Mike Fu
Allen Ma
Professor Bruce Maxwell

Acknowledgments:
Shafat Rahman
Maan Qraitem
Casey Smith



# Explanation of data directory

* data
    * **mmap**; material maps (8000)
        * **mmap_npy**; 512x512 material maps in numpy array form
        * **mmap_real_cr2**; Canon raw, uncropped images of material maps
        * **mmap_real_npy**; uncropped raw material images converted into numpy arrays from 16-bit (linear) tiff
        * **mmap_real_tiff**; 16-bit linear tiffs of the Canon raw images
        * **mmap_synthetic**; 512x512 ppms generated using Bruce's C code
    * **imap**; illumination map (40000 of each)
        * **imap_npy**; 512x512 illumination maps
        * **imap_npy_ambient**; 512x512 ambient illumination maps
        * **imap_npy_direct**; 512x512 direct illumination maps
        * **imap_real_cr2**; Canon raw, uncropped images of illumination maps
        * **imap_real_npy**; uncropped raw illumination images converted into numpy arrays from 16-bit (linear) tiff
        * **imap_real_tiff**; 16-bit linear tiffs of the Canon raw images
