"""
Given a .txt file that has a list of a bunch of names, count how many of each
name there are in the file, and print out the results to the screen. I have a
.txt file for you, if you want to use it!
Extra:
Instead of using the .txt file from above (or instead of, if you want the
challenge), take this .txt file, and count how many of each “category” of
each image there are. This text file is actually a list of files
corresponding to the SUN database scene recognition database, and lists
the file directory hierarchy for the images. Once you take a look at the
first line or two of the file, it will be clear which part represents the
scene category. To do this, you’re going to have to remember a bit about
string parsing in Python 3. I talked a little bit about it in this post.
"""
def read_file():
    dicti = {}
    with open("nameslist.txt", "r") as open_file:
        read_line = open_file.readline()
        while read_line:
            read_line = read_line.strip()
            if read_line in dicti:
                dicti[read_line] += 1
            else:
                dicti[read_line] = 1
            read_line = open_file.readline()
    print(dicti)


def read_file_second():
    dicti = {}
    with open('Training_01.txt', 'r') as file:
        read_line = file.readline()
        while read_line:
            read_line = read_line.split('/')    # Make line into list
            end = read_line[2]                  # 'end' represents first category
            if end == read_line[-2]:
                if read_line[2] in dicti:
                    dicti[read_line[2]] += 1
                else:
                    dicti[read_line[2]] = 1
            elif end != read_line[-2]:
                result = read_line[2]+ '/' + read_line[-2]  # add second category
                if result in dicti:
                    dicti[result] += 1
                else:
                    dicti[result] = 1
            read_line = file.readline()
    print(dicti)


read_file()
read_file_second()
