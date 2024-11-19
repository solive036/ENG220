import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Water Data Viewer for New Mexico")

# Load the dataset directly (assuming it is in the same directory)
file_name = "NewMexico_Data.xlsx"

try:
    # Read the Excel file
    data = pd.read_excel(file_name)
    st.write(f"### Dataset: {file_name}")
    st.dataframe(data.head())

    # Ensure the dataset has at least 5 columns
    if len(data.columns) < 5:
        st.error("The dataset must have at least 5 columns (row index + water data in columns 2-5).")
    else:
        # Automatically use columns 2 through 5 as water data
        water_columns = data.columns[1:5]

        # Plotting
        st.write("### Line Plot of Water Data Against Row Number")
        fig, ax = plt.subplots(figsize=(12, 6))
        row_numbers = range(1, len(data) + 1)  # Generate row indices
        for column in water_columns:
            ax.plot(row_numbers, data[column], label=column)
        ax.set_xlabel("Row Number")
        ax.set_ylabel("Water Data Values")
        ax.legend(title="Water Data Columns")
        ax.grid(True)
        st.pyplot(fig)

except FileNotFoundError:
    st.error(f"The file `{file_name}` was not found. Please ensure it is in the same directory as this script.")
except Exception as e:
    st.error(f"An error occurred: {e}")

