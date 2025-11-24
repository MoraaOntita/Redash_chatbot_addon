from langchain.sql_database import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain_groq import ChatGroq

def answer_question(question, pg_uri, groq_api_key):
    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model="llama3-70b-8192",
        temperature=0,
    )

    db = SQLDatabase.from_uri(pg_uri)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    return agent.run(question)
