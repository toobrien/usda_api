from config     import CONFIG
from requests   import get


API_KEY     = CONFIG["mars"]["api_key"]
ENDPOINT    = CONFIG["mars"]["endpoint"]


def get_reports():

    res = get(ENDPOINT + "/reports", auth = ("", API_KEY))
    res = res.json()

    return res


def get_report(slug_id: str):

    res = get(ENDPOINT + f"/reports/{slug_id}", auth = ("", API_KEY))
    res = res.json()

    return res
