"""Relative strength test static data."""

import pandas as pd

STOCHASTIC_OSCILLATOR_EXPECTED_OUTPUT = {
    "%K": {
        pd.Timestamp("2023-01-03 00:00:00"): None,
        pd.Timestamp("2023-01-04 00:00:00"): None,
        pd.Timestamp("2023-01-05 00:00:00"): None,
        pd.Timestamp("2023-01-06 00:00:00"): None,
        pd.Timestamp("2023-01-09 00:00:00"): None,
        pd.Timestamp("2023-01-10 00:00:00"): None,
        pd.Timestamp("2023-01-11 00:00:00"): None,
        pd.Timestamp("2023-01-12 00:00:00"): None,
        pd.Timestamp("2023-01-13 00:00:00"): None,
        pd.Timestamp("2023-01-17 00:00:00"): None,
        pd.Timestamp("2023-01-18 00:00:00"): None,
        pd.Timestamp("2023-01-19 00:00:00"): None,
        pd.Timestamp("2023-01-20 00:00:00"): None,
        pd.Timestamp("2023-01-23 00:00:00"): 88.45950048405797,
        pd.Timestamp("2023-01-24 00:00:00"): 95.7434896331109,
        pd.Timestamp("2023-01-25 00:00:00"): 92.13358671466278,
        pd.Timestamp("2023-01-26 00:00:00"): 98.50210084199193,
        pd.Timestamp("2023-01-27 00:00:00"): 93.19726315940763,
        pd.Timestamp("2023-01-30 00:00:00"): 77.86501521487264,
        pd.Timestamp("2023-01-31 00:00:00"): 82.46866805333391,
        pd.Timestamp("2023-02-01 00:00:00"): 88.60035581307926,
        pd.Timestamp("2023-02-02 00:00:00"): 98.15581171018916,
        pd.Timestamp("2023-02-03 00:00:00"): 87.80175854146403,
        pd.Timestamp("2023-02-06 00:00:00"): 76.06942393387212,
        pd.Timestamp("2023-02-07 00:00:00"): 88.43705668888809,
        pd.Timestamp("2023-02-08 00:00:00"): 76.42484520501195,
        pd.Timestamp("2023-02-09 00:00:00"): 66.5810775456236,
        pd.Timestamp("2023-02-10 00:00:00"): 65.69731898991293,
        pd.Timestamp("2023-02-13 00:00:00"): 80.99085952059319,
        pd.Timestamp("2023-02-14 00:00:00"): 73.97254937729689,
        pd.Timestamp("2023-02-15 00:00:00"): 87.23534642967084,
        pd.Timestamp("2023-02-16 00:00:00"): 77.14820219893815,
        pd.Timestamp("2023-02-17 00:00:00"): 69.92526422602013,
        pd.Timestamp("2023-02-21 00:00:00"): 44.58274901473433,
        pd.Timestamp("2023-02-22 00:00:00"): 17.123285625983534,
        pd.Timestamp("2023-02-23 00:00:00"): 21.917710047209674,
        pd.Timestamp("2023-02-24 00:00:00"): 9.330871217841134,
        pd.Timestamp("2023-02-27 00:00:00"): 20.735125557823043,
        pd.Timestamp("2023-02-28 00:00:00"): 15.928391556899749,
    },
    "%D": {
        pd.Timestamp("2023-01-03 00:00:00"): None,
        pd.Timestamp("2023-01-04 00:00:00"): None,
        pd.Timestamp("2023-01-05 00:00:00"): None,
        pd.Timestamp("2023-01-06 00:00:00"): None,
        pd.Timestamp("2023-01-09 00:00:00"): None,
        pd.Timestamp("2023-01-10 00:00:00"): None,
        pd.Timestamp("2023-01-11 00:00:00"): None,
        pd.Timestamp("2023-01-12 00:00:00"): None,
        pd.Timestamp("2023-01-13 00:00:00"): None,
        pd.Timestamp("2023-01-17 00:00:00"): None,
        pd.Timestamp("2023-01-18 00:00:00"): None,
        pd.Timestamp("2023-01-19 00:00:00"): None,
        pd.Timestamp("2023-01-20 00:00:00"): None,
        pd.Timestamp("2023-01-23 00:00:00"): None,
        pd.Timestamp("2023-01-24 00:00:00"): None,
        pd.Timestamp("2023-01-25 00:00:00"): 92.1121922772772,
        pd.Timestamp("2023-01-26 00:00:00"): 95.45972572992189,
        pd.Timestamp("2023-01-27 00:00:00"): 94.61098357202077,
        pd.Timestamp("2023-01-30 00:00:00"): 89.85479307209073,
        pd.Timestamp("2023-01-31 00:00:00"): 84.5103154758714,
        pd.Timestamp("2023-02-01 00:00:00"): 82.97801302709529,
        pd.Timestamp("2023-02-02 00:00:00"): 89.74161185886744,
        pd.Timestamp("2023-02-03 00:00:00"): 91.51930868824415,
        pd.Timestamp("2023-02-06 00:00:00"): 87.3423313951751,
        pd.Timestamp("2023-02-07 00:00:00"): 84.10274638807475,
        pd.Timestamp("2023-02-08 00:00:00"): 80.31044194259071,
        pd.Timestamp("2023-02-09 00:00:00"): 77.14765981317454,
        pd.Timestamp("2023-02-10 00:00:00"): 69.56774724684949,
        pd.Timestamp("2023-02-13 00:00:00"): 71.08975201870992,
        pd.Timestamp("2023-02-14 00:00:00"): 73.55357596260102,
        pd.Timestamp("2023-02-15 00:00:00"): 80.7329184425203,
        pd.Timestamp("2023-02-16 00:00:00"): 79.4520326686353,
        pd.Timestamp("2023-02-17 00:00:00"): 78.10293761820971,
        pd.Timestamp("2023-02-21 00:00:00"): 63.8854051465642,
        pd.Timestamp("2023-02-22 00:00:00"): 43.877099622246,
        pd.Timestamp("2023-02-23 00:00:00"): 27.874581562642515,
        pd.Timestamp("2023-02-24 00:00:00"): 16.12395563034478,
        pd.Timestamp("2023-02-27 00:00:00"): 17.327902274291283,
        pd.Timestamp("2023-02-28 00:00:00"): 15.331462777521308,
    },
}