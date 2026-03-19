# Challenge: Text Analyzer
# Difficulty: Beginner → Low-Intermediate
#
# Write a function that analyzes a block of text and returns:
# 1. Total number of words
# 2. Total number of unique words (case-insensitive)
# 3. Most frequent word(s)
#
# Rules:
# - Words are separated by spaces
# - Ignore punctuation (.,!?) at the end of words
# - Treat words in a case-insensitive way ("Apple" and "apple" are the same)
# - If multiple words share the highest frequency, return all of them in a list sorted alphabetically
#
# Return Format:
# - A dictionary with keys:
#   "total_words", "unique_words", "most_frequent"
#   Example:
#   {
#       "total_words": 10,
#       "unique_words": 8,
#       "most_frequent": ["apple"]
#   }
#
# Notes:
# - You may import modules from the Python standard library if needed (like collections)
# - Do NOT print inside the function

def text_analyzer(text):
    result = {}
    # For loop to remove all punctuation from the string.
    for punctuation in """.,!?<>:;/}{[]()'@#$%^&*\"""":
            text = text.replace(punctuation, "")
            
    # Split the words into a list and parse them to lower case
    words = text.lower().strip().split(" ")
    
    # the length (or number of items in the list) is the total_words
    result["total_words"] = len(words)
    
    # for loop to determine the number of times each word appears
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
            
    result["unique_words"] = len(word_count)
        
    # Search word_count using a for loop to find the most used word
    mostFrequentWord = ""
    value = 0    
    for label, number in word_count.items():
        if number > value:
            mostFrequentWord = label
            value = number
        
    result["most_frequent"] = mostFrequentWord
    
    keys = list(result.keys())
    
    finalString = f"""{{
    "{keys[0]}": {result.get(keys[0])},
    "{keys[1]}": {result.get(keys[1])},
    "{keys[2]}": {result.get(keys[2])}
}}"""
        
    return finalString


if __name__ == "__main__":
    sample_text = "Apple apple banana. Orange apple! Banana orange? Grape."
    print(text_analyzer(sample_text))
    # Expected Output:
    # {
    #     "total_words": 8,
    #     "unique_words": 4,
    #     "most_frequent": ["apple"]
    # }