import json
import difflib

# Load JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

def get_definition(word, dictionary):
    # Normalize the word to lower case
    word = word.lower()
    
    # Check if the word is in the dictionary
    if word in dictionary:
        return dictionary[word]
    else:
        # Suggest the closest match if the word is not found
        suggestions = difflib.get_close_matches(word, dictionary.keys())
        if suggestions:
            return f"Word not found. Did you mean: {', '.join(suggestions)}?"
        else:
            return "Word not found and no suggestions available."

# Example usage
word = input("Enter a word: ")
print(get_definition(word, data))
