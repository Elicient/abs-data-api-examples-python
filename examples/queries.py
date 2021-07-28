def deals_summary_statistics(shelves):
    """
    Given a list of shelves, returns a query to return summary statistics for all deals belonging to those shelves.
    :param shelves: An array of strings representing the Bloomberg deal names of the shelves to be included
    :return: Summary statistics for all deals in the given shelves.
    """
    return {
        "dimensions": ["Deal.name", "AssetPool.assetPoolId"],
        "order": [["Deal.name", "desc"]],
        "filters": [
            {
                "member": "Shelf.bloombergName",
                "operator": "equals",
                "values": shelves
            }
        ],
        "segments": ["AssetPool.securitizedAndPricing"],
        "measures": [
            "Asset.count",
            "LoanAssetCutoff.balanceAverage",
            "LoanAssetCutoff.weightedAveragePaymentToIncome",
            "LoanAssetCutoff.balanceSum",
            "LoanAssetCutoff.weightedAverageObligorCreditScore",
            "LoanAssetCutoff.percentNoCreditScore",
            "LoanAssetCutoff.weightedAverageLoanToValueAtCutoff",
            "LoanAssetCutoff.percentUsed",
            "LoanAssetCutoff.weightedAverageOriginalTermAtCutoff",
            "LoanAssetCutoff.weightedAverageRemainingTermAtCutoff",
            "LoanAssetCutoff.weightedAverageInterestRateAtCutoff"
        ]
    }


def stratifications(stratification_def, measures_def, bloomberg_deal_name, asset_pool_id=1):
    return {
        "dimensions": list(set([b["field"] for b in stratification_def["buckets"]])),
        "measures": list(set([val for sublist in
                              [[m["field"]] if "field" in m else [m["weightingField"], m["weightedField"]] for m in
                               measures_def] for val in sublist])),
        "filters": [
            {
                "member": "Deal.bloombergName",
                "operator": "equals",
                "values": [bloomberg_deal_name]
            },
            {
                "member": "AssetPool.assetPoolId",
                "operator": "equals",
                "values": [str(asset_pool_id)]
            }
        ]
    }
