import galsim

# Load and process the configuration file
config_file = 'blend.yaml'

# Use ProcessConfig to load the YAML file and run the simulation
galsim.config.ProcessConfig(config_file)
