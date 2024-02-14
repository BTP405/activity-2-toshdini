def wordCount(t):
    word_dict = {}
    with open(t, 'r') as file:
        data = file.readlines()
        for i, line in enumerate(data, start=1):
            words = line.strip().split()
            for word in words:
                if word not in word_dict:
                    word_dict[word] = [i]
                else:
                    if i not in word_dict[word]:
                        word_dict[word].append(i)
    return word_dict

