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
    # Your code here
    pass


if __name__ == "__main__":
    sample_text = "Apple apple banana. Orange apple! Banana orange? Grape."
    print(text_analyzer(sample_text))
    # Expected Output:
    # {
    #     "total_words": 8,
    #     "unique_words": 4,
    #     "most_frequent": ["apple"]
    # }