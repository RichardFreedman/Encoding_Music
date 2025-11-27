
        
import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Musical Events Map", layout="wide")
st.title("🎵 Musical Events Interactive Map")

# Bryn Mawr, PA coordinates
CENTER_LAT = 40.0209
CENTER_LON = -75.3137

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTT1nChPTl-tDC-g6R-Uv6kctTq48S8hYy_k3NMc9PwFLEhVJelmTLC0jIoFecerYc1KJNk7EcX9dlY/pub?output=csv")

df = load_data()

# Sidebar filters
st.sidebar.header("🎛️ Filter Events")

# Initialize filtered dataframe
filtered_df = df.copy()
active_filters = []

# Purpose filter (multiselect)
if 'purpose' in df.columns:
    st.sidebar.subheader("📝 Purpose")
    purpose_options = df['purpose'].dropna().unique()
    if len(purpose_options) > 0:
        selected_purposes = st.sidebar.multiselect(
            "Select purposes:",
            options=sorted(purpose_options),
            default=sorted(purpose_options),
            key="purpose_filter"
        )
        if len(selected_purposes) < len(purpose_options):
            filtered_df = filtered_df[filtered_df['purpose'].isin(selected_purposes)]
            active_filters.append(f"Purpose: {len(selected_purposes)}/{len(purpose_options)}")

# Numeric fields section
st.sidebar.subheader("🔢 Numeric Attributes")

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
st.sidebar.subheader("📏 Marker Size")
available_numeric_fields = [field for field in numeric_fields if field in df.columns]
size_field = st.sidebar.selectbox(
    "Size markers by:",
    options=['Fixed Size'] + available_numeric_fields,
    index=0,
    help="Choose a numerical field to control marker size"
)

# Show active filters in sidebar
if active_filters:
    st.sidebar.subheader("🎯 Active Filters")
    for filter_info in active_filters:
        st.sidebar.write(f"• {filter_info}")
else:
    st.sidebar.info("No filters applied - showing all events")

# Reset filters button
if st.sidebar.button("🔄 Reset All Filters"):
    st.rerun()

# Clean coordinate data for filtered results
filtered_map_data = filtered_df[['latitude', 'longitude']].dropna()
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

# Main content
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Event Locations")
    
    if len(filtered_map_data) > 0:
        # Configure layer based on size selection
        if size_field == 'Fixed Size':
            layer = pdk.Layer(
                'ScatterplotLayer',
                data=filtered_map_data,
                get_position='[longitude, latitude]',
                get_color='[200, 30, 0, 160]',
                get_radius=50,
                radius_min_pixels=3,
                radius_max_pixels=15,
            )
        else:
            layer = pdk.Layer(
                'ScatterplotLayer',
                data=filtered_map_data,
                get_position='[longitude, latitude]',
                get_color='[200, 30, 0, 160]',
                get_radius=size_field,
                radius_scale=10,
                radius_min_pixels=3,
                radius_max_pixels=50,
            )
        
        st.pydeck_chart(pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=CENTER_LAT,
                longitude=CENTER_LON,
                zoom=12
            ),
            layers=[layer]
        ))
    else:
        st.warning("No events match the selected filters.")

with col2:
    st.subheader("📊 Summary")
    
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
with st.expander("📋 View Filtered Data"):
    if len(filtered_df) > 0:
        st.dataframe(filtered_df, use_container_width=True)
        
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