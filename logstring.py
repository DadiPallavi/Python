def longest_string(strings):
    if len(strings) == 0:
        return None
    
    longest = strings[0]
    
    for word in strings:
        if len(word) > len(longest):
            longest = word
            
    return longest


print(longest_string(["apple", "banana", "kiwi"]))  # banana