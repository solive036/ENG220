import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

        # Plotting water level over time
        st.write("### Water Level Over Time")
        fig, ax = plt.subplots(figsize=(12, 6))
        row_numbers = range(1, len(data) + 1)  # Generate row indices
        for column in water_columns:
            ax.plot(row_numbers, data[column], label=column)
        ax.set_xlabel("Row Number")
        ax.set_ylabel("Water Level in Feet")
        ax.legend(title="Water Data Columns")
        ax.grid(True)
        st.pyplot(fig)

        # Generate correlation heat map
        st.write("### Correlation Heat Map")
        correlation_matrix = data[water_columns].corr()  # Calculate correlation matrix for selected columns
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        ax.set_title("Correlation Between Water Data Columns")
        st.pyplot(fig)

        # Add histograms for each water data column
        st.write("### Distribution of Water Levels")
        for column in water_columns:
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.hist(data[column], bins=20, alpha=0.7, color='blue', edgecolor='black')
            ax.set_title(f"Distribution of {column}")
            ax.set_xlabel("Water Level in Feet")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)

except FileNotFoundError:
    st.error(f"The file `{file_name}` was not found. Please ensure it is in the same directory as this script.")
except Exception as e:
    st.error(f"An error occurred: {e}")

