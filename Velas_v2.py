import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, dcc, html, Input, Output

# Lee el archivo Excel
df = pd.read_excel('yahoo_finance_multiple_tickers.xlsx', sheet_name='Consolidado')

# Calcula indicadores técnicos
df['SMA20'] = df['Close'].rolling(window=20).mean()  # Media móvil simple de 20 periodos
df['EMA20'] = df['Close'].ewm(span=20, adjust=False).mean()  # Media móvil exponencial de 20 periodos
df['BB_upper'] = df['SMA20'] + 2 * df['Close'].rolling(window=20).std()  # Banda superior de Bollinger
df['BB_lower'] = df['SMA20'] - 2 * df['Close'].rolling(window=20).std()  # Banda inferior de Bollinger

# Calcula el RSI (Índice de Fuerza Relativa)
delta = df['Close'].diff()
gain = (delta.where(delta > 0, 0)).fillna(0)
loss = (-delta.where(delta < 0, 0)).fillna(0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
df['RSI'] = 100 - (100 / (1 + rs))

# Crea la aplicación Dash
app = Dash(__name__)

# Define el layout de la aplicación
app.layout = html.Div(
    [
        html.H1("Gráfico de Velas", style={'textAlign': 'center', 'fontFamily': 'Helvetica', 'color': '#222'}),
        dcc.Dropdown(
            id="ticker-selector",
            options=[{"label": ticker, "value": ticker} for ticker in df["Ticker"].unique()],
            value=df["Ticker"].unique()[0],
            style={'fontFamily': 'Helvetica', 'fontSize': '25px', 'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '5px'}
        ),
        dcc.Graph(id="candlestick-graph"),
    ], 
    style={'backgroundColor': '#f4f4f4', 'fontFamily': 'Helvetica', 'color': '#333', 'width': '100vw', 'height': '70vh'} 
)

# Define el callback para actualizar la gráfica
@app.callback(
    Output("candlestick-graph", "figure"), Input("ticker-selector", "value")
)
def update_graph(selected_ticker):
    # Crea la figura con tres subplots
    fig = make_subplots(
        rows=3, 
        cols=1, 
        shared_xaxes=True, 
        vertical_spacing=0.1, 
        row_heights=[1, 0.2, 0.2], 
        specs=[[{}], [{"secondary_y": True}], [{}]]
    )

    # Filtra los datos por el ticker seleccionado
    df_filtered = df[df["Ticker"] == selected_ticker]

    # Agrega la gráfica de velas al primer subplot
    fig.add_trace(
        go.Candlestick(
            x=df_filtered["Date"],
            open=df_filtered["Open"],
            high=df_filtered["High"],
            low=df_filtered["Low"],
            close=df_filtered["Close"],
            name=selected_ticker,
            increasing_line_color="green",
            decreasing_line_color="red",
        ),
        row=1,
        col=1,
    )

    # Agrega las medias móviles al primer subplot
    fig.add_trace(
        go.Scatter(
            x=df_filtered["Date"],
            y=df_filtered["SMA20"],
            name="SMA20",
            line=dict(color="blue", width=1),
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=df_filtered["Date"],
            y=df_filtered["EMA20"],
            name="EMA20",
            line=dict(color="orange", width=1),
        ),
        row=1,
        col=1,
    )

    # Agrega las Bandas de Bollinger al primer subplot
    fig.add_trace(
        go.Scatter(
            x=df_filtered["Date"],
            y=df_filtered["BB_upper"],
            name="BB_upper",
            line=dict(color="grey", width=1),
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=df_filtered["Date"],
            y=df_filtered["BB_lower"],
            name="BB_lower",
            line=dict(color="grey", width=1),
        ),
        row=1,
        col=1,
    )

    # Agrega el gráfico de volumen con colores según la vela al segundo subplot
    fig.add_trace(
        go.Bar(
            x=df_filtered["Date"],
            y=df_filtered["Volume"],
            name="Volumen",
            marker_color=list(map(lambda x: 'green' if x else 'red', df_filtered['Close'] > df_filtered['Open'])),
            opacity=1
        ),
        row=2,
        col=1,
        secondary_y=False,
    )

    # Agrega el RSI al tercer subplot
    fig.add_trace(
        go.Scatter(
            x=df_filtered["Date"],
            y=df_filtered["RSI"],
            name="RSI",
            line=dict(color="purple", width=1),
        ),
        row=3,
        col=1,
    )

    # Configura el diseño del gráfico
    fig.update_layout(
        template="plotly_dark",
        xaxis_rangeslider_visible=False,
        hovermode="x unified",
        yaxis_title="Precio",
        showlegend=False,
        width=1900,
        height=720,
    )

    # Configura el diseño del subgráfico de volumen
    fig.update_yaxes(title_text="Volumen", row=2, col=1)

    # Configura el diseño del subgráfico RSI
    fig.update_yaxes(title_text="RSI", row=3, col=1)
    fig.add_shape(
        go.layout.Shape(
            type="line",
            x0=df_filtered['Date'].min(),
            x1=df_filtered['Date'].max(),
            y0=70,
            y1=70,
            line=dict(color="red", width=1, dash="dash"),
            xref="x",
            yref="y2",
        ),
        row=3,
        col=1,
    )
    fig.add_shape(
        go.layout.Shape(
            type="line",
            x0=df_filtered['Date'].min(),
            x1=df_filtered['Date'].max(),
            y0=30,
            y1=30,
            line=dict(color="green", width=1, dash="dash"),
            xref="x",
            yref="y2",
        ),
        row=3,
        col=1,
    )


    return fig

# Ejecuta la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)