# -*- coding: utf-8 -*-
"""
Created on Tue June 1, 2020
@author: Ni Chen
"""

import torch
import numpy as np

import math

np_dtype = np.float32
pt_dtype = torch.float32



# masked vectors to ndarray
def masked_to_full(x, idx, shape):
    img_full = torch.zeros(shape, dtype=torch.double).flatten()
    # img_full[np.r_[idx]] = x
    return img_full.reshape(shape)

