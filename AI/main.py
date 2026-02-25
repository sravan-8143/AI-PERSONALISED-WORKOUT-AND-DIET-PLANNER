from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    age: int
    height: float
    weight: float
    goal: str
    diet_type: str
    budget: str
    workout_place: str


def calculate_bmi(weight, height):
    height_m = height / 100
    return round(weight / (height_m ** 2), 2)


@app.get("/")
def home():
    return {"message": "AI Fitness Planner API is running"}


@app.post("/generate-plan")
def generate_plan(user: UserInput):

    bmi = calculate_bmi(user.weight, user.height)

    if user.goal == "Weight Loss":
        workout = "Cardio + HIIT + Full body workouts"
    elif user.goal == "Muscle Gain":
        workout = "Chest, Back, Legs, Shoulders split"
    else:
        workout = "Yoga + Light cardio"

    if user.diet_type == "Vegetarian":
        diet = "Oats, Dal, Rice, Vegetables, Fruits"
    else:
        diet = "Eggs, Chicken, Rice, Vegetables"

    return {
        "BMI": bmi,
        "Workout Plan": workout,
        "Diet Plan": diet
    }