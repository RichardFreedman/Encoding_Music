# import necessary libraries
import streamlit as st
import pandas as pd
import pydeck as pdk
import re 
from streamlit_folium import st_folium
import folium
import plotly.express as px
from folium.plugins import MousePosition

# Set up Streamlit page
st.set_page_config(page_title="Musical Events Map", layout="wide")
st.title("BiCo Sound Map")

# Page description
st.markdown('Sounds of Silence: A Sound Survey of the Bi-Co During Finals Week')
st.markdown('By Logan Griffin, Luke Sheppard, Reed Solomon, and Jade Yu')

# Bryn Mawr, PA coordinates (used as map center)
CENTER_LAT = 40.0209
CENTER_LON = -75.3137

# Load data
@st.cache_data
def load_data():
#!!!!!this is where I put in my updated CSV!!!!!!
    return pd.read_csv("https://raw.githubusercontent.com/RichardFreedman/Encoding_Music/refs/heads/main/06_SoundMap/bicomap.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Events by Category")

# Initialize filtered dataframe
filtered_df = df.copy()
active_filters = []

# Purpose filter (multiselect)
if 'purpose' in df.columns:
    st.sidebar.subheader("📝 Purpose")
    
    # Split all purpose strings and collect unique substrings
    all_purposes = set()
    for purpose_string in df['purpose'].dropna():
        # Split by semicolon and add each cleaned substring to the set
        purposes = [p.strip() for p in purpose_string.split(';') if p.strip()]
        all_purposes.update(purposes)
    
    # Convert to sorted list for the multiselect
    purpose_options = sorted(all_purposes)
    
    if len(purpose_options) > 0:
        selected_purposes = st.sidebar.multiselect(
            "Select purposes:",
            options=purpose_options,
            default=purpose_options,
            key="purpose_filter"
        )
        
        if len(selected_purposes) < len(purpose_options):
            # Create regex pattern to match any of the selected purposes
            pattern = '|'.join([re.escape(purpose) for purpose in selected_purposes])
            filtered_df = filtered_df[filtered_df['purpose'].str.contains(pattern, na=False, regex=True)]
            active_filters.append(f"Purpose: {len(selected_purposes)}/{len(purpose_options)}")

# Numeric fields section
st.sidebar.subheader("Numeric Attributes")

numeric_fields = ['volume', 'pitch', 'distractability', 'rowdiness', 'multiplicity', 'repetition', 'persistence']

for field in numeric_fields:
    if field in df.columns:
        # Convert to numeric and get valid values
        numeric_values = pd.to_numeric(df[field], errors='coerce').dropna()
        
        if len(numeric_values) > 0:
            min_val = int(numeric_values.min())
            max_val = int(numeric_values.max())
            
            if min_val < max_val:  # Only create slider if there's a range
                selected_range = st.sidebar.slider(
                    f"{field.title()}:",
                    min_value=min_val,
                    max_value=max_val,
                    value=(min_val, max_val),
                    step=1,
                    key=f"{field}_slider",
                    help=f"Filter events by {field} level (range: {min_val}-{max_val})"
                )
                
                # Check if filter is active (not full range)
                if selected_range != (min_val, max_val):
                    # Filter data based on selected range
                    numeric_col = pd.to_numeric(filtered_df[field], errors='coerce')
                    filtered_df = filtered_df[
                        (numeric_col >= selected_range[0]) & 
                        (numeric_col <= selected_range[1])
                    ]
                    active_filters.append(f"{field.title()}: {selected_range[0]}-{selected_range[1]}")

# Marker size control
st.sidebar.subheader("Set Marker Size")
available_numeric_fields = [field for field in numeric_fields if field in df.columns]
size_field = st.sidebar.selectbox(
    "Size markers by:",
    options=['Fixed Size'] + available_numeric_fields,
    index=0,
    help="Choose a numerical field to control marker size"
)

# Show active filters in sidebar
if active_filters:
    st.sidebar.subheader("Active Filters")
    for filter_info in active_filters:
        st.sidebar.write(f"• {filter_info}")
else:
    st.sidebar.info("No filters applied - showing all events")

# Reset filters button
if st.sidebar.button("Reset All Filters"):
    st.rerun()

