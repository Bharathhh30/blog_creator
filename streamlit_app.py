from dotenv import load_dotenv
load_dotenv()  # load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from googletrans import Translator

# Initialize Google API key for translation
translator = Translator()

# Configure Google API for OpenAI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API And get response
def get_gemini_response(image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt, image[0]])
    return response.text

# Function to set up image data
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="Wizz Ai Lite")
st.header("The AI content creator You all NEED :sparkles:")

# Define input prompt
input_prompt = """
Engaging Prompt for Image-Based Content Generation

Catchy Title: Let's Create Magic with Your Image!

Informative Introduction:
Welcome to a journey through the captivating world of [insert topic related to the image]. Bursting with dynamism and endless possibilities, [describe the topic and its allure]. Today, let's delve deep into the heart of [mention a specific aspect of the topic reflected in the image title]. Our gateway? The mesmerizing photo titled "[image title]". It encapsulates the very essence of [explain how the image title mirrors the topic's essence].

Personal Experience:
As a [your profession/background related to the topic], my fascination with [mention something specific related to the image] knows no bounds. Recently, [share a brief personal anecdote tied to the image title]. This profound experience not only fueled my passion for [mention your passion related to the topic] but also ignited the spark for this blog post.

Recipe and Instructions (Optional):
If the image unveils a culinary masterpiece or a creative process:

Let's embark on a culinary adventure inspired by "[image title]". Here's a step-by-step recipe to recreate this delectable [describe the creation/dish] in the comfort of your kitchen:

[Provide clear instructions and ingredients list]

Variations and Suggestions:
The charm of [topic] lies in its boundless versatility. While we've outlined a specific approach in the recipe, the canvas of creativity awaits your unique brushstrokes! Here are some suggestions to tailor your experience:

[Propose variations of ingredients or techniques]
[Offer ideas for dietary substitutions or preferences]
[Encourage readers to unleash their creativity and experiment]
Conclusion:
Whether you're a seasoned [your profession] or an eager novice, the realm of [topic] beckons you to explore its wonders. Remember, the key lies in [share a key takeaway or inspirational message linked to the topic]. So, gather your [mention relevant tools], ignite your imagination, and prepare to be enchanted by the infinite possibilities!"""

# File upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Language selection
# selected_language = st.selectbox("Select Language:", ["English", "Telugu", "Hindi"])

# Submit button
# Submit button


# If submit button is clicked
# Submit button
# Submit button with a unique key
# Submit button with a unique key


# Define function to generate content
def generate_content():
    # Display animated loader
    with st.empty():
        st.image("path_to_your_loader.gif", caption="Generating content...:sparkles:")

        # Generate content
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(image_data, input_prompt)

        # Display response
        st.subheader("The Response is:")
        st.write(response)

# Submit button with a unique key
if st.button("Generate:rocket:", key="generate_button"):
    generate_content()

# If "Generate More" button is clicked
if st.button("Generate More", key="generate_more_button"):
    generate_content()
