STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def clean_text(line):
    """Read in `file` and print out the frequency of words in that file."""
    
    # removes the punctuation from the text
    #calling function to clean text within the file, opening file, removing punctuation and then closing the file. Looking at each line for punctuation errors with open("praise_song_for_the_day.txt") as praise_song_for_the_day:
        lines = praise_song_for_the_day.readlines()
        print(f"{len(lines)} lines in the file.")
        for line in lines:
            line = line.replace(",","")
            line = line.replace(".","")
            line = line.replace("_","")
            line = line.replace("?","")
            line = line.replace(":","")
            line = line.replace("'","")
        print(praise_song_for_the_day.closed)
            
            

    #normalize ALL words within each string to lowercase via "geeksforgeeks.org", "docs.python.org","bytes.lower()"
def clean_text(text):
    with open("praise_song_for_the_day.txt") as praise_song_for_the_day:
    text = praise_song_for_the_day.readlines()
    print(b"{len(lines)} lines in the file.")
    lower_string = string.lower()
    text = text.lower()
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    text_to_keep = "" 
    print(lower_string.closed)

    #remove "stop words" via example 2"programcreek.com and geeksforgeeks.org"
def clean_text(text):
    with open("praise_song_for_the_day.txt") as praise_song_for_the_day:
    STOP_WORDS = stopwords.words('english')
    text = clean_string (text)
    text = [word for word in text if word not in stop_words]
    print(STOP_WORDS.closed)

    #keep a count of how often each word is used
def print_word_freq(text):

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
