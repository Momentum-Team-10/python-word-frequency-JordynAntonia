import string 
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

"""Read in `file` and print out the frequency of words in that file."""
    
    # removes the punctuation from the text
    #calling function to clean text within the file, opening file, removing punctuation and then closing the file. Looking at each line for punctuation errors with open("praise_song_for_the_day.txt") as praise_song_for_the_day: "text=str
def print_word_freq(file):
    with open (file) as text:
        lines = text.read()
        print(f"{len(lines)} lines in the file.")
        for line in lines:
            line = line.replace(",","")
            line = line.replace(".","")
            line = line.replace("_","")
            line = line.replace("?","")
            line = line.replace(":","")
            line = line.replace("'","")
            line = line.lower()
            print(line)
                lower_string = string.lower()
                text = text.lower()
                all_letters = "abcdefghijklmnopqrstuvwxyz"
                text_to_keep = "" 
    
            

    #normalize ALL words within each string to lowercase via "geeksforgeeks.org", "docs.python.org","bytes.lower()"
def clean_text(file):
    with open(file) as text:
        lines = text.readlines()
        print(b"{len(lines)} lines in the file.")
        lower_string = string.lower()
        text = text.lower()
        all_letters = "abcdefghijklmnopqrstuvwxyz"
        text_to_keep = "" 


    #remove "stop words" via example 2"programcreek.com and geeksforgeeks.org"
def clean_text(text):
    with open("file.text"):
        STOP_WORDS = stopwords.words('english')
    print(f"{len(STOP_WORDS)} text in the file.")
    text = clean_string (text)
    text = [word for word in text if word not in stop_words]
    

#     #keep a count of how often each word is used: splitting the words up in the text file, "item in data", if else statement, creating min-max spaces 0-string2,  

# def print_word_freq(text):
#     """Read in `file` and print out the frequency of words in that file."""
#     with open("file.txt"):
    str = str.split()
    str2 = []
    for i in str:
        if not in str2:
            #"append"adds value 
            str2.append(i)
    for i in range(0, len(str2)) :
        #to make output look like the project 
        print(str2[i], '|', str.count(str2[i])
def main ():
    str = STOP_WORDS
    freq(str)

def _name_ =="_main"
    main()

#     print(file.closed)
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

"""this calls the file to run"""
file = Path(args.file)
if file.is_file():
    print_word_freq(file)
else:
    print(f"{file} does not exist!")
    exit(1)







# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
