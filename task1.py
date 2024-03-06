def compress_string(input_string):
    result = ""
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i-1]:
            count += 1
        else:
            if count > 1:
                result += input_string[i-1] + str(count)
            else:
                result += input_string[i-1]
            count = 1
    if count > 1:
        result += input_string[-1] + str(count)
    else:
        result += input_string[-1]
    return result
input_string = "QQQwwwEEErrrTTTyyy"
output = compress_string(input_string)
print(output)

