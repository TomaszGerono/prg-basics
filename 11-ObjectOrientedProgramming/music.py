class Song:
    def __init__(self,performer,title,album,year):
        self.performer = performer
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return f"Performer: {self.performer}\nTitle: {self.title}\nAlbum: {self.album}\nYear: {self.year}"

def main():
    song1 = Song("Performer1","Title1","Album1","Year1")
    song2 = Song("Perfomer2","Title2","Album2","Year2")

    print(song1)
    print(song2)


if __name__ == "__main__":
    main()