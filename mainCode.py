import time
import pandas as pd
import matplotlib.pyplot as plt

csv_in_use = "historicalData.csv"
date_column = "Date"
y_axis = "Close/Last"
# colors for plots
colour_1 = "#2596be"

# daily change = todays closing price - yesterdays closing price
def read_nordic_data():
    '''
    reads historicalData.csv file and parses the year column as a date and sets it as an index
    '''
   
    nordic_df = pd.read_csv(csv_in_use , parse_dates=[date_column],  index_col=date_column)
    return nordic_df

df = read_nordic_data()


def add_daily_price_change( column="Close/Last"):
    """
    """
    
    df["Daily Price Change"] = df[column].diff()
    return df

# def 

start = time.time()
df = add_daily_percentage_change()
sorted_df = df.sort_values(by=['Daily Price Change'])

end = time.time()
print(sorted_df)
print(f"It took you{end-start}seconds" )

# nordic_df = read_nordic_data()

# nordic_pct_change = nordic_df.pct_change
# print(nordic_pct_change)

# def add_daily_change_price():
#     pass




# start = time.time()
# input ("Type something and we will time it ")
# end =time.time()
# print(f"It took you{end-start}seconds" )
