import streamlit as st


st.set_page_config(
    page_title = "MapBox API Demo",
    page_icon = "🗺️",
)

st.write("# Welcome MapBox API Demo! 🗺️")

st.sidebar.write("")


st.markdown(
    """
    [Streamlit](https://streamlit.io) is an open-source app framework built specifically for Machine Learning and Data Science projects.
    """)

st.image("./media/streamlit_logo.png", width = 400)

st.markdown(
    """
    [Mapbox](https://www.mapbox.com/) is an American provider of custom online maps for websites and applications.

    We would like to demostrate existing map service APIs provided by MapBox and see how we could use these powerful services to create Geo-based web applications.
    """
)

st.image("./media/mapbox_logo.png", width = 400)