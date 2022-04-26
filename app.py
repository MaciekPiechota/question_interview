from urllib import response
import requests
import json

rand_words_api_link = "https://random-words-api.vercel.app/word"

def get_random_words(number_of_words):

    words_set = set()
    while len(words_set) != number_of_words:
        response = requests.get(rand_words_api_link).text
        response_info = json.loads(response)
        words_set.add(response_info[0]['word'])


    print("Words collected from :" + rand_words_api_link)

    for word in words_set:
        print(word)

    



def main():

    number_of_words = 0
    while number_of_words > 20 or number_of_words < 5:
        number_of_words = int(input("Enter number of word in range [5,20]: "))

    random_words = get_random_words(number_of_words)


main()