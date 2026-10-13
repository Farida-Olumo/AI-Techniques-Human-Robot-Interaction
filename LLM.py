import time
import sys
import json
import os
#from groq import Groq
#from furhat_remote_api import FurhatRemoteAPI

# --- 1. SETUP ---
# Ensure you use your specific Groq API Key here
#client = Groq(api_key="HERE")

#try:
    #furhat = FurhatRemoteAPI("localhost")
    #furhat.attend(user="CLOSEST")
    #print("SUCCESS: Groq-AI Personality Engine Online.")
except Exception as e:
    #print(f"ERROR: {e}. Ensure the Furhat SDK is running.")
    #sys.exit()

def get_groq_intelligence(user_input, topic):
    """
    Connects to Groq using Llama 3.3 for high-speed, 
    humanistic responses with synchronized gestures.
    """
    system_prompt = (
        "You are a compassionate, deeply humanistic research assistant named Furhat. "
        "You are currently in the office at the University of Waterloo interviewing Farida. "
        "Your tone is empathetic, professional, and intellectually curious. "
        "Provide thoughtful, non-generic responses that validate her work with social robots. "
        "RESPONSE FORMAT: You MUST respond in valid JSON with exactly two keys: 'speech' and 'gesture'. "
        "Gestures available: BigSmile, Wink, Nod, Surprise, Thoughtful, BrowFrown."
    )

    try:
        # Using the updated, supported Groq model
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Topic: {topic}. User said: {user_input}"}
            ],
            response_format={"type": "json_object"}
        )
        
        # Parse the AI's response
        ai_data = json.loads(completion.choices[0].message.content)
        return ai_data.get("speech"), ai_data.get("gesture", "Nod")
    
    except Exception as e:
        print(f"Connection Error: {e}")
        return "I'm reflecting on what you've shared. It sounds very meaningful.", "Thoughtful"

# --- 2. THE INTERVIEW FLOW ---
def start_ai_session():
    print("--- Starting Humanistic AI Session ---")
    
    # Core research flow questions
    research_flow = [
        ("Hello! I am so pleased to see you in the lab today. To begin our conversation, what is your name?", "introduction"),
        ("And which department are you working with here at Waterloo?", "department"),
        ("Being a graduate researcher can be quite demanding. What do you do in your spare time to relax and find balance?", "well-being"),
        ("Your research on supporting caregivers is a vital gap in social robotics. Could you describe your current project for me?", "research"),
        ("It has been a privilege speaking with you. Do you have any final thoughts on how robots can best support humans?", "conclusion")
    ]

    for question, topic in research_flow:
        # 1. Robot asks the initial question
        furhat.say(text=question, blocking=True)
        
        # 2. Robot listens (The green 'listening' bar appears in the SDK)
        print(f"Listening for: {topic}...")
        result = furhat.listen()
        user_text = result.message if result.message else "User is thinking"

        # 3. Visual 'Thinking' Cue (Makes the robot look more human)
        furhat.gesture(name="Thoughtful", blocking=False)
        
        # 4. Fetch the Intelligent response from Groq
        speech_text, emotion_gesture = get_groq_intelligence(user_text, topic)

        # 5. The 'Humanistic' Reaction
        print(f"Robot [Gesture: {emotion_gesture}]: {speech_text}")
        furhat.gesture(name=emotion_gesture)
        furhat.say(text=speech_text, blocking=True)
        
        # 6. Natural Social Pause (The 'Social Gap')
        time.sleep(1.0)

    furhat.say(text="Thank you for such an insightful session, Farida. I look forward to our next interaction in the lab!", blocking=True)

if __name__ == "__main__":
    start_ai_session()

#/opt/homebrew/Caskroom/miniforge/base/envs/robot_env/bin/python "/Users/Farida/Documents/ALL Furhat Code /Python Code for CS 686/LLM.py
#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
# /opt/homebrew/Caskroom/miniforge/base/envs/robot_env/bin/python "/Users/Farida/Documents/ALL Furhat Code /Python Code for CS 686/LLM.py"
