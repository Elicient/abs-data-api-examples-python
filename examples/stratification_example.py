import pandas as pd

import authenticate
import data
from examples.queries import stratifications as stratification_query
from stratification import stratify

bloomberg_deal_name = 'HART 2021-B'
asset_pool_id = 1

stratification_definitions = {
    "ltv": {
        "step": 0.01,
        "label": {
            "format": "percent",
            "scale": 0,
            "symbol": False
        },
        "buckets": [
            {
                "field": "LoanAssetOrigination.roundedLoanToValue",
                "max": 0.8
            },
            {
                "field": "LoanAssetOrigination.roundedLoanToValue",
                "min": 0.8,
                "max": 0.9
            },
            {
                "field": "LoanAssetOrigination.roundedLoanToValue",
                "min": 0.9,
                "max": 1.0
            },
            {
                "field": "LoanAssetOrigination.roundedLoanToValue",
                "min": 1.0,
                "max": 1.1
            },
            {
                "field": "LoanAssetOrigination.roundedLoanToValue",
                "min": 1.1,
                "max": 1.2
            },
            {
                "field": "LoanAssetOrigination.roundedLoanToValue",
                "min": 1.2,
                "max": 1.3
            },
            {
                "field": "LoanAssetOrigination.roundedLoanToValue",
                "min": 1.3,
                "max": 1.4
            },
            {
                "field": "LoanAssetOrigination.roundedLoanToValue",
                "min": 1.4,
                "max": 1.5
            },
            {
                "field": "LoanAssetOrigination.roundedLoanToValue",
                "min": 1.5
            }
        ]
    },
    "credit score": {
        "step": 1,
        "label": {
            "format": "number",
            "scale": 0,
            "separator": False
        },
        "buckets": [{
            "field": "DebtAssetOrigination.obligorHadCreditScore",
            "exactly": False,
            "label": "None"
        },
            {
                "field": "CreditScoreType.isCommercial",
                "exactly": True,
                "label": "Commercial"
            },
            {
                "field": "DebtAssetOrigination.obligorCreditScore",
                "max": 501
            },
            {
                "field": "DebtAssetOrigination.obligorCreditScore",
                "min": 501,
                "max": 551
            },
            {
                "field": "DebtAssetOrigination.obligorCreditScore",
                "min": 551,
                "max": 601
            },
            {
                "field": "DebtAssetOrigination.obligorCreditScore",
                "min": 601,
                "max": 651
            },
            {
                "field": "DebtAssetOrigination.obligorCreditScore",
                "min": 651,
                "max": 701
            },
            {
                "field": "DebtAssetOrigination.obligorCreditScore",
                "min": 701,
                "max": 751
            },
            {
                "field": "DebtAssetOrigination.obligorCreditScore",
                "min": 751,
                "max": 801
            },
            {
                "field": "DebtAssetOrigination.obligorCreditScore",
                "min": 801,
                "max": 851
            },
            {
                "field": "DebtAssetOrigination.obligorCreditScore",
                "min": 851
            }
        ]
    },
    "pti": {
        "step": 0.0001,
        "label": {
            "format": "percent",
            "scale": 2,
            "symbol": False
        },
        "buckets": [
            {
                "field": "NaturalPersonOrigination.roundedPaymentToIncome",
                "max": 0.07
            },
            {
                "field": "NaturalPersonOrigination.roundedPaymentToIncome",
                "min": 0.07,
                "max": 0.08
            },
            {
                "field": "NaturalPersonOrigination.roundedPaymentToIncome",
                "min": 0.08,
                "max": 0.09
            },
            {
                "field": "NaturalPersonOrigination.roundedPaymentToIncome",
                "min": 0.09,
                "max": 0.10
            },
            {
                "field": "NaturalPersonOrigination.roundedPaymentToIncome",
                "min": 0.10,
                "max": 0.11
            },
            {
                "field": "NaturalPersonOrigination.roundedPaymentToIncome",
                "min": 0.11,
                "max": 0.12
            },
            {
                "field": "NaturalPersonOrigination.roundedPaymentToIncome",
                "min": 0.12,
                "max": 0.13
            },
            {
                "field": "NaturalPersonOrigination.roundedPaymentToIncome",
                "min": 0.13,
                "max": 0.14
            },
            {
                "field": "NaturalPersonOrigination.roundedPaymentToIncome",
                "min": 0.14,
                "max": 0.15
            },
            {
                "field": "NaturalPersonOrigination.roundedPaymentToIncome",
                "min": 0.15
            }
        ]
    },
    "apr": {
        "step": 0.0001,
        "label": {
            "format": "percent",
            "scale": 2,
            "symbol": False
        },
        "buckets": [
            {
                "field": "LoanAssetCutoff.interestRate",
                "max": 0.01
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.01,
                "max": 0.02
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.02,
                "max": 0.03
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.03,
                "max": 0.04
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.04,
                "max": 0.05
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.05,
                "max": 0.06
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.06,
                "max": 0.07
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.07,
                "max": 0.08
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.08,
                "max": 0.09
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.09,
                "max": 0.10
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.10,
                "max": 0.11
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.11,
                "max": 0.12
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.12,
                "max": 0.13
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.13,
                "max": 0.14
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.14,
                "max": 0.15
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.15,
                "max": 0.16
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.16,
                "max": 0.17
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.17,
                "max": 0.18
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.18,
                "max": 0.19
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.19,
                "max": 0.20
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.20,
                "max": 0.21
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.21,
                "max": 0.22
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.22,
                "max": 0.23
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.23,
                "max": 0.24
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.24,
                "max": 0.25
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.25,
                "max": 0.26
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.26,
                "max": 0.27
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.27,
                "max": 0.28
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.28,
                "max": 0.29
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.29,
                "max": 0.30
            },
            {
                "field": "LoanAssetCutoff.interestRate",
                "min": 0.30
            },
        ]
    },
    "original term": {
        "label": {
            "format": "number",
            "scale": 0,
            "separator": False
        },
        "step": 1,
        "buckets": [
            {
                "field": "DebtAssetOrigination.originalTerm",
                "max": 13
            },
            {
                "field": "DebtAssetOrigination.originalTerm",
                "min": 13,
                "max": 25
            },
            {
                "field": "DebtAssetOrigination.originalTerm",
                "min": 25,
                "max": 37
            },
            {
                "field": "DebtAssetOrigination.originalTerm",
                "min": 37,
                "max": 49
            },
            {
                "field": "DebtAssetOrigination.originalTerm",
                "min": 49,
                "max": 61
            },
            {
                "field": "DebtAssetOrigination.originalTerm",
                "min": 61,
                "max": 73
            },
            {
                "field": "DebtAssetOrigination.originalTerm",
                "min": 73
            }
        ]
    }
}

