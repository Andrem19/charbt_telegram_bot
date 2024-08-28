import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf
import os
import numpy as np

def save_candlesticks_pic(part1, part2, path1='post/question/pic_1.png', path2='post/answer/pic_2.png'):

    df1 = pd.DataFrame(part1, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df1['timestamp'] = pd.to_datetime(df1['timestamp'], unit='ms')
    df1.set_index('timestamp', inplace=True)
    
    combined_data = np.vstack((part1, part2))
    df2 = pd.DataFrame(combined_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df2['timestamp'] = pd.to_datetime(df2['timestamp'], unit='ms')
    df2.set_index('timestamp', inplace=True)
    
    binance_dark = {
        "base_mpl_style": "dark_background",
        "marketcolors": {
            "candle": {"up": "#3dc985", "down": "#ef4f60"},  
            "edge": {"up": "#3dc985", "down": "#ef4f60"},  
            "wick": {"up": "#3dc985", "down": "#ef4f60"},  
            "ohlc": {"up": "green", "down": "red"},
            "volume": {"up": "#247252", "down": "#82333f"},  
            "vcedge": {"up": "green", "down": "red"},  
            "vcdopcod": False,
            "alpha": 1,
        },
        "mavcolors": ("#ad7739", "#a63ab2", "#62b8ba"),
        "facecolor": "#1b1f24",
        "gridcolor": "#2c2e31",
        "gridstyle": "--",
        "y_on_right": True,
        "rc": {
            "axes.grid": True,
            "axes.grid.axis": "y",
            "axes.edgecolor": "#474d56",
            "axes.titlecolor": "red",
            "figure.facecolor": "#161a1e",
            "figure.titlesize": "x-large",
            "figure.titleweight": "semibold",
        },
        "base_mpf_style": "binance-dark",
    }
    
    mpf.plot(df1, type='candle', style=binance_dark, savefig=path1)
    
    mpf.plot(df2, type='candle', style=binance_dark, savefig=path2)
