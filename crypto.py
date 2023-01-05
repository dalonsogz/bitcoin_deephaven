my_table = matches_table.drop_columns("type")

BTC = my_table.where("product_id == 'BTC-USD'")\
                  .format_row_where("size>0.25","DEEP_RED")
ETH = my_table.where("product_id == 'ETH-USD'")

large_BTC = my_table.where(["product_id == 'BTC-USD'","size>0.25"])

from deephaven.plot.figure import Figure

figure = Figure()

BTC_fig = figure.plot_xy(series_name="BTC-USD", t=BTC.reverse().tail(500), x="time", y="price").show()
ETH_fig = figure.plot_xy(series_name="ETH-USD", t=ETH.reverse().tail(500), x="time", y="price").show()

nanos_minute = 60_000_000_000
BTC_minute = BTC.select(["time","price"])\
                    .update("time = lowerBin(time,nanos_minute)")\
                    .avg_by("time")\
                    .rename_columns("BTC_price = price")

ETH_minute = ETH.select(["time","price"])\
                    .update("time = lowerBin(time,nanos_minute)")\
                    .avg_by("time")\
                    .rename_columns("ETH_price = price")

combo = BTC_minute.join(table=ETH_minute, on="time")
combo = combo.update(["ETH_BTC = ETH_price / BTC_price", "BTC_ETH = BTC_price / ETH_price"])
