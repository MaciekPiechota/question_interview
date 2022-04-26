from urllib import response
import requests
import musicbrainzngs
import json

RAND_WORD_API_LINK = "https://random-words-api.vercel.app/word"
MIN_WORDS = 5
MAX_WORDS = 20


musicbrainzngs.set_useragent(
    "app.py",
    "0.1",
    "https://github.com/MaciekPiechota/freeport",
)

def get_random_words(number_of_words):

    words_set = set()
    while len(words_set) != number_of_words:
        response = requests.get(RAND_WORD_API_LINK).text
        response_info = json.loads(response)
        words_set.add(response_info[0]['word'])


    print("Words collected from :" + RAND_WORD_API_LINK)

    for word in words_set:
        print(word)

    return words_set

def record_data(record):
    title = record['title']
    artist = record['artist-credit'][0]['name']
    album = record['release-list'][0]['title']
    return title + " - " + artist + " - " + album

def find_songs(words):
    print("-----------------------")
    print("Searching for recording")
    for word in words:
        recordings = musicbrainzngs.search_recordings(word,limit=1)
        if not recordings['recording-list']:
            print(word + " no recording found")
        else:
            print(word + " (" + record_data(recordings['recording-list'][0]) + ")")

def main():
    number_of_words = 0
    while number_of_words > MAX_WORDS or number_of_words < MIN_WORDS:
        number_of_words = int(input("Enter number of word in range [5,20]: "))

    random_words = get_random_words(number_of_words)

    find_songs(random_words)


main()