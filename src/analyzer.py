from collections import Counter

def analyze_headers(headers):
    """Identify words repeated more than twice across translated titles."""
    all_words = " ".join(headers).lower().split()  # Combine all titles and split into words
    word_counts = Counter(all_words)  # Count occurrences of each word
    # Return words that appear more than twice
    return {word: count for word, count in word_counts.items() if count > 2}