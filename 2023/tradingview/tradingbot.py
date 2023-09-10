from tradingview_ta import TA_Handler, Interval, Exchange
import time

# Store the last order.
last_order = "sell"

# Instantiate TA Handler.
handler = TA_Handler (
    symbol="TSLA",
    exchange="NASDAQ",
    screener="america",
    interval=Interval.INTERVAL_1_DAY
)

# Repeat Forever.
while True:
    # Retrieve recommendation.
    rec = handler.get_analysis()["RECOMMENDATION"]

    # create buy order if the recommendation is 'buy' or 'strong buy' and the last order is 'sell'.
    # create a sell order if the recommendation is 'sell' and 'strong sell' and the last order is 'buy'.
    if "BUY" in rec and last_order == "sell":
        # Replace Comment: Create a buy order using the exchange's API.
        last_order = "buy"

    elif "sell" in rec and last_order == "buy":
        last_order = "sell"
    
    time.sleep(20)

