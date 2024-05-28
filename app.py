import streamlit as st
import pandas as pd
import requests
import json
import io

API_ENDPOINT = "***REMOVED***"

def main():
    st.title("Myers and Sons AI POC Demo")

    uploaded_file = st.file_uploader("Select a bid item list to get cost prediction! :building_construction:", type="csv")
    
    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        # Optional: Choose Project Type
        project_type = st.selectbox(
            "Choose Project Type (Optional)",
            ["", "Roadway Improvement", "Heavy Highway", "Utility - Water & Other", "Polyester Overlay"]
        )
        
        if project_type:
            # Check if 'udProjectType' column is present
            if 'udProjectType' not in df.columns:
                df['udProjectType'] = project_type
                st.write(f"'udProjectType' column added with value '{project_type}'")
            else:
                st.warning("'udProjectType' column already exists in the CSV.")
        
        # Display the DataFrame
        st.write("Processed CSV file:")
        st.write(df)

        # Convert DataFrame to CSV content
        csv_content = df.to_csv(index=False)

# Prepare the JSON payload
        json_payload = json.dumps({"data": csv_content})

        # Send the CSV content to the API endpoint
        if st.button("Send to API"):
            json_payload = json.dumps({"data": csv_content})
            response = requests.post(API_ENDPOINT, data=json_payload, headers={"Content-Type": "application/json"})
            
            if response.status_code == 200:
                # Display the response from the API
                st.success("Request was successful!")
                st.write("Final Cost estimate from POC model:")
                
                # Parse the JSON response
                response_json = json.loads(response.text)

                # Get the body content and clean up additional escaping
                body_content = response_json.get('body', '')

                # Remove any escaped characters like \n and \\
                cleaned_body_content = body_content.encode().decode('unicode_escape')

                # Remove leading and trailing quotes if any
                cleaned_body_content = cleaned_body_content.strip('"').strip("\n")
                
                st.write('**${:,.2f}**'.format(float(cleaned_body_content)))
            else:
                st.error(f"Request failed with status code {response.status_code}")
                st.write(response.text)
    st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmFzVjIsqmhfBlJh8Lj_2l0NIpSA9Y2Z-81xkTQO8pnQ&s")
    st.sidebar.title("Myers and Sons - Construction Cost Estimation System - POC Demo")
    st.sidebar.markdown("""
## Welcome to the Construction Cost Estimation System - POC Demo

This demo application demonstrates AI and Machine Learning's capability to generate fairly accurate predictions based on minimal training data. 

The AI is trained on Caltrans' public bid item sheet (item description, unit of measurement, and suggested amount) and project type to generate final costs.

You can upload a CSV file representing the bid item sheet, optionally add a project type to your data if it has not been specified, and send the processed CSV to an API Gateway endpoint for inference.

Nobious have provided some CSV files you can use for this demo.

#### Steps to Use the Demo:
1. **Upload a CSV File**: Use the file uploader to select and upload your CSV file.
2. **Choose Project Type (Optional)**: If the CSV does not already contain a `udProjectType` column, you can choose a project type to add it.
    - Available options:
        - Roadway Improvement
        - Heavy Highway
        - Utility - Water & Other
        - Polyester Overlay
3. **Send to API**: Click the "Send to API" button to send the processed CSV content to the specified API Gateway endpoint.
4. **View API Response**: The response from the API will be displayed in the application.
""")

if __name__ == "__main__":
    main()