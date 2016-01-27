import numpy as np;
#hack to get around mayavi qt issues
try:
    import tvtk.util.ctf
except ImportError:
    pass;
import math as m;
import matplotlib.pyplot as plt;
import cPickle as pickle;
def importcwd():
    import sys;
    sys.path.insert(0,'.');
import re
import h5py as h5
mkdeg = lambda f,th: f(float(th)/180*np.pi);
sind = lambda th: mkdeg(np.sin,th);
cosd = lambda th: mkdeg(np.cos,th);
tand = lambda th: mkdeg(np.tan,th);
mkretdeg = lambda f,x: f(x)/np.pi*180;
arccosd = lambda th: mkretdeg(np.arccos,th);
arcsind = lambda th: mkretdeg(np.arcsin,th);
arctand = lambda th: mkretdeg(np.arctan,th);

g=9.8
G=6e-11
quad = lambda a,b,c: ( (-float(b)+np.sqrt(float(b)**2-4*float(a)*float(c)))/(2*a), (-float(b)-np.sqrt(float(b)**2-4*float(a)*float(c)))/(2*a));
e0 = 8.854e-12

def readfile(fname):
    if re.match(r".*\.h5",fname):
        return h5.File(fname);
    return np.load(fname,allow_pickle=True);

def savefile(fname, data):
    with open(fname,'w') as f:
        pickle.dump(data,f,2);
    pass;

def plot(*args,**kwargs):
    plt.plot(*args,**kwargs);
    plt.show();

def scatter(*args,**kwargs):
    plt.scatter(*args,**kwargs);
    plt.show();
