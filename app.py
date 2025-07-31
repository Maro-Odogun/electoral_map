from dash import Dash, dcc, Input, Output, callback, html
from utilities_and_text import external_link, external_stylesheets, \
    presidential_election_p1, presidential_election_p2, voter_reg_p, legislature_p, make_break
from data import main_data, senate_df, house_df, voter_reg_focus
from create_visuals import create_map, create_figure, create_plot


app = Dash(external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.Div([html.Img(src="https://media.istockphoto.com/id/495144439/photo/nigerian-flag-map.jpg?s=612x612&w=0&k=20&c=9NENjlSRzNLw_xUGFydkAe36VkwD8d9e8JvZIipv7Y8=", 
    style={'width': '300px', 'height': '200px'})], style={'text-align': 'center'}),
    html.H1("A Glance at Nigeria's Electoral Scene", style={'font-family':'DM Sans', 'text-align':'center'}),
    html.Div([
        dcc.Dropdown(id='year_id', 
            options=[{'label': '2023', 'value': 2023}, 
            {'label': '2019', 'value': 2019}, {'label': '2015', 'value': 2015}], placeholder='2023',
            style={'width': '150px', 'height': '40px', 'margin': '50px 0px 0px 35px', 'fontFamily': 'DM Sans, Arial, sans-serif'}),

        dcc.Graph(id='election_map')
    ]),

    *make_break(1),
    html.P(presidential_election_p1, style={'font-family':'DM Sans', 'padding':'0px 100px 0px 100px'}),

    html.P([
    presidential_election_p2,
    html.A("here", href=f"{external_link}", target="_blank", style={'color': '#1f77b4', 'text-decoration': 'none'}),
    "."
], style={'font-family':'DM Sans', 'padding':'0px 100px 0px 100px'}), 
 

    *make_break(4),
    html.Div([
        dcc.Dropdown(id='year_concerned', 
            options=[{'label': '2023', 'value': 2023}, {'label': '2019', 'value': 2019}, 
            {'label': '2015', 'value': 2015}, {'label': '2011', 'value': 2011}, {'label': '2007', 'value': 2007}], placeholder='2023',
            style={'width': '150px', 'height': '40px', 'margin': '50px 0px 0px 35px', 'fontFamily': 'DM Sans, Arial, sans-serif'}),

        dcc.Graph(id='legislative_composition')
    ]),

    html.P(legislature_p, style={'font-family':'DM Sans', 'padding':'0px 100px 0px 100px'}),
    *make_break(4),
    html.Div([
        dcc.Graph(id='voter_reg_trend'),
        *make_break(1),
        dcc.Slider(
            id = 'year_slider',
            min = 2011,
            max = 2023,
            value = 2011,
            step = 1,
            marks={
                2011: {'label': '2011', 'style': {'font-family': 'DM Sans'}},
                2015: {'label': '2015', 'style': {'font-family': 'DM Sans'}},
                2019: {'label': '2019', 'style': {'font-family': 'DM Sans'}},
                2023: {'label': '2023', 'style': {'font-family': 'DM Sans'}},
            },
            vertical = False,

        ),
    ], style={'margin': '0px 0px 40px 0px'}),

    html.P(voter_reg_p, style={'font-family':'DM Sans', 'padding':'0px 100px 0px 100px'}),
    *make_break(2)
    ,
    html.Footer(html.I('Created by Oghenemaro. Inspired by Stears', style={'font-family':'DM Sans', 'padding':'0px 100px 0px 100px'}))

],
style={'background-color': 'white', 'padding': '40px'}
)



# Callback for Presidential Election functionality
@callback(
    # Set the input and output of the callback to link the dropdown to the graph
    Output(component_id='election_map', component_property='figure'),
    Input(component_id='year_id', component_property='value'),
)
def update_map(input_year):
    default_year = 2023
    election_data = main_data.copy(deep=True)

    if (input_year):
        fig = create_map(main_data, input_year)

    else:
        fig = create_map(main_data, default_year)
      
    return fig


# Callback for Legislative Composition dropdown functionality
@callback(
# Set the input and output of the callback to link the dropdown to the graph
    Output(component_id='legislative_composition', component_property='figure'),
    Input(component_id='year_concerned', component_property='value')
)
def update_figure(input_year):
    selected_year = 2023
    if (input_year):
        selected_year = input_year
        fig = create_figure(senate_df, house_df, selected_year)
        
    else:
        fig = create_figure(senate_df, house_df, selected_year)
    

    return fig


# Callback for Voter Participation slider functionality
@callback(
    # Set the input and output of the callback to link the dropdown to the graph
    Output(component_id='voter_reg_trend', component_property='figure'),
    Input(component_id='year_slider', component_property='value')
)
def update_chart(input_year):
    default_year = 2011
    if (input_year):
        fig = create_plot(input_year)
    else:
        fig = create_plot(default_year)
    
    return fig



if __name__ == '__main__':
    app.run(debug=True)
