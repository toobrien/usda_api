from mars   import mars_api
from json   import dumps
from sys    import argv


def s0(args = None):

    # print list of reports available from MARS api
    # this output includes the slug_ids needed for use with mars_api.get_report

    res = mars_api.get_reports()

    for row in res:

        print(f"{row['report_title']:100}{row['report_date']:20}{row['slug_id']}")


def s1(args):

    if not args:

        # print the report "Mid Missouri Stockyards Cattle Auction - Phillipsburg, MO"

        slug_id = 3654

    else:

        slug_id = args[0]

    res = mars_api.get_report(slug_id)

    for result in res["results"]:

        for key, val in result.items():

            if not val:

                result[key] = "null"

    print(dumps(res, indent = 2))


if __name__ == "__main__":

    sample = int(argv[1])
    args   = argv[2:]

    samples = {
        0: s0,
        1: s1
    }

    samples[sample](args)
