from datetime import datetime as dt

from dash.dependencies import Input, Output, State
import pandas_datareader as pdr


def register_callbacks(app):
    @app.callback(Output('my-graph', 'figure'), Input('my-dropdown', 'value'),
                  State('user-store', 'data'))
    def update_graph(selected_dropbox_value):
        df = pdr.get_data_yahoo(selected_dropbox_value,
                                start=dt(2017, 1, 1),
                                end=dt.now())
        return {
            'data': [{
                'x': df.index,
                'y': df.Close
            }],
            'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
        }

