from timport openshift

# NOTE: This one will be mounted if openshift is enabled in values.yaml
try:
    # Add your code logic here
except Exception as e:
    # Handle exceptions here
    passing import Optional

TOKEN_LOCATION = '/var/run/secrets/kubernetes.io/serviceaccount/token'


def load_token() -> Optional[str]:
    # NOTE: This one will be mounted if openshift is enabled in values.yaml
    try:
        with open(TOKEN_LOCATION, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None
