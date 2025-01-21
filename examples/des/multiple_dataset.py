import os
import yaml
import galsim

# Path to your original galsim YAML file
yaml_file = 'blend.yaml'
output_dir = '/u/spnand/vaegan-galsim/GalSim/examples/des/output/galsim_fri_dataset_fits'

# Make sure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Number of unique images to generate
n_images = 2000

# Load the original YAML file once
with open(yaml_file, 'r') as file:
    config = yaml.safe_load(file)

# Run GalSim for each unique image
for i in range(0, 10000):
    # Modify the random_seed in the YAML config
    config['image']['random_seed'] = 1000 + i  # Update seed for each run
    
    # Modify the output file name to ensure uniqueness
    config['output']['file_name'] = f"{output_dir}/blended_{i+1:03d}.fits"
    if 'deblend' in config['output']:
        config['output']['deblend']['file_name'] = f"{output_dir}/deblend_{i+1:03d}.fits"
    
    # Process the configuration directly with GalSim
    galsim.config.Process(config)
    
    print(f"Generated image {i+1} with random seed {1000 + i} and file name blended_{i+1:03d}.fits")
