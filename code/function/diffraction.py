# -*- coding: utf-8 -*-
"""
Created on Tue June 1, 2020
@author: Ni Chen
"""

import math

import numpy as np
import torch

np_dtype = np.float32
pt_dtype = torch.float32


class PropParam:
    def __init__(self):
        self.wavelen = 500e-9
        self.pps = 2e-6
        self.z = torch.nn.Parameter(torch.tensor([10], dtype=torch.float32, requires_grad=True))

'''
Propagation kernel
'''
def prop_kernel(params, pad_ratio=1):
    params.pad_ratio = pad_ratio
    pps = params.pps
    wavelen = params.wavelen
    z = params.z

    Ny = params.Ny
    Nx = params.Nx

    Lx = Nx * pps
    Ly = Ny * pps
    dfx = torch.as_tensor(1 / Lx)
    dfy = torch.as_tensor(1 / Ly)

    x_range = torch.arange(0, Nx, 1) - np.round((Nx-1) / 2)
    y_range = torch.arange(0, Ny, 1) - np.round((Ny-1) / 2)

    Fx = x_range * dfx
    Fy = y_range * dfy
    fx, fy = torch.meshgrid(Fx, Fy)

    k = 2 * math.pi / wavelen
    params.otf = torch.exp(1j* k * z) * torch.exp(-1j* wavelen * math.pi * z * (fx ** 2 + fy ** 2))

    return params


'''
Forward wave field propagation. Propagate a 3D object to a 2D hologram.
'''
def forward_wave_prop(field_in, params):
    return iFT2(FT2(field_in)*params.otf.to(field_in.device))


'''
Backward wave field propagation. Propagate a 2D hologram to a 3D volume.
'''
def backward_wave_prop(field_in, params):
    return iFT2(FT2(field_in) * torch.conj(params.otf.to(field_in.device)))


def FT2(field_in, pps=1):
    Ny, Nx = field_in.shape
    x_range = torch.linspace(0, Nx - 1, Nx).to(field_in.device)
    y_range = torch.linspace(0, Ny - 1, Ny).to(field_in.device)

    y, x = torch.meshgrid(y_range, x_range, indexing='ij')

    shift_phase = torch.exp(1j * math.pi * (x + y))

    return torch.fft.fft2(shift_phase * field_in)*shift_phase * pps**2

def iFT2(field_in, ppf=1):
    Ny, Nx = field_in.shape
    x_range = torch.linspace(0, Nx - 1, Nx).to(field_in.device)
    y_range = torch.linspace(0, Ny - 1, Ny).to(field_in.device)

    y, x = torch.meshgrid(y_range, x_range, indexing='ij')

    shift_phase = torch.exp(-1j * math.pi * (x + y))

    return torch.fft.ifft2(shift_phase * field_in) * shift_phase / (ppf**2)