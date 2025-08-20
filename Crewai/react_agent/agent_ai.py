import html
import re
import httpx
import google.generativeai as genai
import os
from dotenv import load_dotenv


def get_summary(query):
    """Fethes a short summary from wikipedia based on the search term."""
    response = httpx.get('https://en.wikipedia.org/w/api.php', params={
        "action" : "query",
        "list" : "search",
        "srsearch" : query,
        "format" : "json"
    })

    raw_snippet = response.json()['query']['search'][0]['snippet']

    # remove html tags
    clean_snippet = re.sub(r'<[^>]+>', '', raw_snippet)

    # Unescape HTML entities (e.g., &quot; -> ", &amp; -> &)
    text_snippet = html.unescape(clean_snippet)

    return text_snippet

# summary = get_summary("Elon Musk")
# print(summary)

def quick_math(expr):
    """Evaluates a math expression given as a string"""
    return eval(expr)

# result = quick_math("2 + 1 - 1 / 1 * 7 + 9 / 2")
# print(result)

def fetch_todo():
    """Fetches a placeholder to-do item from a fake API"""
    url = "https://jsonplaceholder.typicode.com/todos/1"
    res = httpx.get(url)

    if res.status_code == 200:
        return res.json()

    else:
        return {"error" : "could not fetch"}
    
# print(fetch_todo())


load_dotenv()

class Chat:
    """Wrapper class for Google's Gemini API"""

    def __init__(self, api_key, system=""):
        self.system = system
        self.messages = []
        genai.configure(api_key=api_key)   # ✅ yeh sahi hai
        self.model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ Client nahi, GenerativeModel use karo

        if self.system:
            self.messages.append({"role": "system", "content": system})

    def __call__(self, message):
        if message:
            self.messages.append({"role": "user", "content": message})

        response = self.model.generate_content(message)  # ✅ send_message nahi, generate_content
        result = response.text

        self.messages.append({"role": "assistant", "content": result})
        return result
    

# test_chat = Chat(api_key=os.getenv("API_KEY"), system="You are a helpful assistant.")

# f1 = test_chat("What is the capital of india ?")
# print(f1)


# ReAct Agent, LLM
class ReActAgent:
    """
    A ReAct (Reasoning and Acting) agent that can use tools to answer questions.

    The agent follows the ReAct patterns:
    1. Reason about the task
    2. Act by calling appropriate tools
    3. Observe the results
    4. Repeat until the task is complete
    """

    def __init__(self, api_key):
        self.memory = [] # Agent Memory
        self.system_prompt = (
            "You are a helpful assistant. You can use the followig tools:\n"
            "- get_summary(query: str): to search wikipedia\n"
            "- quick_math(expr: str): to evaluate a math expression \n"
            "- fetch_todo(): to get a sample todo \n"
            "When you need to use a tool, respond with: Action: <tool_name>[<input>]\n"
            "Otherwise, respond normally as the assistant. \n"
        )

        self.chat = Chat(api_key=api_key, system=self.system_prompt)

    def __call__(self, message):
        """Process a user message and return a response, using tools if necessary"""
        full_input = "\n".join(self.memory + [f"User : {message}"]) # old memeory + new user message

        response = self.chat(full_input)

        self.memory.append(f"User : {message}")
        self.memory.append(f"Assistant: {response}")

        # Check id the response contains a tool invocation
        if response.startswith("Action:"):
            tool_call = re.match(r'Action:\s*(\w+)\[(.*?)\]', response)

            if not tool_call:
                return 'Invalid Tool Format.'

            tool_name, tool_arg = tool_call.group()
            result = self.invoke_tool(tool_name, tool_arg.strip())

            self.memory.append(f"Observation: {result}")

            # Recursive call to process the tool result
            return self(f"Observation: {result}")
        
        else:
            return response
        
    def invoke_tool(self, name, arg):
        """Execute a tool with the given argument"""
        try:
            if name == "get_summary":
                return get_summary(query=arg)
            elif name == "quick_math":
                return quick_math(expr=arg)
            elif name == "fetch_todo":
                return fetch_todo()
            else:
                return f"Unknown tool: {name}"
            
        except Exception as e:
            return f"Error executing {name}: {str(e)}"
        

def main():
    API_KEY = os.getenv('API_KEY')
    agent = ReActAgent(API_KEY)

    print("Welcome to the ReAct Agent! Type 'exit' to quit.")
    # print(agent("hello"))
    # print(agent("What is 2 + 1"))
    # print(agent("What is the capital of India ?"))

    Stop = True
    while Stop:
        question = input("Question: ")
        if question == 'exit':
            Stop = False
        else:
            print("ReAct Agent: ", agent(question))

if __name__ == '__main__':
    main()
