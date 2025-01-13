import logging

# import os
# import sys
from io import BytesIO, StringIO

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))
from scaleway_core.client import Client
from .custom_api import InstanceUtilsV1API

logger = logging.getLogger("scaleway")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# Create a client
client = Client(
    access_key="SCW1TKH1HKECKF6K68X5",
    secret_key="9034fb39-f48d-463a-9aa1-66f356077e05",
    default_project_id="d3520a52-2c75-4ba0-bda8-82dd087f07f2",
    default_region="fr-par",
    default_zone="fr-par-1",
)

# How to connect to Instance API
instanceClient = InstanceUtilsV1API(client)


# Create the server and attach the volume
instance_basic = instanceClient._create_server(
    commercial_type="DEV1-S",
    image="ubuntu_jammy",
    name="my-server-web",
    volumes={},  # Attach the volume to mount point "1"
)

key = "hello"
content = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10"  # Use bytes directly

# Set and get server user data
instanceClient.set_server_user_data(
    server_id=instance_basic.server.id, key=key, content=content
)
response = instanceClient.get_server_user_data(
    server_id=instance_basic.server.id, key=key
)

print(response.text)
