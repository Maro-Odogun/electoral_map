import pandas as pd
from data_loader import senate_df, house_df, main_data, voter_reg_focus
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Colour Map for Presidential Election Entities
color_map_election={
    'Labour Party': 'rgba(214, 39, 40, 0.9)',     
    'All Progressives Congress': 'rgba(96, 129, 238, 0.9)',     
    'People\'s Democratic Party': 'rgba(44, 160, 44, 0.9)',           
    'New Nigeria People\'s Party': 'rgba(154, 220, 192, 0.9)',     
}

# Colour Map for Legislative Composition Entities
color_map_legislative = {
    'Peoples\' Democratic Party': 'rgba(44, 160, 44, 0.8)',    # Green 
    'All Progressives Congress': 'rgba(96, 129, 238, 0.8)',    # Blue 
    'All Nigeria Peoples Party': 'rgba(255, 127, 14, 0.7)',   # Orange 
    'Action Congress': 'rgba(148, 103, 189, 0.7)',            # Purple 
    'Other Parties': 'rgba(140, 86, 75, 0.7)'                 # Brown 
}

# Find the centroids of the states and use that to plot a scatterplot with text representing state names
centroids = main_data.geometry.centroid

# Remove these states names for a tidier map
remove_places = ['Federal Capital Territory', 'Adamawa', 'Anambra', 'Kastina', 'Ebonyi', 'Abia', 'Cross River', 'Akwa Ibom']
label_data = pd.DataFrame({
    'lat': centroids.y,
    'lon': centroids.x,
    'text': main_data.index
})
label_data = label_data.drop(remove_places, errors='ignore')



# Code for creating Presidential Election Map
def create_map(main_data, input_year):
    data = main_data[main_data['Year'] == input_year]
    before_2023_hover_data = ['People\'s Democratic Party', 'All Progressives Congress']
    hover_data = ['People\'s Democratic Party', 'All Progressives Congress', 'Labour Party', 'New Nigeria People\'s Party']

    if input_year != 2023:
        selected_hover_data = before_2023_hover_data
    else:
        selected_hover_data = hover_data

    fig = px.choropleth(
        data,
        geojson=data.geometry,
        locations=data.index,
        color="Winning Party",
        # Add custom color palette for political parties
        color_discrete_map= color_map_election,
        hover_data=selected_hover_data,
        custom_data = 'Winning Party',
        title="Nigerian Presidential Election Results by State"
    )
        
    fig.add_trace(
        go.Scattergeo(
        lon=label_data['lon'],
        lat=label_data['lat'],
        text=[f"<b style='text-shadow: -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, \
        2px 2px 0 #000, 0px -2px 0 #000, 0px 2px 0 #000, -2px 0px 0 #000, 2px 0px 0 #000; font-family: \
        \"Plus Jakarta Sans\", \"Montserrat\", \"Roboto\", sans-serif; font-weight: 400; letter-spacing: 1px;'>{txt}</b>" for txt in label_data['text']],
        mode='text',
        textfont=dict(
            size=8, 
            color='white', 

        ),
        textposition='middle center',
        showlegend=False,
        hoverinfo='skip'
        )
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False,
        projection_type="natural earth",
    )

    fig.update_layout(
        title=dict(
            text=f"Nigerian Presidential Election Results by State ({input_year})",
            x=0.5,
            font=dict(size=16, family='DM Sans, Arial, sans-serif', color='black')
        ),

        font=dict(size=12, family='DM Sans, Arial, sans-serif', color='black'),
        margin=dict(l=0, r=0, t=50, b=0),
        legend=dict(x=0.8, y=0.1),
        autosize=True,  
        height=500 
      
    )

    return fig

# # Code for creating legislative pie charts
def create_figure(senate_df, house_df, input_year):
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'pie'}, {'type': 'pie'}]],
                        subplot_titles=("Senate", "House"))

    senate = senate_df[senate_df['Year'] == input_year]
    house = house_df[house_df['Year'] == input_year]

    senate_chart = px.pie(data_frame=senate, 
    names='Party', values='Seats', color='Party',
    labels='Party',
    color_discrete_map = color_map_legislative)

    house_chart = px.pie(data_frame=house, 
        names='Party', values='Seats', color='Party',
    labels='Party',
    color_discrete_map = color_map_legislative)

    senate_chart.update_traces(
    hovertemplate='<b>%{label}</b><br>Seats: %{value}'
    )

    house_chart.update_traces(
    hovertemplate='<b>%{label}</b><br>Seats: %{value}'
    )

    fig.add_trace(senate_chart.data[0], row=1, col=1)
    fig.add_trace(house_chart.data[0], row=1, col=2)

    fig.update_layout(
        title=dict(
            text=f"Legislative Composition ({input_year})",
            x=0.5,
            font=dict(size=16, family='DM Sans, Arial, sans-serif', color='black')
        ),
        font=dict(size=12, family='DM Sans, Arial, sans-serif', color='black'),
        autosize=True,  
        height=500 
    )

    return fig

# # Code for creating Voter Participation line plots
def create_plot(input_year):
    data = voter_reg_focus.copy(deep=True)
    data = data[data['Year'] <= input_year]
    fig = px.line(
        data_frame=data, 
        x='Year', 
        y=['% registered voters who voted', '% eligible pop. who registered to vote', '% eligible pop. who voted'], 
        markers=True,
        title='Nigerian Electoral Participation Trends',
        labels={
            'value': 'Percentage (%)',
            'variable': 'Metric',
            'Year': 'Election Year'
        },

        color_discrete_map={
            '% registered voters who voted': '#2E86AB',        # Blue 
            '% eligible pop. who registered to vote': '#A23B72', # Purple  
            '% eligible pop. who voted': '#F18F01'              # Orange 
        },
    )

    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        autosize=True,  
        height=500, 
        font=dict(size=12, family='DM Sans, Arial, sans serif', color='black'),
        title=dict(
            text='Nigerian Electoral Participation Trends',
            x=0.5,
            font=dict(size=16, color='#2F2F2F')
        ),
        legend=dict(
            title=dict(text='Metrics', font=dict(size=12)),
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='center',
            x=0.5,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#CCCCCC',
            borderwidth=1
        ),
        xaxis=dict(
            title='Election Year',
            showgrid=True,
            gridcolor='#E5E5E5',
            linecolor='#CCCCCC',
            range=[2010, 2024],
            tickfont=dict(size=11)
        ),
        yaxis=dict(
            title='Percentage (%)',
            showgrid=True,
            gridcolor='#E5E5E5',
            linecolor='#CCCCCC',
            tickfont=dict(size=11),
            range=[0, 100]  
        ),
        hovermode='x unified'
    )

        # Update line styles
    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=8, line=dict(width=2, color='white')),
        hovertemplate='<b>%{fullData.name}</b><br>' +
                     '<span style="color: #666;">Percentage:</span> <b>%{y:.1f}'
                    
               
    )
    
    return fig  

