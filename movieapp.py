import requests
from bs4 import BeautifulSoup


headers = {"User-Agent": 
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0"}

class MovieOperators():
    def getTopMovie(self,headers):
        tm_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
        response =  requests.get(tm_url,headers=headers).text
        soup = BeautifulSoup(response, "html.parser")
        print("Welcome For Top 250 Movies!")
        limit = int(input("How many movies do you want ? "))
        print("----"*7)
        movie_List = soup.find("ul",{"class":"ipc-metadata-list"}).find_all("li",limit=limit)
        for movie in movie_List:
            movie_name = movie.find("h3", {"class":"ipc-title__text"}).text
            movie_rating = movie.find("span", {"class":"ipc-rating-star--rating"}).text
            print(f"{movie_name} imdb: {movie_rating}")
            print("----"*7)
    def getTopSeries(self,headers):
        tm_url = "https://www.imdb.com/chart/toptv/"
        response =  requests.get(tm_url,headers=headers).text
        soup = BeautifulSoup(response, "html.parser")
        print("Welcome For Top 250 series!")
        limit = int(input("How many series do you want ? "))
        print("----"*7)
        movie_List = soup.find("ul",{"class":"ipc-metadata-list"}).find_all("li",limit=limit)
        for movie in movie_List:
            movie_name = movie.find("h3", {"class":"ipc-title__text"}).text
            movie_rating = movie.find("span", {"class":"ipc-rating-star--rating"}).text
            print(f"{movie_name} imdb: {movie_rating}")
            print("----"*7)

opm = MovieOperators()
#loop for user to interaction with app
while True:
    print("What do you want to do ? ")
    print("1-Top Movies\n2-Top Series\n3-for exite")
    
    choice = str(input("Enter your choice: "))
    if choice == "3":
        break
    else:
        if choice == "1":
            print("----"*7)
            opm.getTopMovie(headers)
            #Url ile Top Movieleri al
        elif choice == "2":
            opm.getTopSeries(headers)
            #Url ile Top Seriesleri al
        else:
            print("Invalid choice. Please try again.")


