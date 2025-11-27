import streamlit as st
import pandas as pd

# Force browser cache refresh [2]
st.markdown("""
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/RichardFreedman/Encoding_Music/main/06_SoundMap/bicomap.csv')
    if 'time' in df.columns:
        df = df.drop('time', axis=1)
    return df.dropna(subset=['latitude', 'longitude'])

st.header('Bi-Co Sound Survey Computational Essay')
st.markdown('By Logan Griffin, Luke Sheppard, Reed Solomon, and Jade Yu')
st.markdown('Sounds of Silence: A Sound Survey of the Bi-Co During Finals Week')

# Load data
full_data = load_data()

# Sidebar
st.sidebar.write("Filter Data")
volume_range = st.sidebar.slider('Maximum Volume Level', 0, 10, 10)
filtered_data = full_data[full_data['volume'] <= volume_range]

show_data = st.sidebar.checkbox('Show Filtered Data', value=False)

if show_data:
    st.dataframe(filtered_data)

# Map section
st.subheader("Sound Survey Map")

if len(filtered_data) > 0:
    # Debug info
    st.write(f"📍 **Data Summary:**")
    st.write(f"- Total points: {len(filtered_data)}")
    st.write(f"- Latitude range: {filtered_data['latitude'].min():.4f} to {filtered_data['latitude'].max():.4f}")
    st.write(f"- Longitude range: {filtered_data['longitude'].min():.4f} to {filtered_data['longitude'].max():.4f}")
    
    # Simple map attempt
    map_data = filtered_data[['latitude', 'longitude']].copy()
    
    try:
        st.map(map_data)
        st.success("✅ Map should be visible above")
    except Exception as e:
        st.error(f"❌ Map failed: {e}")
        
        # Fallback: Show data in table with Google Maps links
        st.warning("Map failed to render. Using table view instead:")
        
        display_data = filtered_data.copy()
        display_data['Google_Maps_Link'] = display_data.apply(
            lambda row: f"https://maps.google.com/?q={row['latitude']},{row['longitude']}", 
            axis=1
        )
        
        st.dataframe(
            display_data[['location', 'volume', 'latitude', 'longitude', 'Google_Maps_Link']],
            column_config={
                "Google_Maps_Link": st.column_config.LinkColumn("View on Google Maps")
            }
        )

else:
    st.warning("No data to display")

# Troubleshooting section
with st.expander("🔧 Map Troubleshooting"):
    st.markdown("""
    **If the map is still not visible, try these steps:**
    
    1. **Hard refresh your browser:** Press `Ctrl+Shift+R` (Windows/Linux) or `⌘+Shift+R` (Mac)
    
    2. **Try a different browser:** Chrome, Firefox, Safari, or Edge
    
    3. **Clear browser cache completely:**
       - Chrome: Settings → Privacy → Clear browsing data
       - Firefox: Settings → Privacy → Clear Data
    
    4. **Try incognito/private mode**
    
    5. **Run Streamlit on a different port:**
       ```bash
       streamlit run your_app.py --server.port=8502
       ```
    
    6. **Check your Streamlit version:**
    """)
    
    st.code(f"Streamlit version: {st.__version__}")
    
    st.markdown("""
    7. **If you're on a corporate network:** The firewall might be blocking map tiles
    
    8. **Try the Google Maps links in the table above** as an alternative
    """)