import authenticate
import data
from examples import queries
import pandas as pd

def run_example():
    # get an authenticated client we can use to call the api
    client = authenticate.get_authenticated_client()

    # list out all available fields for us to reference
    print(data.meta(client))

    # load summary statistics for all of SDART's deals into pandas data frames
    df = pd.DataFrame(data.load(client, queries.deals_summary_statistics(['SDART'])))
    print(df)

run_example()



