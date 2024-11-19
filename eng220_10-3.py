import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Water Data Time Series Viewer")

# Sidebar for file upload
st.sidebar.header("Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if uploaded_file:
    # Load the dataset
    try:
        # Read the Excel file
        data = pd.read_excel(uploaded_file)
        st.write("### Dataset Preview")
        st.dataframe(data.head())

        # Ensure the dataset has at least 6 columns (including time and water data columns)
        if len(data.columns) < 6:
            st.error("The dataset must have at least 6 columns (Time column + water data in columns 2-5).")
        else:
            # Automatically select the first column as time and columns 2-5 as water data
            time_column = data.columns[0]
            water_columns = data.columns[1:5]

            # Parse the time column as datetime
            try:
                data[time_column] = pd.to_datetime(data[time_column])
            except Exception as e:
                st.error(f"Error parsing time column: {e}")
                st.stop()

            # Plotting
            st.write("### Line Plot of Water Data Over Time")
            fig, ax = plt.subplots(figsize=(12, 6))
            for column in water_columns:
                ax.plot(data[time_column], data[column], label=column)
            ax.set_xlabel("Time")
            ax.set_ylabel("Water Data Values")
            ax.legend(title="Water Data Columns")
            ax.grid(True)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error loading dataset: {e}")
else:
    st.write("Please upload an Excel file to get started.")
