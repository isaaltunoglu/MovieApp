import requests
from bs4 import BeautifulSoup


headers = {"User-Agent": 
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0"}


while True:
    print("What do you want to do ? ")
    print("1-Top Movies\n2-Top Series\n3-Categories for me\n4- -1 for exite")
    
    choice = str(input("Enter your choice: "))
    if choice == "-1":
        break
    else:
        if choice == "1":
            tm_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

            #Url ile Top Movieleri al
        elif choice == "2":
            pass
            #Url ile Top Seriesleri al
        elif choice == "3":
            pass
            #Kategorileri getir
        else:
            print("Invalid choice. Please try again.")