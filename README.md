This is a simple example demonstrating how to use a Python script to
programmatically access Elicient's new HTTP data API, a feature currently
in preview.

## Getting started
First, clone this repository to your local hard drive.

Once cloned, you must insert your **client_id** into the appropriate field within [config.py](config.py).
If you do not know your client_id, please contact us at [hello@elicient.com](mailto:hello@elicient.com).

It is recommended that you create and activate a new virtual environment before installing.  From within the project's
root folder, execute the following from a command line to create a new virtual environment named *env*:
```commandline
python -m venv venv
.\venv\Scripts\activate
```

Now install the project's requirements:
```commandline
pip install -r requirements.txt
```

You may now execute the example script:
```commandline
 python example.py
``` 

Upon running the example script for the first time, a web browser window will open requiring you to authenticate.  Once
you authenticate, a token will be stored in your user directory so you do not need to re-authenticate each time you
interact with the API.

## Rest API reference
Elicient's data API is located at [https://data.elicient.com/abs/v1](https://data.elicient.com/abs/v1) and exposes a few
useful endpoints:

### GET /meta
Returns all available cubes (tables) and their dimensions, measures, and segments.

A (truncated) example response:
```json
{
  "cubes": [
    {
      "name": "Asset",
      "title": "Asset",
      "description": "An individual asset belonging to at least one asset pool.",
      "connectedComponent": 1,
      "measures": [
        {
          "name": "Asset.count",
          "title": "Asset Count",
          "description": "The count of distinct assets.",
          "shortTitle": "Count",
          "cumulativeTotal": false,
          "cumulative": false,
          "type": "number",
          "aggType": "count",
          "drillMembers": [],
          "drillMembersGrouped": {
            "measures": [],
            "dimensions": []
          }
        },
        {
          "name": "Asset.earliestSeenInPeriod",
          "title": "Asset Earliest Seen in Period",
          "description": "The earliest period in which an asset was reported.",
          "shortTitle": "Earliest Seen in Period",
          "cumulativeTotal": false,
          "cumulative": false,
          "type": "number",
          "aggType": "min",
          "drillMembers": [],
          "drillMembersGrouped": {
            "measures": [],
            "dimensions": []
          }
        },
        {
          "name": "Asset.latestFirstSeenInPeriod",
          "title": "Asset Latest First Seen in Period",
          "description": "The latest period in which an asset was first reported.",
          "shortTitle": "Latest First Seen in Period",
          "cumulativeTotal": false,
          "cumulative": false,
          "type": "number",
          "aggType": "max",
          "drillMembers": [],
          "drillMembersGrouped": {
            "measures": [],
            "dimensions": []
          }
        }
      ],
      "dimensions": [
        {
          "name": "Asset.assetId",
          "title": "Asset Id",
          "type": "number",
          "description": "Uniquely identifies the asset.",
          "shortTitle": "Id",
          "suggestFilterValues": true,
          "format": "id"
        },
        {
          "name": "Asset.issuerAssignedAssetId",
          "title": "Asset Issuer assigned Id",
          "type": "string",
          "description": "Issuer-assigned value that uniquely identifies the asset within the deal.",
          "shortTitle": "Issuer assigned Id",
          "suggestFilterValues": true
        },
        {
          "name": "Asset.firstSeenInPeriod",
          "title": "Asset First Seen in Period",
          "type": "time",
          "description": "The first day of the reporting period in which this asset was first disclosed.",
          "shortTitle": "First Seen in Period",
          "suggestFilterValues": true
        }
      ],
      "segments": []
    }
  ]
}
```

### GET /load
Load accepts a single query parameter named `query`, which is a json object that may consist of the following properties:
* `measures`: An array of the names of the measures to be included in the query
* `dimensions`: An array of the names of the dimensions to be included in the query
* `filters`: An array of filter objects by which the query will be filtered
* `timeDimensions`: Any time dimensions by which data should be sliced
* `segments`: Segments by which the query should be filtered
* `limit`: The number of rows the query results should be limited to (*note: Currently it is not possible to return more
than 50,000 rows in a single request.  If you need to return more than 50,000 rows, please paginate your results using
both the `limit` and `offset` fields*)
* `offset`: The number of initial rows to be skipped.  Helpful when paginating results.
* `order`: A list of tuples containing the names of dimensions or arrays and directions by which the results should be
ordered.

Elicient's API is based on the [Cube.js](https://cube.dev/docs/query-format) data engine.  For specifics on formatting
queries, please refer to [Cube.js' query format documentation](https://cube.dev/docs/query-format). 

To see an example query, please refer to the code file [queries.py](examples/queries.py).