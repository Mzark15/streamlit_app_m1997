
# import streamlit as st
# import yfinance as finance

# st.write(
#     """
#     # Stock Price Analyzer
    
#     Shown are stock prices of Apple
#     """
# )

# # Define the stock symbol
# symbol = "AAPL"

# # Fetch historical stock data
# stock_data = finance.download(symbol, start="2022-01-01", end="2022-12-31")

# # Display the stock data in a table
# st.write("## Stock Data:")
# st.write(stock_data)
import pandas as pd
import streamlit as st
import yfinance as yf
import  datetime

ticker_symbol = st.text_input("Enter stock symbol",
                              "AAPL",
                              key="placeholder")

col1,col2=st.columns(2)

## Start with Analysis
with col1:
    
    start_date=st.date_input("Input Start Date",
                             datetime.date(2024,1,1))
##End with Analysis
with col2:
    
    End_date=st.date_input("Input End Date",
                            datetime.date(2024,2,5))

st.write(
    """
    # Stock Price Analyzer
    
    Shown are stock prices of Apple
    """
)


ticker_data = yf.Ticker(ticker_symbol)

ticker_df = ticker_data.history(period="1d",

start=start_date,

end=End_date)

st.write(f"""## {ticker_symbol}'s EOD prices""")

st.dataframe(ticker_df)
st.write("""
         ## Daily closing chart
         """)
st.line_chart(ticker_df.Close)

# Additional Graph: Volume Traded
# st.write("## Volume Traded")
# st.bar_chart(ticker_df.Volume)
# Additional Graph: Volume Traded
st.write("## Volume Traded")
st.bar_chart(ticker_df.Volume, use_container_width=True, height=400, color='#FFA500')
# Additional Graph: Volume Traded
# st.write("## Volume Traded")
# st.bar_chart(ticker_df.Volume, use_container_width=True, height=400, color='orange')
# Define the stock symbol
# symbol = "AAPL"

# # Fetch historical stock data
# stock_data = finance.download(symbol, start="2022-01-01", end="2022-12-31")

# # Display the stock data in a table
# st.write("## Stock Data:")
# st.write(stock_data)

# # Plot trends for a particular time range
# st.write("## Stock Trends:")
# selected_start_date = st.date_input("Select Start Date:", min_value=stock_data.index.min(), max_value=stock_data.index.max())
# selected_end_date = st.date_input("Select End Date:", min_value=stock_data.index.min(), max_value=stock_data.index.max())

# selected_data = stock_data.loc[selected_start_date:selected_end_date]

# # Plotting trends
# st.line_chart(selected_data['Close'])

# Additional analysis or statistics can be added here

