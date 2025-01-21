import os
import galsim
import matplotlib.pyplot as plt

plt.switch_backend('Agg')

# Define the input directory and output directory
input_dir = '/u/spnand/vaegan-galsim/GalSim/examples/des/output/galsim_fri_dataset_fits'
output_dir = '/u/spnand/vaegan-galsim/GalSim/examples/des/output/galsim_fri_dataset_png'

# Make sure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
# List all FITS files in the input directory
fits_files = [f for f in os.listdir(input_dir) if f.endswith('.fits')]

# Process each FITS file
for fits_file in fits_files:
    # Create the full path to the FITS file
    fits_file_path = os.path.join(input_dir, fits_file)

    # Read the FITS file into a GalSim Image
    image = galsim.fits.read(fits_file_path)

    # Convert the GalSim Image to a NumPy array
    img_array = image.array

    # Define the output PNG file name
    output_file = os.path.join(output_dir, f'{os.path.splitext(fits_file)[0]}.png')

    # Save the image as a PNG file
    plt.imsave(output_file, img_array, cmap='gray')

    print(f'Image saved to {output_file}')
