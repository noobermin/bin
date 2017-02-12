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
try:
    import pys
except ImportError:
    pass;

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
e0  = 8.8541878176e-12
c=299792458
c_cgs = c*1e2
h=6.626070040e-34
e=1.602176208e-19
hc=h*c*1e9/e;
alpha = e**2/(4*np.pi*e0)/(h*c/(2*np.pi));
m_e=9.10938356e-31
m_p=1.672621898e-29
m_e_cgs= m_e *1e3
mu0 = 4*np.pi*1e-7 
r_e = e**2/m_e/c**2/(4*np.pi*e0)
kb = 8.6173324e-5
kb_si = 1.38064852e-23
a0 = lambda I,l=.8e-4: np.sqrt(r_e/c/m_e/(c**2)*2/np.pi * I * l**2)

debye = lambda T_eV, ne_invcc: np.sqrt(T_eV/(hc*1e-7)/(2*alpha)/ne_invcc)
nc = lambda l,gm=1,m=m_e,q=e: e0*m*(2*np.pi*c/l)**2/q**2/gm*1e-6
wp = lambda ne,q=e,m=m_e: np.sqrt(ne*e**2/m/e0)
ItoE = lambda I: np.sqrt(2*I*1e4/(e0*c));
EtoI = lambda E: e0*c*E**2/2.0*1e-4
def laserE(E_0, T, w,dim="3D"):
    '''
    Get total energy in a Gaussian Laser.
    

    Parameters and Keywords
    -----------------------
    E_0   -- Peak E field.
    T     -- FWHM of the pulse.
    w     -- Spotsize.
    dim   -- Spatial dimension, either "2D", or "3D" or None for "3D"

    Returns laser energy.
    '''

    if dim == "2D":
        return w * np.sqrt(np.pi/2) * (c*e0*E_0**2)/2 * T*1e-2;
    elif not dim or dim == "3D":
        return w**2 * (np.pi/2) * (c*e0*E_0**2)/2 * T;
    else:
        raise ValueError("dim is not None, '2D' or '3D'");


zr = lambda lm,w0: w0**2*np.pi/lm

waist = lambda z,lm,w0: w0*np.sqrt(1+(z/zr(lm,w0))**2)
spit=lambda n: "{:e}".format(n);

gm  = lambda b: 1.0/np.sqrt(1-b**2);
igm = lambda gm: np.sqrt(1.0-1.0/gm**2)
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
    
