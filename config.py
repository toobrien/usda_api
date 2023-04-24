

CONFIG = {

    # foreign agricultural service -- provides WASDE data, updated upon each release
    # https://apps.fas.usda.gov/psdonline/app/index.html#/app/about#G1

    "fas": {
        "api_key":  "<YOUR_API_KEY>",
        "endpoint": "https://apps.fas.usda.gov/PSDOnlineDataServices/api/"
    },

    # agricultural marketing service

    "mars": {
        "api_key":  "<YOUR_API_KEY>", 
        "endpoint": "https://marsapi.ams.usda.gov/services/v1.2/reports/{0}"
    }
}
