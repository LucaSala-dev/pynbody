import sys
import time

import numpy as np

import pynbody

np.random.seed(1337)

Npart = 10000000
Ntrials = 20

centres = np.random.uniform(size=(Ntrials,3)) - 0.5
radii = 10.**np.random.uniform(low=-3.0,high=-1.0,size=Ntrials)

f = pynbody.new(dm=Npart)

f['pos'] = np.random.uniform(size=(Npart,3))
f['pos'] -= 0.5

start = time.time()
for cen, rad in zip(centres, radii):
    print(".",end="")
    sys.stdout.flush()
    f[pynbody.filt.Sphere(rad, cen)]

end = time.time()

print("no tree time:", end - start)

pynbody.sph.build_tree(f)

start = time.time()
for cen,rad in zip(centres,radii):
    print(".", end="")
    sys.stdout.flush()
    f[pynbody.filt.Sphere(rad, cen)]


end = time.time()

print("with tree time:",end - start)
