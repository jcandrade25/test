#---------------------------------------------------------------------
#Include libraries

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd

#---------------------------------------------------------------------
#Import data

from busRoutes import MAN_Route, NY_Route
# MAN_Route.printRouteInfo()		#Uncomment these to see route info
# NY_Route.printRouteInfo()			#printed on the console	

#---------------------------------------------------------------------
#Layout

external_stylesheets = [
    "https://codepen.io/chriddyp/pen/bWLwgP.css",
    "/assets/style.css",
    ]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width,initial-scale=1.0"}
    ],
)

app.layout = html.Div(
	html.Div(id="app-container",
		children = [
			html.Div(
		        id="header",
		        children=[
		            html.Div(
		                id="header-text",
		                children=[
		                    html.H3("NYC Boroughs Electric Bus Routes Report"),
		                    html.H6("by Juan Camilo Andrade"),
		                ],
		            ),
		        ],
		    ),
		    html.Hr(),
			html.Div(id='tabs-container',
				children=[
				    dcc.Tabs(id='tabs',
				    	children=[
					        dcc.Tab(label='Manhattan', value="Manhattan_Tab",),
					        dcc.Tab(label='NY',value='NY_Tab'),
				   	],colors={
				        "border": "#23272c",
				        "primary": "#a3a7b0",
				        "background": "#23272c"
			   		})
				]
			),
			html.Div(id='data-container',
				children=[
					# html.Br(),
					html.Div(id='graphs-container',
						children=[
							html.Div(id='graph-routeVelocity'),
							html.Div(id='graph-routeEnergy'),
						]
					 ),	
					html.Div(id='moments-container',
						children=[
							html.Br(),
							html.Hr(),
							html.Div(id='pad-moments'),
							html.Div(id='disp-velocityMoments'),
							html.Div(id='disp-powerMoments'),
							html.Hr(),
						], style= {"border": "#23272c",
						        "primary": "#a3a7b0",
						        "background": "#23272c"}
					),
				]
			)
		]
	)		
)

def createFig(data):
	# print(data)
	return {
	    "data": [
	        {
	            "x": data.index,
	            "y": data[data.columns[0]],
	            "type": "line",
	            "showscale": False,
	            "colorscale": [[0, "rgba(255, 255, 255,0)"], [1, "#a3a7b0"]],
	        }
	    ],
	    "layout": {
	    	'title':f"Bus {data.columns[0]} over t[s]",
	        "margin": {"t": 100, "b": 30},
	        "height": 400,
	        "xaxis": {
	            "showline": True,
	            "zeroline": False,
	            "showgrid": True,
	            "showticklabels": True,
	            "color": "#a3a7b0",
	        },
	        "yaxis": {
	            "fixedrange": True,
	            "showline": False,
	            "zeroline": False,
	            "showgrid": True,
	            "showticklabels": True,
	            "ticks": "",
	            "color": "#a3a7b0",
	        },
	        "plot_bgcolor": "#23272c",
	        "paper_bgcolor": "#23272c",
	    },
	}

#---------------------------------------------------------------------
#Callbacks

@app.callback(
	Output('graph-routeVelocity','children'),
	Input('tabs','value')
)
def render_graph1(tab):
	if tab == 'Manhattan_Tab':
		route = MAN_Route
	elif tab == 'NY_Tab':
		route = NY_Route
	else:
		return

	return html.Div([
		dcc.Graph(id='man_routeVelocity',
	            figure=createFig(route.routeVelocity), 
	            config={"doubleClick": "reset"}
	    )
	])

@app.callback(
		Output('graph-routeEnergy','children'),
		Input('tabs','value')
	)
def render_graph2(tab):
	if tab == 'Manhattan_Tab':
		route = MAN_Route
	elif tab == 'NY_Tab':
		route = NY_Route
	else:
		return

	return html.Div([
		dcc.Graph(id='man_routeEnergy',
                figure=createFig(route.routeEnergy), 
                config={"doubleClick": "reset"}
        )
    ])

@app.callback(
		Output('disp-velocityMoments','children'),
		Input('tabs','value')
	)
def render_moments1(tab):
	if tab == 'Manhattan_Tab':
		route = MAN_Route
	elif tab == 'NY_Tab':
		route = NY_Route
	else:
		return
	return html.Div(
		children=[
			html.H2('Velocity Moments'),
			html.P(f'Mean Velocity: {route.avgVelocity} m/s'),
			html.P(f'Velocity Standard Deviation: {route.stdVelocity}'),
		]	
	)

@app.callback(
		Output('disp-powerMoments','children'),
		Input('tabs','value')
	)
def render_moments2(tab):
	if tab == 'Manhattan_Tab':
		route = MAN_Route
	elif tab == 'NY_Tab':
		route = NY_Route
	else:
		return

	return html.Div(
		children=[
			html.H2('Power Moments'),
			html.P(f'Mean Power: {route.avgPower} W'),
			html.P(f'Power Standard Deviation: {route.stdPower}'),
		]	
	)



if __name__=="__main__":
	app.run_server(debug=True)


        