stratification_measures = [
    {
        "name": "count",
        "type": "sum",
        "field": "Asset.count"
    },
    {
        "name": "balance",
        "type": "sum",
        "field": "LoanAssetCutoff.balanceSum"
    },
    {
        "name": "waFico",
        "type": "weightedAverage",
        "weightingField": "LoanAssetCutoff.balanceSum",
        "weightedField": "LoanAssetCutoff.weightedAverageObligorCreditScore"
    },
    {
        "name": "waApr",
        "type": "weightedAverage",
        "weightingField": "LoanAssetCutoff.balanceSum",
        "weightedField": "LoanAssetCutoff.weightedAverageInterestRateAtCutoff"
    },
    {
        "name": "waLtv",
        "type": "weightedAverage",
        "weightingField": "LoanAssetCutoff.balanceSum",
        "weightedField": "LoanAssetCutoff.weightedAverageLoanToValueAtCutoff"
    },
    {
        "name": "waPti",
        "type": "weightedAverage",
        "weightingField": "LoanAssetCutoff.balanceSum",
        "weightedField": "LoanAssetCutoff.weightedAveragePaymentToIncome"
    },
    {
        "name": "waOrigTerm",
        "type": "weightedAverage",
        "weightingField": "LoanAssetCutoff.balanceSum",
        "weightedField": "LoanAssetCutoff.weightedAverageOriginalTermAtCutoff"
    },
    {
        "name": "percentUsed",
        "type": "weightedAverage",
        "weightingField": "LoanAssetCutoff.balanceSum",
        "weightedField": "LoanAssetCutoff.percentUsed"
    }
]

def run_example():
    client = authenticate.get_authenticated_client()
    for stratification in stratification_definitions:
        df = pd.DataFrame(stratify(
            data.load(client, stratification_query(stratification_definitions[stratification], stratification_measures,
                                                   bloomberg_deal_name, asset_pool_id)),
            stratification_definitions[stratification], stratification_measures))
        print(stratification)
        print(df.to_markdown())
        print("\r\n\r\n")

run_example()