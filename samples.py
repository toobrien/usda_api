from    fas     import  fas_client
import  polars  as      pl
from    sys     import  argv


def s0():

    # get total US consumption for corn: between 2018 and 2022

    res = fas_client.get_commodity_data("ZC", 2018, 2022)

    if res:

        df = pl.from_dict(res)
        df = df.filter(
                (pl.col("CountryName")           == "United States")      &
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


if __name__ == "__main__":

    sample = int(argv[1])

    samples = {
        0: s0
    }

    samples[sample]()
