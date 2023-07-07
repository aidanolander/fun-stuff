
# Aidan's Map App 
# Web App to highlight my favorite locations in DC, using Shiny for Python to display a map and table with filter options


from shiny import App, render, ui, reactive
from shinywidgets import output_widget, render_widget
import pandas as pd
import mysql.connector
from ipyleaflet import Map, Marker, AwesomeIcon
from ipywidgets import HTML
import shinyswatch

#create connection to Amazon RDS database
conn = mysql.connector.connect(
        host="data-maps-1.czlrrfwauudc.us-east-2.rds.amazonaws.com",
        user="adminaidan",
        passwd="tac02zDAYS!"
        )

#we're just grabbing the whole table, to be turned into a pandas DF. That DF will be manipulated for the filters
stmt = "SELECT * FROM maps_db.dc_locations_tab"

#remplate for the html popup of the marker
html_temp="""
        <h3> {loc_name} </h3><br>
        Type: {loc_type}<br>
        Address: {address}<br>
        Tags: {tags}<br>
        Rating: {rate}<br>
        <i>{description}</i>
        """

#create pandas DF
df = pd.read_sql(stmt, con=conn)

#just a list of the column names, for reference and maybe future use
col_names = ['loc_name', 'city_name', 'loc_type', 'type_special', 'loc_address',
       'loc_vibe', 'loc_rating', 'latitude', 'longitude', 'loc_neighbor',
       'loc_tags', 'loc_descr']



#This was my way of solving the issue with having commas separating tags in the csv file. Next iteration will have a separate table for tags as we discussed
#Converts underscores back into commas while dealing with the extra space it somehow created before all underscores
#And capitalizes tags so it looks better in table and popups 
df['loc_descr'] = df['loc_descr'].str.replace('_',',')
df['loc_tags'] = df['loc_tags'].str.replace(' ','')
df['loc_descr'] = df['loc_descr'].str.replace(' ,',',')
df['loc_tags'] = df['loc_tags'].apply(lambda x: ", ".join(x.split("_")).title())



#function to filter the dataframe by a keyword in a column
def Filter_DF(filt_by, dataframe, col_name):
    filter_word = filt_by.title()
    filt_df = dataframe[dataframe[col_name]==filter_word].reset_index()
    return(filt_df)
#end def


#themes I enjoy:
#cerulean, darkly, journal, sketchy, superhero, vapor

#beginning of shiny framework
#this creates the UI, and in order contains:
# ui.page_fluid() - makes a fluid page that resizes to browser size
# shinyswatch.theme.sketchy() - creates the theme, "sketchy" can be replaced with those I mentioned above
# ui.h2() - HTML header, sized to 2
# ui.input_radio_buttons() - create first filter options input, radio buttons to select All, Food, Bar, or Activity. Saves choice as string named input.select_type()
# ui.unput_text() - create second filter option input with a search bar. Creates string named input.text_search()
# ui.hr() - HTML line break, creates a thin line separating above and below UI objects
# output_widget() - output element of UI that shows the map created from the output_map function in the server section of app
# ui.hr() - same HTML line break as before
# ui.output_table() - outputs the table creates from out_table function in server section of app

app_ui = ui.page_fluid(
    shinyswatch.theme.sketchy(),
    ui.h2("Aidan's Favorites in DC"),
    ui.input_radio_buttons(
        id="select_type", label="What are you looking for?", choices={"All": "All", "Bar": "Bar", "Food": "Food", "Activity": "Activity"}),
    ui.input_text("text_search", "Search locations", placeholder="Enter name, tags, etc."),
    ui.hr(), #creates a little line on the page separating elements
    output_widget("my_widget"),
    ui.hr(),
    ui.output_table(id="out_table")
)

#this is the server section of the shiny app, where it reacts to inputs to render outputs.
#inside we are only outputting two things, a map and a table

