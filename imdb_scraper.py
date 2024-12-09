# Script to scrape the IMDb rating from a list of movies in a file

import requests, time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.random
headers = {'User-Agent': user_agent}


def main():
    with open('movies.txt') as movies:
        for movie in movies:
            movie = movie.rstrip('\n')
            request = requests.get('https://imdb.com/find?q=' + movie, headers=headers).text
            soup = BeautifulSoup(request, 'lxml')
            try:
                movie_id = soup.find('a', class_='ipc-metadata-list-summary-item__t').attrs['href']
            except AttributeError:
                movie_id = ""
                rating = "Movie ID not found!"
                    
            time.sleep(0.5)
    
            if movie_id == "":
                pass
            else:
                second_request = requests.get('https://www.imdb.com' + movie_id, headers=headers).text
                second_soup = BeautifulSoup(second_request, 'lxml')
                try:
                    rating = second_soup.find('span', class_='sc-7ab21ed2-1 jGRxWM').text
                except AttributeError:
                    rating = "Not found!"
                        
            with open('movie_ratings.txt', 'a') as ratings_file:
                ratings_file.write('{} -> {}\n'.format(movie, rating))

            print('{} -> {}'.format(movie, rating))
            time.sleep(1)


if __name__ == '__main__':
    main()

# Script to sort movie ratings
'''
dic = {}
with open('movie_ratings.txt') as ratings_file:
    for line in ratings_file:
        line = line.rstrip('\n').split('->')
        dic[line[0]] = line[1]

new_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for i in new_dic:
    print(i)
'''
