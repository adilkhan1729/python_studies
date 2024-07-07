def highlight_keywords(essay, keywords):
    # Split the essay into words
    words = essay.split()
    
    # Check each word in the essay
    highlighted_essay = []
    for word in words:
        if word.lower() in keywords:
            # If the word is in the list of keywords, highlight it
            highlighted_essay.append("<<{word}>>")
            pass
        else:
            highlighted_essay.append(word)
    
    # Join the words back together into a highlighted essay
    highlighted_essay_text = ' '.join(highlighted_essay)
    return highlighted_essay_text

# Example keywords given by Mr. Smith
keywords_to_check = ['important', 'analyze', 'conclusion', 'evidence']

# Example essay content (you can replace this with your file reading code)
sample_essay = """
In order to write a good essay, it is crucial to analyze the given topic thoroughly. Providing strong evidence and examples is important to support your arguments. In conclusion, the essay should summarize the main points effectively.
"""

# Highlight keywords in the essay
highlighted_essay = highlight_keywords(sample_essay, keywords_to_check)
print(highlighted_essay)
