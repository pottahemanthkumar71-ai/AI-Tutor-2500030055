from fastapi import FastAPI
import uvicorn

klu = FastAPI(title="AI-Tutor",
              description="AI-Tutor pbl project",
              version="1.0.0")

@klu.get("/")
def home():
    return {"message":"Welcome to AI-Tutor project"}

@klu.get("/demo")
def demo():
    return {"message":"KL University"}

@klu.get("/askquestion")
def ask():
    return {"message":"What is LLM ?","Answer":"Large Language Modle"}

@klu.get("/student")
def std():
    return {"id":11,"name":"Ram","gender":"Male","course":"DSA"}

@klu.get("/students")
def getstds():
    return [{"id":11,"name":"Ram","gender":"Male","course":"DSA"},
            {"id":15,"name":"Rahul","gender":"Male","course":"DSA"},
            {"id":18,"name":"Rani","gender":"Female","course":"DSA"}]


if __name__ == "__main__":
    uvicorn.run("Main:klu", host="127.0.0.1", port=2027, reload=True)
   