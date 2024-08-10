from collections import Counter

def word_count(text):
    """
    Counts the frequency of each word in a given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary where the keys are words and the values are their frequencies.
    """
    words = text.lower().split()
    cleaned_words = [word.strip('.,!?;') for word in words]
    return Counter(cleaned_words)

def display_word_count(word_counts):
    """
    Displays the word counts in a formatted way.

    Args:
        word_counts (dict): A dictionary of word counts.
    """
    print("Word Frequency:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

def main():
    text = input("Enter a sentence or paragraph: ")
    word_counts = word_count(text)
    display_word_count(word_counts)

if __name__ == "__main__":
    main()
