def evaluator(schemes):
    if not schemes:
        return "ଆପଣଙ୍କ ପାଇଁ କୌଣସି ଯୋଗ୍ୟ ଯୋଜନା ମିଳିଲା ନାହିଁ।"

    response = "ଆପଣ ଯୋଗ୍ୟ ଥିବା ଯୋଜନାଗୁଡ଼ିକ:\n\n"
    for s in schemes:
        response += f"- {s['name']} : {s['description']}\n"

    response += "\nସୁପାରିଶ: ସର୍ବୋଚ୍ଚ ପ୍ରାଥମିକତା ଯୋଜନାକୁ ଆବେଦନ କରନ୍ତୁ।"
    return response
