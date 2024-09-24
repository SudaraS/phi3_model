import subprocess

# Function to query the phi3 model through Ollama
def query_phi3(prompt):
    # Call the Ollama CLI and pass the prompt to it directly as input
    command = ["ollama", "run", "phi3"]
    
    # Use subprocess to send the prompt as input to the command
    result = subprocess.run(command, input=prompt, capture_output=True, text=True)
    
    # Return the result from the model
    return result.stdout.strip()

# Function to read prompts from a text file
def read_prompts(file_path):
    with open(file_path, 'r') as file:
        # Read all lines and strip any leading/trailing whitespace characters
        prompts = [line.strip() for line in file.readlines()]
    return prompts

# Function to write the responses to a text file
def write_responses(responses, file_path):
    with open(file_path, 'w') as file:
        for response in responses:
            file.write(response + '\n')

def main():
    # Define file paths
    prompt_file = "prompts.txt"
    response_file = "responses.txt"

    # Read prompts from the prompt file
    prompts = read_prompts(prompt_file)

    # Store responses in a list
    responses = []

    # Iterate over the prompts and query the model
    for prompt in prompts:
        response = query_phi3(prompt)
        # Format the response and store it
        formatted_response = f"Prompt: {prompt}\nResponse: {response}\n"
        responses.append(formatted_response)

    # Write the responses to the response file
    write_responses(responses, response_file)

if __name__ == "__main__":
    main()