# Clean coordinate data for filtered results
filtered_map_data = filtered_df.dropna(subset=['latitude', 'longitude'])
filtered_map_data['latitude'] = pd.to_numeric(filtered_map_data['latitude'], errors='coerce')
filtered_map_data['longitude'] = pd.to_numeric(filtered_map_data['longitude'], errors='coerce')
filtered_map_data = filtered_map_data.dropna()

# Add the size field to map data if selected
if size_field != 'Fixed Size' and size_field in filtered_df.columns:
    # Get the size values for the filtered data
    size_values = pd.to_numeric(filtered_df.loc[filtered_map_data.index, size_field], errors='coerce')
    filtered_map_data[size_field] = size_values
    # Remove rows where size field is NaN
    filtered_map_data = filtered_map_data.dropna()
st.dataframe(filtered_df)
# Main content
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Event Locations")
    
    # Creating the base map 
    if len(filtered_map_data) > 0:

        m = folium.Map(location=[CENTER_LAT, CENTER_LON], zoom_start=16)

        # Putting the markers from my data onto the map
        for index, row in filtered_map_data.iterrows():
            popup_html = "<br>".join([f"<b>{k}:</b> {str(v)}" for k, v in row.to_dict().items()])
            
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=6,
                color="blue",
                fill=True,
                fill_opacity=0.8,
                tooltip=row.get("location"),
                popup=folium.Popup(folium.Html(popup_html, script=True), max_width=250),
                interactive=False   
            ).add_to(m)

        # This is so it can respond when I click on markers
        folium.LatLngPopup().add_to(m)

        # Getting the map to load
        st_data = st_folium(m, width = 725, key = "main_map")

        # Setting up last object clicked so I can reference what I click
        last = st_data.get("last_object_clicked")
        if last is not None:
            st.session_state["last_object_clicked"] = last
    
    else:
        st.warning("No events match the selected filters")

    # Melting the dataframe so I can make a bar chart
    id_vars = ['link', 'timestamp', 'campus', 'time', 'date', 'location', 'latitude', 'longitude', 'device', 'sound', 'recorder', 'purpose']
    value_vars = ['volume','pitch','distractability', 'rowdiness','multiplicity','repetition','persistence']
    melted_df = pd.melt(filtered_df, id_vars = id_vars, value_vars = value_vars)


    # Setting lat, lon, and clicked_row_melted to be empty to avoid errors before the first click
    lat = None
    lon = None
    clicked_row_melted = pd.DataFrame()

    # Registering a click
    clicked = st.session_state.get("last_object_clicked")

    # Getting the coordinates of the clicked marker
    if clicked is not None:
        lat = clicked.get("lat")
        lon = clicked.get("lng")

    # Filtering the dataframe to the rows with the clicked marker
    if lat is not None and lon is not None:
        clicked_row_melted = melted_df[
            (melted_df["latitude"]==lat) &
            (melted_df["longitude"]==lon)
        ]
 
    # Making the bar chart
    if not clicked_row_melted.empty:
        st.subheader("Feature Chart for: {}" .format(clicked_row_melted["sound"].iloc[0]))
        fig = px.bar(
            clicked_row_melted,
            x="variable",
            y="value",
            color="variable"
            )
        st.plotly_chart(fig)
    else:
        st.info("No sound selected")


    
with col2:
    st.subheader("Summary")
    
    # Metrics
    total_events = len(df)
    filtered_events = len(filtered_df)
    mapped_events = len(filtered_map_data)
    
    st.metric("Total Events", total_events)
    st.metric("Filtered Events", filtered_events, delta=filtered_events - total_events)
    st.metric("Mapped Events", mapped_events)
    
    # Show size field info
    if size_field != 'Fixed Size':
        st.write(f"**Marker Size:** {size_field.title()}")
        if len(filtered_map_data) > 0 and size_field in filtered_map_data.columns:
            size_values = filtered_map_data[size_field]
            st.write(f"Range: {size_values.min():.1f} - {size_values.max():.1f}")
    
    # Coverage percentage
    if total_events > 0:
        coverage = (filtered_events / total_events) * 100
        st.progress(coverage / 100)
        st.write(f"Showing {coverage:.1f}% of all events")

# Optional data preview
with st.expander("View Filtered Data"):
    if len(filtered_df) > 0:
        st.dataframe(filtered_df, width='stretch')
        
        # Download button
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Filtered Data",
            data=csv,
            file_name="filtered_musical_events.csv",
            mime="text/csv"
        )
    else:
        st.info("No data to display with current filters.")



    


