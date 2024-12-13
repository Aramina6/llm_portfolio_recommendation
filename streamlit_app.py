import streamlit as st
from langchain_code import generate_bond_recommendations

# Streamlit App Interface 
def main(): 
  st.title("Financial Portfolio Assistant")

  st.sidebar.header("User Input")
  # Country selection
  country = st.sidebar.selectbox("Select Country", ["USA", "Germany", "UK", "France", "Canada"])

  # Bond type selection
  bond_types = st.sidebar.multiselect("Select Bond Types", ["Government Bonds", "Corporate Bonds", "Municipal Bonds", "High Yield Bonds", "Treasury Bonds"])

  # Button to generate recommendation
  if st.sidebar.button("Get Bond Recommendations"): 
    if country and bond_types: 
      with st.spinner('Fetching bond recommendations...'): 
        # Call Langchain function to get recommendations
        bond_recommendations = generate_bond_recommendations(country, bond_types)
        st.success("Top 5 Bonds to Buy:")

        # Display recommendations
        st.write(bond_recommendations)
    else: 
      st.error("Please select both a country and bond types.")

if __name__ == "__main__": 
  main()
