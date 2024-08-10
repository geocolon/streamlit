import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Data Dashborad')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    # st.write('File uploaded...')
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Data Visualization")
    st.write("Correlation Matrix")  

    st.subheader("Filter Data")
    colums = df.columns.tolist()
    selected_column = st.selectbox("Select Columns to filter by", colums)
    unique_values = df[selected_column].unique()
    selected_values = st.selectbox("Select Values", unique_values)

    filtered_df = df[df[selected_column] == selected_values]
    st.write(filtered_df)

    st.subheader("Data Visualization")
    x_columns = st.selectbox("Select x-axis", colums)
    y_columns = st.selectbox("Select y-axis", colums)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_columns)[y_columns])
        # fig, ax = plt.subplots()
        # ax.scatter(df[x_columns], df[y_columns])
        # ax.set_xlabel(x_columns)
        # ax.set_ylabel(y_columns)
        # st.pyplot(fig)
else:
    st.write('No file uploaded...')