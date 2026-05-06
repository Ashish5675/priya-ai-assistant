from voice import listen, speak
from ai import get_ai_response
from vision import detect_emotion

print("🤖 Priya AI Assistant Started...")

while True:
    try:
        user_input = listen()

        if not user_input:
            continue

        if "exit" in user_input:
            speak("Goodbye!")
            break

        emotion = detect_emotion()
        print("Detected Emotion:", emotion)

        response = get_ai_response(user_input, emotion)
        speak(response)

    except Exception as e:
        print("Error:", e)
