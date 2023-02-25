import streamlit as st
import openai
import os

# Set up OpenAI API credentials
openai.api_key = "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"

# Define function to generate response for a single prompt
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Define function to process uploaded text file and generate responses
def process_file(file):
    content = file.read()
    content_string = content.decode("utf-8")
    prompts = content_string.splitlines()
    responses = []
    for prompt in prompts:
        response = generate_response(prompt)
        responses.append(response)
    return responses

# Define streamlit app
def main():
    st.title("PenCrafter - Best AI Writing Tool")

    # Upload file
    file = st.file_uploader("Upload a text file containing prompts", type="txt")

    # Generate responses
    if file is not None:
        st.write("Generating responses...")
        responses = process_file(file)

        # Display and download responses
        for i, response in enumerate(responses):
            st.write(f"Prompt {i+1}")
            filename = f"response_{i+1}.txt"
            with open(filename, "w") as f:
                f.write(response)
            st.download_button("Download response", response)

if __name__ == "__main__":
    main()
