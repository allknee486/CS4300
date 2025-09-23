def read_text_file():
    file = open("/home/student/CS4300/homework1/task6_read_me.txt")
    num_of_words = 0
    for i in file:
        words = i.split()
        num_of_words += len(words)
    file.close()
    return num_of_words