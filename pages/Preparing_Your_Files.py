import streamlit as st

st.set_page_config(page_title="Preparing Your Files")
st.title("Preparing Your Files for Cost Prediction")

st.markdown("""
## How to Prepare Your CSV Files

To use the AI POC Demo for cost prediction, your CSV files must be formatted correctly. Below are the necessary columns and an example of how your file should look.

### Required Columns:
- **BidDescription**: Description of the bid item.
- **OrigContractUnits**: Original contract units.
- **UM**: Unit of measurement.
- **udProjectType**: Project type (can be added using the POC if not already in the file).

### Example:
```csv
BidDescription,OrigContractUnits,UM,udProjectType
OVERHEAD,0,LS,Roadway Improvement
LEAD COMPLIANCE PLAN,0,LS,Roadway Improvement
CONSTRUCTION AREA SIGNS,0,LS,Roadway Improvement
...
```

### Steps to Prepare Your Files:
1. **Ensure the CSV file has the required columns**:
    - You can create or edit the CSV file using a spreadsheet application like Microsoft Excel or Google Sheets.
2. **Add or Update the `udProjectType` Column**:
    - If your file does not have the `udProjectType` column, you can use the AI POC Demo to add it.
    - Choose from the available project types: "Roadway Improvement," "Heavy Highway," "Utility - Water & Other," or "Polyester Overlay."

By following these steps, you'll ensure your files are ready for cost prediction using the AI POC Demo.
""")