from langchain.chains import LLMChain 
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os
from config import OPENAI_API_KEY

#Set OpenAI API Key 
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def generate_bond_recommendations(country, bond_types):
    # Prepare the prompt template for the model
    promtp_template = """
    You are a financial advisor. Based on the given country and bond types, recommend the top 5 bonds to buy with the name of the company or government. 
    Provide recommendations for the country: {country}
    Bond types: {bond_types}
    """

    prompt = prompt_template.format(country=country, bond_types=", ".join(bond_types))

    openai_model = OpenAI(temperature=0.7)

    chain = LLMChain(llm=openai_model, prompt=PromptTemplate(template=prompt, input_variables=["country", "bond_types"]))
    result = chain.run({"country": country, "bond_types": ", ".join(bond_types)})

    return result 
