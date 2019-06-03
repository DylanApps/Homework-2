Name = "Eminem"
Age = 46
Song = "Rap God"

def ArtistName():
    global Name;
    return Name;
print ("Artist Name:",ArtistName())

def ArtistAge():
    global Age;
    return Age;
print ("Artist Age:", ArtistAge())

def SongName():
    global Song;
    return Song;
print ("SongName:", SongName())

def MoreThan():
    if (Age > 1000):
        return False
    else:
        return True


#I had planned on having the if statement be a question but i cant figure out inputs just yet!
print ("Eminem is 46 years old:", MoreThan())