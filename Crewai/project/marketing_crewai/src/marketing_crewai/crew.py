from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool


class MarketingCrew(CrewBase):

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher_agent'],
            tools=[SerperDevTool()]
        )
    
    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_agent'],
            verbose=True,
        )
    
    @agent
    def reviewer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['reviewer_agent'],
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher_agent,
            tools=[SerperDevTool()],
            verbose=True
        )
    
    @task
    def writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['writer_task'],
            agent=self.writer_agent,
            output_file='output.md',
            verbose=True
        )
    
    @task
    def reviewer_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewer_task'],
            agent=self.reviewer_agent,
            output_file='output.md',
            verbose=True
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential
        )
