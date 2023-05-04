from config     import CONFIG
from requests   import get


API_KEY     = CONFIG["mars"]["api_key"]
ENDPOINT    = CONFIG["mars"]["endpoint"]
AUTH        = ("", API_KEY)


def get_reports():

    res = get(ENDPOINT + "/reports", auth = AUTH)
    res = res.json()

    return res


def get_report(slug_id: str):

    res = get(ENDPOINT + f"/reports/{slug_id}", auth = AUTH)
    res = res.json()

    return res
