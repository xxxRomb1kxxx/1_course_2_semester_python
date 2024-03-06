words = ['dog','cat','hourse','slon','dog','cat','hourse','slon','slon','slon','slon','slon','slon','slon','slon','slon','slon','slon',]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for count in word_count.values():
    print(count, end='')
    # 22212 -> 2 dog, 2 cat, 2 hourse, 12 slone