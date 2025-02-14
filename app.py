

import pandas as pd
import numpy as np
import streamlit as st
import pickle
import plotly.graph_objects as go

# Load your data and save it as a pickle file
import pandas as pd
data = pd.read_excel("etherum_data.xlsx", parse_dates=['Date'])
data.to_pickle("data.pkl")


# Load  price data from pickle file
with open("data.pkl", "rb") as f:
    data = pickle.load(f)
data.set_index('Date', inplace=True)

# Debugging: Show dataset range
st.write(f"Minimum Close Price: {data['Close'].min()}")
st.write(f"Maximum Close Price: {data['Close'].max()}")

# Filter data for a specific price range
min_price = 1000  # Set your minimum price here
max_price = 35000  # Set your maximum price here
filtered_data = data[(data['Close'] >= min_price) & (data['Close'] <= max_price)]

if filtered_data.empty:
    st.error(f"No data available for the price range {min_price}-{max_price}. Please adjust the range.")
    st.write("Showing entire dataset as fallback:")
    st.write(data)
else:
    # Simulate Buy/Sell signals
    filtered_data['Buy_Entry'] = np.where(filtered_data['Close'] > filtered_data['Close'].rolling(10).mean(), 1, 0)
    filtered_data['Sell_Entry'] = np.where(filtered_data['Close'] < filtered_data['Close'].rolling(10).mean(), 1, 0)

    # Plot interactive Line chart
    st.title(f" Price Line Chart (Filtered: {min_price}-{max_price})")
    line_fig = go.Figure()

    # Add line graph for  price
    line_fig.add_trace(go.Scatter(
        x=filtered_data.index,
        y=filtered_data['Close'],
        mode='lines',
        name='Bitcoin Price Line',
        line=dict(color='blue', width=2)
    ))

# Mark Buy/Sell points for the Line chart
    line_fig.add_trace(go.Scatter(
        x=filtered_data[filtered_data['Buy_Entry'] == 1].index,
        y=filtered_data[filtered_data['Buy_Entry'] == 1]['Close'],
        mode='markers',
        name='Buy Signal',
        marker=dict(color='green', symbol='triangle-up', size=10)
    ))
    line_fig.add_trace(go.Scatter(
        x=filtered_data[filtered_data['Sell_Entry'] == 1].index,
        y=filtered_data[filtered_data['Sell_Entry'] == 1]['Close'],
        mode='markers',
        name='Sell Signal',
        marker=dict(color='red', symbol='triangle-down', size=10)
    ))

    # Customize layout for the Line chart
    line_fig.update_layout(
        title=f" Line Chart (Filtered: {min_price}-{max_price})",
        xaxis_title='Date',
        yaxis_title='Price',
        template='plotly_dark',
        xaxis_rangeslider_visible=False
    )

    # Display the Line chart
    st.plotly_chart(line_fig)

    # Plot interactive Candlestick chart
    st.title(f" Candlestick Chart (Filtered: {min_price}-{max_price})")
    candlestick_fig = go.Figure()

    # Add candlestick chart
    candlestick_fig.add_trace(go.Candlestick(
        x=filtered_data.index,
        open=filtered_data['Open'],
        high=filtered_data['High'],
        low=filtered_data['Low'],
        close=filtered_data['Close'],
        name='Candlestick',
    ))

    # Customize layout for the Candlestick chart
    candlestick_fig.update_layout(
        title=f" Candlestick Chart (Filtered: {min_price}-{max_price})",
        xaxis_title='Date',
        yaxis_title='Price',
        template='plotly_dark',
        xaxis_rangeslider_visible=False
    )

    # Display the Candlestick chart
    st.plotly_chart(candlestick_fig)
