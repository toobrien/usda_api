from    fas     import  fas_api
from    fas     import  fas_client
from    json    import  dumps
import  polars  as      pl
from    sys     import  argv


def s0():

    # show total US consumption for corn: between 2018 and 2023

    res = fas_client.get_commodity_data("ZC", 2018, 2023)

    if res:

        df = pl.from_dict(res)
        df = df.filter(
                (pl.col("CountryName")           == "United States") &
                (pl.col("AttributeDescription")  == "Total Consumption")
            ).select(
                [
                    "CountryName",
                    "CommodityDescription",
                    "MarketYear",
                    "CalendarYear",
                    "Month",
                    "UnitDescription",
                    "Value"
                ]
            )

        print(df)


def s1():

    # show Armenian wheat production between 2015 and 2023

    res = fas_client.get_world_commodity_data("ZW", 2015, 2023)

    if res:

        df = pl.from_dict(res)
        df = df.filter(
                (pl.col("CountryName")          == "Armenia") &
                (pl.col("AttributeDescription") == "Production")
            ).select(
                [
                    "CountryName",
                    "CommodityDescription",
                    "MarketYear",
                    "CalendarYear",
                    "Month",
                    "UnitDescription",
                    "Value"
                ]
            )

        print(df)


def s2():

    # show all attributes

    recs = fas_api.attributes()

    if recs:

        for rec in recs:

            print(f"{rec['AttributeId']}\t{rec['AttributeName']}")


def s3():

    # show all commodities

    recs = fas_api.commodities()

    if recs:

        for rec in recs:

            print(f"{rec['CommodityCode']}\t{rec['CommodityName']}")


def s4():

    # show attributes available per commodity, as of 2023

    out = {}

    recs = fas_api.commodities()

    if recs:

        for rec in recs:

            commodity_code = rec["CommodityCode"]
            commodity_name = rec["CommodityName"].strip()
            
            cols = fas_client.get_commodity_data(commodity_code, 2023, 2023)

            if cols:

                df = pl.from_dict(cols)

                out[commodity_name] = {
                    "code":         commodity_code,
                    "attributes":   [
                                        row[0] 
                                        for row in df.select("AttributeDescription").unique().rows()
                                    ]
                }

    print(dumps(out, indent = 2))


if __name__ == "__main__":

    sample = int(argv[1])

    samples = {
        0: s0,
        1: s1,
        2: s2,
        3: s3,
        4: s4
    }

    samples[sample]()
