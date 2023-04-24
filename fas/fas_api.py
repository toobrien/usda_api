from    usda_api.config import  CONFIG
from    requests        import  get


# https://apps.fas.usda.gov/psdonline/app/index.html#/app/about#G1


API_KEY     = CONFIG["fas"]["api_key"]
ENDPOINT    = CONFIG["fas"]["endpoint"] 
HEADERS     = { 
    "Accept":   "application/json",
    "API_KEY":  API_KEY
}


def make_request(path: str, query_params: dict = None):

    kwargs = {
        "url":      ENDPOINT + path,
        "headers":  HEADERS
    }

    if query_params:

        kwargs["params"] = query_params

    res = get(**kwargs)

    if res.status_code != 200:

        print(f"{path:50}", res.status_code)

        return None

    else:

        return res.json()


# CommodityData route


def commodity_data_by_year(
    commodity_code: str, 
    market_year:    int
):

    path            = "/CommodityData/GetCommodityDataByYear"
    query_params    = {
        "commodityCode":    commodity_code,
        "marketYear":       market_year
    }

    res = make_request(path, query_params)

    return res


def world_commodity_data_by_year(
    commodity_code: str,
    market_year:    int
):

    path            = "/CommodityData/GetCommodityDataByYear"
    query_params    = {
        "commodityCode":    commodity_code,
        "marketYear":       market_year
    }

    res = make_request(path, query_params)

    return res


# LookupData route


def regions():

    path    = "/LookupData/GetRegions"
    res     = make_request(path)

    return res


def countries():

    path    = "/LookupData/GetCountries"
    res     = make_request(path)

    return res


def commodities():

    path    = "/LookupData/GetCommodities"
    res     = make_request(path)

    return res


def attributes():

    path    = "/LookupData/GetAttributes"
    res     = make_request(path)

    return res


def units_of_measure():

    path    = "/LookupData/GetUnitsOfMeasure"
    res     = make_request(path)

    return res