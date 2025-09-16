import re
from collections import Counter

def count_word_frequencies(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_counts:
        print(f"{word} → {count}")
user_input = input("Enter a paragraph:\n")
count_word_frequencies(user_input)