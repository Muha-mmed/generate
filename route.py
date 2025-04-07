from fastapi import APIRouter
import json
import random

router = APIRouter()

with open("mood.json") as mood_json:
    mood_data = json.load(mood_json)
    
with open("would_you.json") as would_you_json:
    would_you_data = json.load(would_you_json)
    

@router.get("/mood-base/{mood}")
def get_mood(mood: str):
    if mood not in mood_data:
        return {"error": "mood doesn't exist in memory"}
    quote = random.choice(mood_data[mood]["quotes"])
    song = random.choice(mood_data[mood]["songs"])
    return{
        "quote": quote,
        "songs": song
    }
    
@router.get("/would-you/{wouldYou}")
def get_would_you(wouldYou: str):
    if wouldYou not in would_you_data:
        return {"error": "mood doesn't exist in memory"}
    data = random.choice(would_you_data[wouldYou])
    return {
        "message": data
    }