import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Penguine Explorer",
    page_icon="🐧",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

st.title('Exploratory Penguine Data Analysis with Streamlit')
st.title('This Streamlit application reads the penguin dataset and displays interesting data visualizations!')

def load_data():
    penguins = sns.load_dataset('penguins')
    return penguins

penguins = load_data()

# Display dataset
st.subheader('Penguin Dataset')
st.write(penguins)

# Filter data
st.sidebar.header('Filter Data')
selected_column = st.sidebar.selectbox('Select a column to filter:', penguins.columns)
if penguins[selected_column].dtype == 'float64':
    min_value = penguins[selected_column].min()
    max_value = penguins[selected_column].max()
    selected_range = st.sidebar.slider(f'Select range for {selected_column}:', min_value, max_value, (min_value, max_value))
    filtered_data = penguins[(penguins[selected_column] >= selected_range[0]) & (penguins[selected_column] <= selected_range[1])]
else:
    selected_value = st.sidebar.text_input(f'Enter value for {selected_column}:')
    filtered_data = penguins[penguins[selected_column] == selected_value]

# Display filtered data
st.subheader('Filtered Data')
st.write(filtered_data)

# Visualizations
st.header('Data Visualizations')

# Histogram
st.subheader('Histogram')
fig, ax = plt.subplots()
sns.histplot(data=penguins, x='flipper_length_mm', kde=True, ax=ax)
st.pyplot(fig)

# Scatter plot
st.subheader('Scatter Plot')
fig, ax = plt.subplots()
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species', ax=ax)
st.pyplot(fig)