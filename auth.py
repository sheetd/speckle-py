from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_default_account

# load environment variables from .env.
from dotenv import load_dotenv
import os
load_dotenv()
speckle_token = os.getenv("speckle_token")

# initialise the client
client = SpeckleClient(host="conduit.aosm.app") # or whatever your host is
# client = SpeckleClient(host="localhost:3000", use_ssl=False) or use local server

# authenticate the client with a token
# account = get_default_account()
# client.authenticate_with_account(account)

# if you're in an environment without accounts, you can construct an Account object yourself
# or authenticate with just a token
client.authenticate_with_token(speckle_token)

# use that stream id to get the stream from the server
# new_stream = client.stream.get(id="a83d461d16")

# get list of commits
commits = client.commit.list("a83d461d16")
print(commits)