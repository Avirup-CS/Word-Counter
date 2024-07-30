def wordCount(text):

    def remove_special_character(word):

        return ''.join(ch for ch in word if ch.isalnum() or ch.isspace()) # Joins characters from 'word' that are alphanumeric or spaces into a new string, effectively removing special characters

    words = text.split() # Splits the input text into a list of words based on whitespace
    
    cleaned_words = [remove_special_character(word) for word in words] # Applies the remove_special_character function to each word in 'words' and stores the cleaned words in a new list
    
    cleaned_sentence = ' '.join(cleaned_words) # Joins the list of cleaned words into a single string with spaces between words
    
    newtext = cleaned_sentence.split(' ') # Splits the cleaned sentence back into a list of words based on whitespace
    
    text_letter = [letter for letter in newtext if letter.isalnum()] # Filters out words that contain only alphanumeric characters
    
    no_of_Words = len(text_letter)

    return no_of_Words
    

text = input("Enter a Sentence or Paragraph:\n").strip() # Prompts the user for input and removes any leading or trailing whitespace

if len(text) > 0: # Checks if the input text is not empty
    print("\nThe number of words in the sentence: ", wordCount(text))
    
else: # If the input text is empty
    print("\nSorry, Input is Empty..Please Enter Some Text !!")
    
