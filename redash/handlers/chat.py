from flask import request, jsonify
from redash.handlers.base import (
    BaseResource
)
import os
from openai import OpenAI

# Import Langchain LIbraries
from dotenv import load_dotenv
from langchain.agents import create_sql_agent 
from langchain.agents.agent_toolkits import SQLDatabaseToolkit 
from langchain.sql_database import SQLDatabase 
from langchain.llms.openai import OpenAI 
from langchain.agents import AgentExecutor 
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

VARIABLE_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(
  api_key=VARIABLE_KEY
)

class ChatResource(BaseResource):
    def post(self):
        try:
            value = request.get_json() #This line retrieves data from a request (likely from a web page or application). The .get_json() part specifically extracts the data in a format called JSON, which is a way of structuring information.
            question = value.get('question')
            
            ######## Make Changes here i.e intergrating it with a database #############
            
            # - Database Connection
            # Load environment variables from .env
            load_dotenv()

            # Construct PostgreSQL URI using environment variables
            pg_uri = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
            
            # Setting up the database connection
            db = SQLDatabase.from_uri(pg_uri)
            
            # Setting up LLM
            OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
            
            # Defining our LLM model
            gpt = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name='gpt-3.5-turbo')
            
            # Defining our agent toolkit
            toolkit = SQLDatabaseToolkit(db=db, llm=gpt)
            
            # Create our agent executor
            agent_executor = create_sql_agent(
                llm=gpt,
                toolkit=toolkit,
                verbose=True,
                agent_type=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            )
            
            # Prompt Engineering
            def create_chat_prompt_template():
                return ChatPromptTemplate.from_messages(
                    [
                        ("system", "Welcome to the Redash chat add-on. I can help you extract insights from your Redash dashboards and connected databases using natural language."),
                        ("human", "{input}"),
                        ("ai", "{sql_query}"),
                        ("ai", "{sql_result}"),
                        ("ai", "{answer}"),
                    ]
                )

            def create_few_shot_chat_message_prompt_template():
                return FewShotChatMessagePromptTemplate(
                    example_prompt=ChatPromptTemplate.from_messages(
                        [
                            ("human", "How many views does the city of New York have?"),
                            ("ai", "SELECT views FROM cities WHERE city_name = 'New York';"),
                        ]
                    ),
                    examples=[
                        {"input": "How many views does the city of New York have?", "output": "SELECT views FROM cities WHERE city_name = 'New York';"},
                        {"input": "What is the average view duration for videos on the platform?", "output": "SELECT AVG(average_view_duration) FROM content_type;"},
                        {"input": "What is the most popular device type used to watch videos on the platform?", "output": "SELECT device_type FROM device_type ORDER BY views DESC LIMIT 1;"},
                    ],
                ) 
                
                def extract_answer(chat_prompt):
                    return chat_prompt.get_message("ai", 4).content

                def prepare_response(answer):
                    return {"answer": answer}

                def send_response(response):
                    return jsonify(response), 200   
                
                answer = extract_answer(chat_prompt)
                response = prepare_response(answer)
                return send_response(response)
            
        except Exception as error:
            print(error)
            return jsonify({"error": "An error occurred"}), 500                         
            