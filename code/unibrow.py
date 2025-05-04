'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

#First I am going to upload a file
#Then I am going to load it using my pandaslib.py
#Then I am going to select columns to display where I know that all will be selected as a default
#Next I am going to optionally filter rows using categorical(object) column and one of its unique values
#Lastly I am going to display the filtered dataframe and its .describe() output

st.title("UniBrow")
st.caption("The Universal data browser")

uploaded_file = st.file_uploader("Choose a data file", type=['csv', 'xls', 'xlsx', 'json'])

if uploaded_file is not None:
    #Determine file extension
    ext = pl.get_file_extension(uploaded_file.name)

    #Read file content into a datafram
    try:
        if ext == 'csv':
            df = pd.read_csv(uploaded_file)
        elif ext in ['xls', 'xlsx']:
            df = pd.read_excel(uploaded_file)
        elif ext == 'json':
            df = pd.read_json(uploaded_file)
        else:
            st.error(f"Unsupported file extension: {ext}")
            st.stop()
    except Exception as e:
        st.error(f"Failed to load file: {e}")
        st.stop()

#Column multi-select
    all_columns = pl.get_column_names(df)
    selected_columns = st.multiselect("Select columns to display", all_columns, default=all_columns)

#Optional row filter
    enable_filter = st.checkbox("Add a filter to a column")

    filtered_df = df #Start with full DataFrame

    if enable_filter:
        object_columns = pl.get_columns_of_type(df, 'object')
    if object_columns:
        selected_filter_col = st.selectbox("Select a column to filter by", object_columns)
        unique_values = pl.get_unique_values(df, selected_filter_col)
        if unique_values:
            selected_value = st.selectbox("Select a value", unique_values)
            filtered_df = df[df[selected_filter_col] == selected_value]
        else:
            st.warning(f"No unique values found in column '{selected_filter_col}'.")
    else:
        st.warning("No object columns available to filter.")

#Apply column filter
    if selected_columns:
        filtered_df = filtered_df[selected_columns]

#Display results
    st.subheader("Filtered DataFrame")
    st.dataframe(filtered_df)

    st.subheader("Descriptive Statistics")
    st.dataframe(filtered_df.describe())
else:
    st.info("Please upload a CSV, Excel, or JSON file.")
