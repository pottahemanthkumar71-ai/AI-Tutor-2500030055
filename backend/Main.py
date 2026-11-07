from fastapi import FastAPI

klu = FastAPI(titel="AI-Tutor",
              description="AI-Tutor pbl project",
              version="1.0.0",)

@klu.get("/")
def home():
    return {"message":"Welcome to AI-Tutor project"}

@klu.get("/demo")
def demo():
    return {"message":"KL University"}

@klu.get("/askquestion")
def ask():
    return {"message":"What is LLM ?","Answer":"Large Language Modle"}
