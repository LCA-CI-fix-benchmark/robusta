ffrom typing import Optional  # Add import statement for Optional type from typing module

TOKEN_LOCATION = '/var/run/secrets/kubernetes.io/serviceaccount/token'

def load_token() -> Optional[str]:
    # NOTE: This one will be mounted if openshift is enabled in values.yaml
    try:
        with open(TOKEN_LOCATION, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None  # Handle the case where the file is not found by returning None import Optional

TOKEN_LOCATION = '/var/run/secrets/kubernetes.io/serviceaccount/token'


def load_token() -> Optional[str]:
    # NOTE: This one will be mounted if openshift is enabled in values.yaml
    try:
        with open(TOKEN_LOCATION, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None
