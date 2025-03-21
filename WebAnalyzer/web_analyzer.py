import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/University_of_Calgary"
def keyword_display(soup):
    keyword = input("Please enter the key word you would like to search for: ")
    number = soup.count(keyword)
    print(f"The {keyword} appears {number} times")

def word_freuqency(soup):
    #Search and split
    split_list = soup.split(" ")
    dict_count = {}

    for word in split_list:
        if word.lower() in dict_count.keys():
            dict_count[word.lower()] += 1
        else:
            dict_count[word.lower()] = 1

    #print(dict_count)
    for i in range(5):
        max_num = max(dict_count.values())
        for key in dict_count.keys():
            if dict_count[key] == max_num:
                print(f"The {i+1} most occuring word is \"{key}\" and has a frequency of {max_num}")
                del dict_count[key]
                break

def count_p(p):
    max_num = 0
    max_paragraph = ''
    for paragraph in p:
        list_words = paragraph.get_text().split(" ")
        if len(list_words) < 5:
            break
        if len(list_words) > max_num:
            max_num = len(list_words)
            max_paragraph = paragraph
    print(f"The longest paragraph contains {max_num} words and is {max_paragraph}")



    
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
    print(soup.prettify())
    h1 = soup.find_all("h1")
    num_h1 = len(h1)
    h2 = soup.find_all("h2")
    num_h2 = len(h2)
    h3 = soup.find_all("h3")
    num_h3 = len(h3)
    h4 = soup.find_all("h4")
    num_h4 = len(h4)
    h5 = soup.find_all("h5")
    num_h5 = len(h5)
    h6 = soup.find_all("h6")
    num_h6 = len(h6)
    headings = num_h1+num_h2+num_h3+num_h4+num_h5+num_h6
    print("The number of heading tags is: ", headings)


    p = soup.find_all("p")
    print(p)
    num_p = len(p)
    print("The number of p tags is: ", num_p)

    a = soup.find_all("a")
    num_a = len(a)
    print("The number of a tags is: ", num_a)

    soup_text = soup.get_text()
    keyword_display(soup_text)
    word_freuqency(soup_text)
    count_p(p)

    labels = ['Headings', 'Links', 'Paragraphs']
    values = [headings, num_a, num_p]
    plt.bar(labels, values)
    plt.title('Group #14')
    plt.ylabel('Count')
    plt.show()

except Exception as e:
    print(f"Error fetching content: {e}")