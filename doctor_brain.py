import os
import base64
from groq import Groq

# Set up GROQ API key from environment variables
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set.")

# Function to convert an image to a base64 encoded string
def encode_image(image_path):
    """Encodes a local image file to a base64 string."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file at {image_path} was not found.")
        return None

# Function to analyze an image with a text query using a Groq multimodal LLM
def analyze_image_with_query(query, model, encoded_image):
    """
    Sends a text query and an encoded image to a Groq multimodal model for analysis.
    
    Args:
        query (str): The text question to ask about the image.
        model (str): The name of the Groq multimodal model to use.
        encoded_image (str): The base64 encoded image string.
        
    Returns:
        str: The text response from the model, or None on error.
    """
    if not encoded_image:
        return "Image encoding failed. Please check the image path."

    client = Groq()
    
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]
    
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred during the API call: {e}")
        return None

# Main execution
if __name__ == "__main__":
    # Change this to the path of your image file ---
    image_path = "acne.jpg" 
    
    query = "Is there something wrong with my face?"
    model = "meta-llama/llama-4-scout-17b-16e-instruct"

    # Encode the image
    encoded_image = encode_image(image_path)
    
    # Call the analysis function and get the response
    response_text = analyze_image_with_query(query, model, encoded_image)

    # Print the final response
    if response_text:
        print("Model Response:")
        print(response_text)
