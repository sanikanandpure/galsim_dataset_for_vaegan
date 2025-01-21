import galsim
import sys
import matplotlib.pyplot as plt

plt.switch_backend('Agg')

# Specify the path to your FITS file
fits_file = '/u/spnand/vaegan-galsim/GalSim/examples/des/output/galsim_fri_dataset_fits/blending_blending.fits'

# Read the FITS file into a GalSim Image
image = galsim.fits.read(fits_file)

# Convert the GalSim Image to a NumPy array
img_array = image.array

# Save the image as a PNG file
output_file = '/u/spnand/vaegan-galsim/GalSim/examples/des/output/galsim_fri_dataset_fits/blending_img1.png'
plt.imsave(output_file, img_array, cmap='gray')

#print(f'Image saved to {output_file}')

