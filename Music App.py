# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:41:02 2023

@author: SHASHANK
"""

#input genre, will make playlist with 5 songs of that genre 
#song title, artist, genre, song length

songsLibrary = [
    ["Old Town Road", "Lil Nas X", "Pop", "4m 1s"],
    ["Always you", "Louis Tomlinson", "Indie", "3m 23s"],
    ["Watermelon Sugar", "Harry Styles", "Pop", "3m 0s"],
    ["Roses", "St John's", "EDM", "3m 43s"],
    ["Highway To Hell", "AC/DC", "Rock", "4m 14s"],
    ["London Thumakada", "Queen", "Bollywood", "5m 1s"],
    ["Legacy", "Motionless In White", "Metal", "2m 59s"],
    ["Goosebumps", "Travis Scott", "Rap", "3m 40s"],
    ["Hallucinations", "PVRIS", "Pop", "3m 19s"],
    ["Queen Bee", "Lauren Sanderson", "Pop", "3m 19s"],
    ["Bewafa", "Imran Khan", "Bollywood", "4m 1s"],
    ["Nothing Else Matters", "Metallica", "Metal", "6m 6s"],
    ["YKWIM?", "Yot Club", "Indie", "2m 9s"],
    ["HOT", "Young Thug", "Rap", "4m 2s"],
    ]

#creates NEW account
def account():
    account = []
    fileOpener = open("accounts.txt", "a")
    
    name = input("Welcome! Enter your name: ")
    dob = input("Enter your date of birth: ")
    favArtist = input("Enter your favourite artist: ")
    favGenre = input("Enter your favourite genre: ")
    
    account.append(name + "," + dob + ","  + favArtist + "," + favGenre)
    
    print("Account created successfully. ")
    
    for each in account:
        fileOpener.write(each + "\n")
    
    
    fileOpener.close()
    
    print()
    menu()

#creates a playlist based on user's fav genre
def genre():
    playlist = []
    
    #checker = False
    favGenre = input("Enter your favourite genre: ")
    
    for row in songsLibrary:
            
        if favGenre in row[2]:
            playlist.append(row)
        
             
    print("Curated playlist of the genre: ", favGenre)
    print()
    
    for each in playlist:
        print(*each, sep = ", ")
    
    print()
    menu()

#sorts 2D ARRAY SONG LIBRARY alphabetically
def alphabetical():
    sortedList = []
    sortedList = (sorted(songsLibrary, key=lambda x: x))
    
    for each in sortedList:
        print(*each, sep = ", ")
    
    print()
    menu()


#checks for EXISTING account

def accountChecker():
    
    fileOpener = open("accounts.txt", "r")
    
    checker = fileOpener.readlines()
    
    nameInput = input("Enter your name: ")
    flag = False
    
    while flag == False:
        for each in checker:
            if nameInput in each:
                flag = True
                
                print("Welcome back ", nameInput, " !")
                print("What would you like to do now? ")
                
                menu()
        
            while flag == False:
                print("Name not found. ")
                break  
    
    menu()

def create():
    playlistName = input("What would you like to name your playlist?: ")
    playlistName = []
    
    numOfSongs = int(input("Enter the number of songs you would like to put: "))
    
    for i in range(0, numOfSongs):
        enterSong = input("Enter a song: ")
        playlistName.append(enterSong)
    
    print()
    
    for each in playlistName:
        print(each)
        
    print("Playlist successfully created. ")

    print()
    menu()
        
#Menu to display options 

def menu():
    print("[1] Create an account ")
    print("[2] Generate playlist of your favourite genre ")
    print("[3] Display song library in alphabetical order ")
    print("[4] Log into existing account ")
    print("[5] Create a playlist ")
    print("[6] Quit ")
    
    print()

    check = False
    while check == False:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account()
            check = True
            break
    
        elif choice == 2:
            genre()
            check = True
            break
    
        elif choice == 3:
            alphabetical()
            check = True
            break
    
        elif choice == 4:
            accountChecker()
            check = True
            break
        
        elif choice == 5:
            create()
            check = True
            break
        
        elif choice == 6:
            print()
            print("Thank you for using Music Mania. ")
            check = True 
            break 
        
        else:
            print("Invalid input. Try again. ")
            choice = int(input("Enter your choice: "))

menu()

#Automatically generates new playlists for the user using the 
#following criteria:
#the user inputs a time limit (e.g. 10 minutes) and 
#it generates a playlist that 
#does not last longer than this time





    
    
    
    
    
    
    
    
    

