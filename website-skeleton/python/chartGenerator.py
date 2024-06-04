import yfinance as yf
import plotly.graph_objs as go


def make_graph(ticker,start,end):
  # Download Apple stock data
  apple = yf.download(ticker, start=start, end=end)

  # Create a Candlestick chart
  fig = go.Figure(data=[go.Candlestick(x=apple.index,
                                      open=apple['Open'],
                                      high=apple['High'],
                                      low=apple['Low'],
                                      close=apple['Close'])])

  # Add hover data
  fig.update_traces(hoverinfo='x+y')

  # Add range selector buttons for zooming in/out
  fig.update_layout(xaxis=dict(rangeslider=dict(visible=False), type="date"))

  # Show the interactive chart
  fig.show()

  return fig.write_html("../html/apple_stock_candlestick_chart.html")

make_graph("AAPL","2023-6-1","2024-1-1")

