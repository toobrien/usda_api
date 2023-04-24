from fas import fas_api


sym_to_code = {
    "LE":   "0011000",  # "animal numbers, cattle"  cme     live cattle
    "GF":   "0011000",  # "animal numbers, cattle"  cme     feeder cattle
    "HE":   "0013000",  # "animal numbers, swine"   cme     live hogs
    "KC":   "0711100",  # "coffe, green"            ice     coffee c
    "ZC":   "0440000",  # "corn"                    cbot    corn
    "CT":   "2631000",  # "cotton"                  ice     cotton #2
    "CB":   "0230000",  # "dairy, butter"           cme     cash-settled butter
    "CSC":  "0240000",  # "dairy, cheese"           cme     cash-settled cheese
    "DC":   "0223000",  # "dairy, milk, fluid"      cme     class iii milk
    "GNF":  "0224200",  # "dairy, milk, nonfat dry" cme     nonfat dry milk
    "ZM":   "0813100",  # "meal, soybean"           cbot    soybean meal
    "ZO":   "0452000",  # "oats"                    cbot    oats
    "CPO":  "4243000",  # "oil, palm"               cme     malaysian crude palm oil
    "ZL":   "4232001",  # "oil, soybean (local)"    cbot    soybean oil
    "ZS":   "2222000",  # oilseed, soybean          cbot    soybean
    "OJ":   "0585100",  # orange juice              ice     frozen concentrated orange juice
    "ZR":   "0422110",  # rice, milled              cbot    rough rice
    "ZW":   "0410000",  # wheat                     cbot    chicago wheat
    "KE":   "0410000",  # wheat                     cbot    kansans wheat
}


def get_commodity_data(symbol_or_code: str, start: int, end: int):

    code = symbol_or_code

    if len(symbol_or_code) < 7:

        code = sym_to_code[symbol_or_code]

    recs = []

    for year in range(start, end + 1):

        res = fas_api.commodity_data_by_year(code, year)

        if res:

            recs.extend(res)

    cols = {}

    for rec in recs:

        for key, val in rec.items():

            if key not in cols:

                cols[key] = []

            cols[key].append(val.strip() if type(val) == str else val)

    return cols