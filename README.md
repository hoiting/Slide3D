# Slide3D
Slide3D is a Python tool for visualising the emission line fit produced by LZIFU. 

![Slide3D ScreenShot1](https://github.com/hoiting/Slide3D/blob/master/ScreenShot1.png)
![Slide3D ScreenShot2](https://github.com/hoiting/Slide3D/blob/master/ScreenShot2.png)


## Dependencies
The following python modules are required 
* [numpy](http://www.numpy.org/), [scipy](https://www.scipy.org/)
* [astropy](http://www.astropy.org/)
* [pyqtgraph](http://www.pyqtgraph.org/)

## Installation
Change the first line in slide3d.py to the python path on your machine. Place slide3d.py under your PATH. In shell:
```
>>> slid3d.py -c [configuration file] 
              -p [path to data = ./] 
              -z [redshift = 0.05 or from Z_LZIFU in LZIFU_CUBE_FILE header0] 
              -s [scale factor = 1. normally not required.]
              -h [= --help] -v [= --version]
               B_CUBE_FILE R_CUBE_FILE LZIFU_CUBE_FILE  (for 2-sided data)
               or 
               CUBE_FILE LZIFU_CUBE_FILE (for 1-sided data)
               FILE can be .fits or .fits.gz (slower to launch)
```
## Configuration file
A template is provided as slide3d.config. The configuration file describes what to display in the 8 subpanels (p1 - p8). The configuration file should following the following format
```
# panel (p1 - p8),EXTNAME (from LZIFU LINELIST)
```


For questions, please drop an email to iting@mpia.de