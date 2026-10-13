import requests
FURHAT_URL = "http://localhost:8080"

def furhat_say(text):
    """Send text to Furhat to speak."""
    requests.post(f"{FURHAT_URL}/furhat/say", json={"text": text})

def rule_based_interaction():
    furhat_say("Hello there! I'd like to get to know you a little better.")

    name = input("Furhat: What is your name?\nYou: ")
    furhat_say(f"Nice to meet you, {name}.")

    department = input("Furhat: Which department are you in?\nYou: ")
    furhat_say(f"Oh, {department} sounds interesting.")

    spare_time = input("Furhat: What do you like to do in your spare time?\nYou: ")
    furhat_say(f"That sounds like a great way to spend your time.")

    hobbies = input("Furhat: Do you have any hobbies?\nYou: ")
    furhat_say(f"{hobbies} sounds fun!")

    robot_interests = input("Furhat: What are your interests in robots?\nYou: ")
    furhat_say(f"Thanks for sharing! It's great to hear about your interest in {robot_interests}.")

    furhat_say("Thank you for chatting with me. Goodbye!")

rule_based_interaction()
