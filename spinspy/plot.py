import matplotlib.pyplot as plt
import numpy as np
import collections

import isdim
import nearest_index

## plot: A top-level plotting function.
#    plot determines the dimensionality of
#    the desired plot object and calls
#    the appropriate plotting function to
#    do the actual plotting
def plot(var, time, xinds=None, yinds=None, zinds=None,
                    xvals=None, yvals=None, zvals=None,
                    xrels=None, yrels=None, zrels=None):
    
    # Determine the size of each dimension
    #   Any dimension that is left as None is assumed to 
    #   mean to plot the entire dimension
    if isdim('x'):
        xs = get_indices(xinds, xvals, xrels, Nx)
    if isdim('y')
        ys = get_indices(yinds, yvals, yrels, Ny)
    if isdim('z')
        zs = get_indices(zinds, zvals, zrels, Nz)

    num_dim = 0
    for sel in [xs,ys,zs]:
        if len(sel) > 1:
            num_dim += 1

    # Load the necessary data
    if n_sim_dim == 3:
        to_plot = reader(var,time,xs,ys,zs)
    elif not(isdim('z')):
        to_plot = reader(var,time,xs,ys)
    elif not(isdim('y')):
        to_plot = reader(var,time,xs,zs)
    elif not(isdim('x')):
        to_plot = reader(var,time,ys,zs)

    # Call the appropriate plotting tool
    if num_dim == 0:
        print('Bad! Only 1D')
    elif num_dim == 1:
        plot1d(X1,to_plot)
    elif num_dim == 2:
        plot2d(X1,X2,to_plot)
    elif num_dim == 3:
        print('Bad! 3D plotting not implemented')
    else:
        print('For some reason your data has more than three dimensions...')


# A helper function that parses the *inds, *vals, and *rels values.
def get_indices(inds,vals,rels,N): 
    if not(inds == None):
        if isinstance(inds, collections.Sequence):
            if inds[1] - 1 == inds[0]:
                returns [inds[0]]
            else:
                return inds
        else:
            return [inds]
    elif not(vals == None):
        if isinstance(vals, collections.Sequence):
            lower_ind = nearest_index(vals[0])
            upper_ind = nearest_index(vals[1])
            return [lower_ind, upper_ind]
        else:
            return [nearest_index(vals)]
    elif not(rels == None):
        if isinstance(vals, collections.Sequence):
            lower_ind = np.floor(rels[0]*N)
            upper_ind = np.ceil(rels[1]*N)
            return [lower_ind, upper_ind]
        else:
            return [int(rels*N)]
    else: # If all are none, assume plotting full thing
        return [0,-1]
