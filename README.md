## Introduction
The Redash Chatbot LLM integrates OpenAI's ChatGPT model with your Redash dashboard, offering an innovative approach to data interaction. By enabling users to pose natural language queries, this plugin enhances the intuitiveness and user-friendliness of data exploration and analysis within Redash. The Chatbot LLM plugin supports conversational queries, automated data visualization, and smooth Redash integration. Additionally, it employs Docker for straightforward setup and deployment, ensuring users can easily begin utilizing the integration.

## Features
**Conversational Queries:** Users can engage with their Redash dashboards through natural language queries, simplifying the data exploration and analysis process to make it more intuitive and user-friendly.

**Automated Data Visualization:** Query results can be visualized directly within the chat interface, facilitating quicker data exploration and analysis.

**Integration with Redash:** Designed to seamlessly integrate with Redash, this project allows users to fully utilize the capabilities of this popular open-source data visualization tool.

## Requirements Before Installation:
- Node.js: This is a JavaScript runtime built on Chrome's V8 JavaScript engine.
- Yarn: This is a package manager that doubles down as project manager.
* Python: The project requires a Python version that is greater than or equal to 3.9 and less than or equal to 3.10.2.
* Poetry: This is a tool for dependency management and packaging in Python.

## Setup and Installation
1. Clone the Repository:
   
```bash
git clone git@github.com:10ac-group10/Redash_Chatbot_LLM.git
cd Redash_Chatbot_LLM
```

2. Create Virtual ENvironment and Install Dependencies:

   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # For Unix or MacOS
   venv\Scripts\activate     # For Windows
   pip install -r requirements.txt
   
   ```
3. Install Frontend Dependencies:

   ```bash
   poetry add openai
   ```

    ```bash
   yarn add react-icons
   ```

   ```bash
   yarn add react-syntax-highlighter
   ```
   
4. Environment Variables:
   Create a ```.env``` file in the root directory and add the following environment variables:   
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```
   
   Replace ```your_openai_api_key``` with your OpenAI API key.
   
   **Get your free OpenAI API key** - [OpenAI](https://platform.openai.com/docs/api-reference/authentication)
   
   **Note:** Follow the best practices by not commiting the .env file to the repository.

6. Build the application:
   Run the following commands to get the container up and running and start the application:
   ```bash
   yarn
   ```
   
   ```bash
   make build
   ```
   
   ```bash
   make compose_build
   ```
   
   ```bash
   make up
   ```
   
   If running all the above commands successfully, in future you can then simplify the process by running the below command to start the application.
   
   ```bash
   make run
   ``` 
