# Open the file
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

# Print successors for ("the", "strange")
if ("the", "strange") in successor_map:
    print("Successors of ('the', 'strange'):", successor_map[("the", "strange")])
else:
    print("Bigram ('the', 'strange') not found.")