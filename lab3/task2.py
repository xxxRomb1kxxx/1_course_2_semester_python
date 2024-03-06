def decompress_string(compressed_string):
    decompress_string = ""
    i = 0
    while i < len(compressed_string):
        char = compressed_string[i]
        if i + 1 < len(compressed_string) and compressed_string[i+1].isdigit():
            char_count = int(compressed_string[i+1])
            decompress_string += char *char_count
            i += 2
        else:
            decompress_string += char
            i += 1
    return decompress_string
compressed_string = "Q3w3E3r3Ty3"
print(decompress_string(compressed_string))