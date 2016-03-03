import numpy as np;
#hack to get around mayavi qt issues
try:
    import tvtk.util.ctf
except ImportError:
    pass;
import math as m;
import matplotlib.pyplot as plt;
from matplotlib.colors import LogNorm;
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
G=6.67408e-11
quad = lambda a,b,c: ( (-float(b)+np.sqrt(float(b)**2-4*float(a)*float(c)))/(2*a), (-float(b)-np.sqrt(float(b)**2-4*float(a)*float(c)))/(2*a));
e0  = 8.854e-12
c=299792458
h=6.626070040e-34
e=1.602176208e-19
hc=h*c*1e9/e;
alpha = e**2/(4*np.pi*e0)/(h*c/(2*np.pi));
m_e=9.10938356e-31
mu0 = 4*np.pi*1e-7 
r_e = e**2/m_e/c**2/(4*np.pi*e0)
kb = 8.6173324e-5
a0 = lambda I,l=.8e-4: np.sqrt(r_e/c/m_e/(c**2)*2/np.pi * I * l**2)

debye = lambda T_eV, ne: np.sqrt(T_eV/(hc*1e-7)/(2*alpha)/ne)
nc = lambda l,gm=1,m=m_e,q=e: e0*m*(2*np.pi*c/l)**2/q**2/gm*1e-6 

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

def goagg():
    plt.change_backend('agg');
    
