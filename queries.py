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
