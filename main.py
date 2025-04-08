from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

# Create a search tool using Serper API
search_tool = SerperDevTool()

researcher = Agent(
    role="Senior Data Researcher",
    goal="Uncover cutting-edge developments in Clinical trials",
    backstory="""You are a seasoned researcher with a knack for uncovering the latest
    developments in Clinical Trials. Known for your ability to find the most relevant
    information and present it in a clear and concise manner.""",
    verbose=True,
    llm="gpt-4o",
    allow_delegation=False,
    tools=[search_tool]
)

writer=Agent(
    role="Tech content strategist",
    goal="Write a concise and clear report based on the research findings",
    backstory="""You are a seasoned writer with a knack for uncovering the latest
    developments in Clinical Trials. Known for your ability to find the most relevant
    information and present it in a clear and concise manner.""",
    verbose=True,
    allow_delegation=False,
    llm="gpt-4o"
)

#Tasks

task1 = Task(
    title="Research latest developments in Clinical trials",
    description="Conduct a comprehensive analysis of the latest developments in Clinical trials",
    expected_output="A comprehensive report on the latest developments in Clinical trials",
    priority=1,
    agent=researcher
)

task2 = Task(
    title="Write a concise and clear report based on the research findings",
    description="Write a concise and clear report based on the research findings, the post should be imformative and concise, Make it sound cool and avoid complex words",
    expected_output="A concise and clear report on clinical trials that sounds cool and avoids complex words",
    priority=1,
    agent=writer
)

#Crew

crew = Crew(
    name="Clinical Trials Research Crew",
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True
)

#Run

result = crew.kickoff()
print(result)