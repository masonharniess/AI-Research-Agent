# AI-Research-Agent
A Python implementation of an AI agent which can provide responses to simple research queries provided by the user. 

The agent uses OpenAI's GPT-4o mini model by default. Other OpenAI models, or models from other providers (such as Anthropic) can be used with only small changes to `main.py`.
## Features
- Provide structured responses to written queries.
- Search the internet for information.
- Search Wikipedia for information. 
- Save response output to a file if requested by the user.

## Installation
1. Clone the repository to your desired location.

2. Navigate to the root directory. 

3. Create a `.env` file in the project root with your OpenAI or Anthropic key. Only a single provider's API key is necessary, though keys for both platforms can be obtained to switch between providers.
    ```
    OPENAI_API_KEY="your_api_key_here"
    ANTHROPIC_API_KEY="your_api_key_here"
    ```
    The API platforms for OpenAI and Anthropic can be found here:
    - [OpenAI API Platform](https://platform.openai.com/api-keys)
    - [Anthropic API Platform](http://console.anthropic.com/)

4. In the root directory, run the following command to create a virtual environment called `venv`.
    ```Python
    python3 -m venv venv
    ```

5. Enter the virtual environment with the following command.
    ```Python
    source ./venv/bin/activate
    ```

6. Install the dependencies listed in `requirements.txt`.
    ```Python
    pip install -r requirements.txt
    ```

## Usage
1. In your virtual environment, run the program with the following command.
    ```Python
    python3 main.py
    ```

> **Note**:
> At this stage, you may encounter a `NotOpenSSLWarning` warning. If so, this can be resolved by exiting the program and running the following commands in your virtual environment.
> ```Python
> pip uninstall urllib3 
> pip install 'urllib3<2.0'
> ```
>You can learn more about this issue on [Stack Overflow](https://stackoverflow.com/questions/76187256/importerror-urllib3-v2-0-only-supports-openssl-1-1-1-currently-the-ssl-modu).


2. When asked `What can I help you research?`, enter your desired topic of enquiry and press enter. 
    ```
    What can I help you research? Hammerhead sharks
    ```
3. To save the LLM's response to a text file, simply add this command onto your enquiry:
    ```
    What can I help you research? Hammerhead sharks, save to file
    ```