def server(input, output, session):
     
    #map output, done in a few steps. Eventually I want to clean this and make it into a a simple function above like Filter_DF
    @output
    @render_widget
    def my_widget():
        #first, filter by the radio button input described above. All is the whole df, others use Filter_DF to filter by loc_type 
        #then filter by the search bar input, using the lambda function to search the whole row of the DF. this allows them to search by tags, address, name, etc
        if input.select_type() == "All":
            filtered_df = df
            is_present = filtered_df.apply(lambda row: any(input.text_search().lower() in str(value).lower() for value in row.values), axis=1)
            filtered_df = filtered_df[is_present].reset_index()

        else:
            filtered_df = Filter_DF(input.select_type(), df, "loc_type")
            is_present = filtered_df.apply(lambda row: any(input.text_search().lower() in str(value).lower() for value in row.values), axis=1)
            filtered_df = filtered_df[is_present].reset_index()
        
        #get center coordinates as the average of all remaining locations
        start_lat = (filtered_df.latitude).mean()
        start_long = (filtered_df.longitude).mean()
        start_coords = list([start_lat]+[start_long])

        #Create the map
        my_map = Map(center=start_coords, zoom=12)
    
        #use a for loop to go through the filtered DF and create a popup for each location
        for i in range(len(filtered_df)):
            loc_lat = float(filtered_df.latitude[i])
            loc_long = float(filtered_df.longitude[i])
            loc_coords = tuple(list([loc_lat] + [loc_long]))
        
            #use html template created at the top and fill it with information from the dataframe
            html=html_temp.format(loc_name=filtered_df.loc_name[i], loc_type = filtered_df.loc_type[i],
                              address=filtered_df.loc_address[i],tags=filtered_df.loc_tags[i],
                              rate=filtered_df.loc_rating[i], description=filtered_df.loc_descr[i])
        
            #check to see what type of location, change icons to better match. Uses Font Awesome icons 
            if filtered_df.loc_type[i]=="Bar":
                loc_icon = "fa-glass"
                loc_color = "blue"
            elif filtered_df.loc_type[i]=="Food":
                loc_icon = "fa-cutlery"
                loc_color = "gray"
            else:
                loc_icon = "fa-globe"
                loc_color = "green"
            
            icon1 = AwesomeIcon(
                name=loc_icon,
                marker_color=loc_color,
                icon_color='white',
                spin=False
            )
        
            #create the marker and add it as a layer to the map
            marker = Marker(icon=icon1, location=loc_coords, draggable=False, title=filtered_df.loc_name[i])
            message = HTML(html)
            marker.popup = message
            my_map.add_layer(marker);






        #Display the map
        return(my_map)
    

    #table output, much simpler. Basically uses the same logic to filter the dataframe but drops certain information. 
    #Then renders the table to show what's displayed on the map

    @output
    @render.table
    def out_table():
        if input.select_type() == "All":
            filtered_df = df
            is_present = filtered_df.apply(lambda row: any(input.text_search().lower() in str(value).lower() for value in row.values), axis=1)
            filtered_df = filtered_df[is_present]
        else:
            filtered_df = Filter_DF(input.select_type(), df, "loc_type")
            is_present = filtered_df.apply(lambda row: any(input.text_search().lower() in str(value).lower() for value in row.values), axis=1)
            filtered_df = filtered_df[is_present]
        columns_to_drop = ['loc_vibe', 'city_name','type_special', 'latitude', 'longitude']
        filtered_df = filtered_df.drop(columns=columns_to_drop)
        filtered_df.rename(columns={'loc_name': 'Name', 'loc_type': 'Type', 'loc_address': 'Address',
                                    'loc_rating': 'Rating', 'loc_descr': 'Description','loc_tags': 'Tags' }, inplace=True)
        return filtered_df



#last part is connecting the server and UI, creating the app
app = App(app_ui, server)

#run in terminal using "shiny run map_code4William.py"
