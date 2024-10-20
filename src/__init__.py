# __init__.py

import logging

# Set up a logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# You can also import configurations from other files if necessary
from config import API_KEY

# Optional: Expose modules or variables directly through the package
from cities import cities_portugal
