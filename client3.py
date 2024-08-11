################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(stock):

    stock_name = stock['stock']
    bid_price = float(stock['bid_price'])
    ask_price = float(stock['ask_price'])
    price = (bid_price + ask_price) / 2
    return stock_name, bid_price, ask_price, price



def getRatio(price_a, price_b):

    if price_b == 0:
        return None
    return price_a / price_b



# Main
def main():
    
    for stock in stocks:  # Assuming 'stocks' is a list of stock dictionaries
        stock_name, bid_price, ask_price, price = getDataPoint(stock)
        print(f"Stock: {stock_name}, Bid: {bid_price}, Ask: {ask_price}, Price: {price}")

    # Assuming the list has exactly two stocks for ratio calculation
    price_a = getDataPoint(stocks[0])[3]
    price_b = getDataPoint(stocks[1])[3]
    ratio = getRatio(price_a, price_b)
    print(f"Ratio: {ratio}")

