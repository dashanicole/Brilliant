import random

# Open the file (make sure you have data/jekyll.txt saved)
reader = open('jekyll.txt', encoding='utf-8')

# Dictionary to store bigram -> list of successors
successor_map = {}
window = []

# Process the file line by line
for line in reader:
    for word in line.split():
        # Clean punctuation and lowercase
        clean_word = word.strip('.;,-“’”:?—‘!()_').lower()
        window.append(clean_word)

        # Maintain a sliding window of size 3
        if len(window) == 3:
            key = (window[0], window[1])   # bigram key
            value = window[2]              # successor word

            # Add to the successor map
            if key not in successor_map:
                successor_map[key] = [value]
            else:
                successor_map[key].append(value)

            # Slide the window forward
            window.pop(0)

# Close the file
reader.close()

print("\nGenerated Text:")

# Seed random for reproducibility
random.seed(3)

# Starting words
word1 = "the"
word2 = "lawyer"

# Generate 15 words using the Markov chain
for i in range(15):
    print(word1, end=" ")
    successors = successor_map.get((word1, word2))
    if not successors:
        break
    word3 = random.choice(successors)
    word1, word2 = word2, word3

print(word2)  # print the last word