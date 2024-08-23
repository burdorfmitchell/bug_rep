# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import pyuvdata

filled=False

a=pyuvdata.UVData()
a.read_uvh5("ref_2.2_uvbeam_gleam_vot.uvh5")
a.conjugate_bls('ant1<ant2')
a.reorder_blts()

b=pyuvdata.UVData()
b.read_uvh5("ref_2.2_uvbeam_skyh5.uvh5")
b.conjugate_bls('ant1<ant2')
b.reorder_blts()

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(20,15), dpi=100)

ax.set_yscale("log")

histogram1 = np.histogram(np.abs(b.data_array), bins=50) #/np.abs(a.data_array), bins=500)
hist1, bins1 = histogram1
#print(hist1, bins1)
ax.stairs(hist1,bins1, fill=filled, label="new")

histogram2 = np.histogram(np.abs(a.data_array), bins=50) #/np.abs(a.data_array), bins=500)
hist2, bins2 = histogram2
#print(hist2, bins2)
ax.stairs(hist2,bins2, fill=filled, label="old")

#ax.stairs(hist2-hist1,bins2, fill=filled, label="old")

ax.set_xlabel("Amp [Jy]")
ax.set_ylabel("Counts")
ax.set_title("Abs")

ax.legend()

plt.savefig("hist_abs_ratio.png", bbox_inches="tight")
