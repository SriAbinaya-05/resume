def summarize_resume(text):

    words = text.split()

    if len(words) > 100:
        return " ".join(words[:100])

    return text