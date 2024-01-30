import streamlit as st
import snowflake.connector
import pandas
import requests

# Snowflake connection parameters
conn_params = {
    'user': 'PrudhviCherukuri',
    'password': 'Cprudhvi@5533',
    'account': 'https://le34532.eu-north-1.aws.snowflakecomputing.com',
    'warehouse': 'compute_wh',
}

# Connect to Snowflake
conn = snowflake.connector.connect(**st.secrets["snowflake"])

# Streamlit app
st.title("Snowflake Schema Explorer")

# Get the selected database
selected_db = st.selectbox("Select Database:", ["Database1", "Database2", "Database3"])  # Replace with your list of databases

# Get the selected schemas
selected_schemas = st.multiselect("Select Schemas:", ["Schema1", "Schema2", "Schema3"])  # Replace with your list of schemas

# Create a Snowflake cursor
cursor = conn.cursor()

# Fetch tables for selected schemas
selected_tables = []
for schema in selected_schemas:
    cursor.execute(f"SHOW TABLES IN SCHEMA {schema}")
    tables = cursor.fetchall()
    selected_tables.extend([(schema, table[1]) for table in tables])

# Close the cursor
cursor.close()

# Display the list of tables as a multi-selectable list
selected_tables = st.multiselect("Select Tables:", [f"{schema}.{table}" for schema, table in selected_tables])

# Close the connection
conn.close()

# Sidebar for target database and schema selection
st.sidebar.title("Transfer Configuration")
target_db = st.sidebar.selectbox("Select Target Database:", ["TargetDB1", "TargetDB2", "TargetDB3"])  # Replace with your list of target databases
target_schema = st.sidebar.selectbox("Select Target Schema:", ["TargetSchema1", "TargetSchema2", "TargetSchema3"])  # Replace with your list of target schemas

# Button to initiate transfer
if st.button("Transfer Tables"):
    # Add transfer logic here
    st.write(f"Transferring selected tables to {target_db}.{target_schema}")

# Optionally, you can add a confirmation button to execute the transfer
if st.sidebar.button("Confirm Transfer"):
    # Add confirmation logic and transfer execution here
    st.write(f"Confirmed transfer to {target_db}.{target_schema}")

# Optionally, you may want to add a reset button to clear selections
if st.sidebar.button("Reset Selections"):
    st.experimental_rerun()
