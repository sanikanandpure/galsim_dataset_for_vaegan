import yaml
import galsim

# Specify the path to your YAML configuration file
# config_file = '/u/spnand/vaegan-galsim/GalSim/examples/des/blend.yaml'

# # Load and parse the YAML configuration file
# config = galsim.config.ReadConfig(config_file)

with open('/u/spnand/vaegan-galsim/GalSim/examples/des/blend.yaml') as f:
    config = yaml.safe_load(f)
# Process the loaded configuration object to run the simulation
galsim.config.Process(config)
