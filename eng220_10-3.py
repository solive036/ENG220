import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("Water and Weather Data Viewer for New Mexico")

# Load the water dataset
water_file = "NewMexico_Data.xlsx"
# Load the weather dataset
weather_file = "weather_data.xlsx"

try:
    # Read the water dataset
    water_data = pd.read_excel(water_file)
    
    # Read the weather dataset
    weather_data = pd.read_excel(weather_file)

    # Ensure the water dataset has at least 5 columns
    if len(water_data.columns) < 5:
        st.error("The water dataset must have at least 5 columns (row index + water data in columns 2-5).")
    else:
        # Automatically use columns 2 through 5 as water data
        water_columns = water_data.columns[1:5]

        # Dropdown menu to select the type of data to view
        data_type = st.selectbox(
            "Select the type of data to view:",
            ["Water Data", "Weather Data"]
        )

        # If Water Data is selected
        if data_type == "Water Data":
            # Dropdown menu to select the type of plot for water data
            plot_type = st.selectbox(
                "Select the type of plot to view:",
                ["Water Level Over Time", "Correlation Heat Map", "Distribution of Water Levels"]
            )

            if plot_type == "Water Level Over Time":
                st.write("### Water Level Over Time")
                fig, ax = plt.subplots(figsize=(12, 6))
                row_numbers = range(1, len(water_data) + 1)  # Generate row indices
                for column in water_columns:
                    ax.plot(row_numbers, water_data[column], label=column)
                ax.set_xlabel("Row Number")
                ax.set_ylabel("Water Level in Feet")
                ax.legend(title="Water Data Columns")
                ax.grid(True)
                st.pyplot(fig)

            elif plot_type == "Correlation Heat Map":
                st.write("### Correlation Heat Map")
                correlation_matrix = water_data[water_columns].corr()  # Calculate correlation matrix for selected columns
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
                ax.set_title("Correlation Between Water Data Columns")
                st.pyplot(fig)

            elif plot_type == "Distribution of Water Levels":
                st.write("### Distribution of Water Levels")
                for column in water_columns:
                    fig, ax = plt.subplots(figsize=(8, 4))
                    ax.hist(water_data[column], bins=20, alpha=0.7, color='blue', edgecolor='black')
                    ax.set_title(f"Distribution of {column}")
                    ax.set_xlabel("Water Level in Feet")
                    ax.set_ylabel("Frequency")
                    st.pyplot(fig)

        # If Weather Data is selected
        elif data_type == "Weather Data":
            # Dropdown menu to select the weather data to view
            weather_plot_type = st.selectbox(
                "Select the weather data to plot:",
                ["Average Temperature", "Precipitation"]
            )

            if weather_plot_type == "Average Temperature":
                st.write("### Average Temperature Over Time")
                fig, ax = plt.subplots(figsize=(12, 6))
                row_numbers = range(1, len(weather_data) + 1)  # Generate row indices
                ax.plot(row_numbers, weather_data.iloc[:, 0], label="Average Temperature", color="red")
                ax.set_xlabel("Row Number")
                ax.set_ylabel("Average Temperature (°F)")
                ax.legend()
                ax.grid(True)
                st.pyplot(fig)

            elif weather_plot_type == "Precipitation":
                st.write("### Precipitation Over Time")
                fig, ax = plt.subplots(figsize=(12, 6))
                row_numbers = range(1, len(weather_data) + 1)  # Generate row indices
                ax.plot(row_numbers, weather_data.iloc[:, 2], label="Precipitation", color="blue")
                ax.set_xlabel("Row Number")
                ax.set_ylabel("Precipitation (inches)")
                ax.legend()
                ax.grid(True)
                st.pyplot(fig)

except FileNotFoundError as e:
    st.error(f"File not found: {e.filename}. Please ensure it is in the same directory as this script.")
except Exception as e:
    st.error(f"An error occurred: {e}")
