print(">>> main.py started")

from stt import speech_to_text
from tts import speak
from planner import planner 
from executor import executor
from evaluator import evaluator
from memory import Memory

memory = Memory()

speak("ସରକାରୀ ଯୋଜନା ସହାୟକକୁ ସ୍ୱାଗତ")

while True:
    step = planner(memory)
    if step == "ASK_AGE":
        speak("ଆପଣଙ୍କ ବୟସ କେତେ?")
        age_input = speech_to_text().strip()

        if not age_input.isdigit():
            speak("ଦୟାକରି ସଂଖ୍ୟାରେ ବୟସ କହନ୍ତୁ।")
            continue

        memory.update("age", int(age_input))

    
    elif step == "ASK_INCOME":
        speak("ଆପଣଙ୍କ ବାର୍ଷିକ ଆୟ କେତେ?")
        income_input = speech_to_text().strip()
        if not income_input.isdigit():
            speak("ଦୟାକରି ସଂଖ୍ୟାରେ ଆୟ ଦିଅନ୍ତୁ।")
            continue

        memory.update("income", int(income_input))

    elif step == "ASK_OCCUPATION":
        speak("ଆପଣଙ୍କ ପେଶା କଣ?")
        occ = speech_to_text().lower()
        if "କୃଷକ" in occ or "farmer" in occ:
            memory.update("occupation", "farmer")
        elif "student" in occ or "ଛାତ୍ର" in occ:
            memory.update("occupation", "student")
        else:
            memory.update("occupation", "other")
    elif step == "ASK_CATEGORY":
        speak("ଆପଣ BPL, General କି Student?")
        cat = speech_to_text().strip().lower()

        if cat == "student":
            memory.update("category", "Student")
        elif cat == "bpl":
            memory.update("category", "BPL")
        else:
            memory.update("category", "General")

    
    elif step == "RUN_ELIGIBILITY":
        schemes = executor(memory)
        result = evaluator(schemes)
        speak(result)
        break
