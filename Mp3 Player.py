from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title('Charles Player')
root.geometry('500x400')


#Time info
def play_time():
    #check for double timing
    if stopped:
        return
    #Get current time
    currentTime = pygame.mixer.music.get_pos()/1000


    #Throw up a temporary label
    #slider_label.config(text=f'Slider: {int(mySlider.get())} and Song Pos: {int(currentTime)}')
    #convert time
    convertTime = time.strftime('%M:%S', time.gmtime(currentTime))
    

    #Get currently song
    #currentSong = songBox.curselection()
    #Grab song title from plylist
    song = songBox.get(ACTIVE)
    song = f'D:/Coding/Python/Tkinter/Song/{song}'

    #Get song length
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length
    #Convert to time format
    #convert time
    convert_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    #increase current time
    currentTime+=1
    if int(mySlider.get()) == int(song_length):
        statusBar.config(text=f'Time Elapsed: {convert_song_length}')


    elif int(mySlider.get()) == int(currentTime):
        #Slider has'nt been moved
         #Update slider to position
        slider_pos = int(song_length)
        mySlider.config(to=slider_pos, value=int(currentTime))
    
    elif paused:
        pass

    else:
        #Slider has been moved
         #Update slider to position
        slider_pos = int(song_length)
        mySlider.config(to=slider_pos, value=int(mySlider.get()))
        #convert time
        convertTime = time.strftime('%M:%S', time.gmtime(int(mySlider.get())))
        statusBar.config(text=f'Time Elapsed: {convertTime} of {convert_song_length}')

        #Move 
        next_time = int(mySlider.get()) + 1
        mySlider.config(value=next_time)



    #Put on status bar
    #statusBar.config(text=f'Time Elapsed: {convertTime} of {convert_song_length}')
    #Update slider position value to current song position
    #mySlider.config(value=int(currentTime))

   
    #Update time
    statusBar.after(1000, play_time)

#Add one song
def add_song():
    song = filedialog.askopenfilename(initialdir='Song/', title='Choose a Song', filetypes=(("mp3 Files", "*.mp3"),("flac Files","*.flac")))
    song = song.replace("D:/Coding/Python/Tkinter/Song/","") #Menghilangkan D:/Coding...

    #Add song to list box
    songBox.insert(END, song)

#Add many song
def add_many_song():
    songs = filedialog.askopenfilenames(initialdir='Song/', title='Choose a Song', filetypes=(("mp3 Files", "*.mp3"),("flac Files","*.flac")))

    #loop through song list to replace
    for song in songs:
        song = song.replace("D:/Coding/Python/Tkinter/Song/","") #Menghilangkan D:/Coding...

        #Add song to list box
        songBox.insert(END, song)


#Play selected song
def play():
    #currVolume = pygame.mixer.music.get_volume()
    #slider_label.config(text=currVolume)
    global stopped
    stopped = False
    songPlay = songBox.get(ACTIVE)
    songPlay = f'D:/Coding/Python/Tkinter/Song/{songPlay}'

    pygame.mixer.music.load(songPlay)
    pygame.mixer.music.play(loops=0)

    #Time counter when song was play
    play_time()

    #Update slider to position
    #slider_pos = int(song_length)
    #mySlider.config(to=slider_pos, value=0)
    
    #get current volume
    #currVolume = pygame.mixer.music.get_volume()
    #slider_label.config(text=currVolume * 100)
    
#Stop selected song
global stopped
stopped = False
def stop():
    #Reset slider and status bar
    statusBar.config(text='')
    mySlider.config(value=0)

    #stop song 
    pygame.mixer.music.stop()
    songBox.selection_clear(ACTIVE) #ACTIVE mean stop selection

    #Clear status bar
    statusBar.config(text='')

    #set stop variable to true
    global stopped
    stopped = True

#Pause function
global paused
paused = False
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:          #paused = True
        #Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        #Pause
        pygame.mixer.music.pause()
        paused = True

#Play the next song
def nextSong():
    #Reset slider and status bar
    statusBar.config(text='')
    mySlider.config(value=0)

    #Dapatkan tupple number lagu yang sedang dijalankan
    nextOne = songBox.curselection()
    #Add one to get next song tupple number
    #Kalau bingung dengan nextOne[0], coba uncomment program di bawah
    #print(nextOne)
    #print(nextOne[0])
    nextOne = nextOne[0]+1
    #Grab song title from plylist
    song = songBox.get(nextOne)
    
    song = f'D:/Coding/Python/Tkinter/Song/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #Move active bar
    songBox.selection_clear(0,END)
    songBox.activate(nextOne)
    songBox.selection_set(nextOne,last=None)

def prevSong():
    #Reset slider and status bar
    statusBar.config(text='')
    mySlider.config(value=0)
    #Dapatkan tupple number lagu yang sedang dijalankan
    prevOne = songBox.curselection()
    #Add one to get next song tupple number
    #Kalau bingung dengan nextOne[0], coba uncomment program di bawah
    #print(nextOne)
    #print(nextOne[0])
    prevOne = prevOne[0]-1
    #Grab song title from plylist
    song = songBox.get(prevOne)
    
    song = f'D:/Coding/Python/Tkinter/Song/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #Move active bar
    songBox.selection_clear(0,END)
    songBox.activate(prevOne)
    songBox.selection_set(prevOne,last=None)


#ddelete one song which selected
def delete_song():
    stop()
    songBox.delete(ANCHOR)
    pygame.mixer.music.stop()


#delete all song
def delete_All_song():
    stop()
    songBox.delete(0,END)
    pygame.mixer.music.stop()

#Slider function 
def slide(x):
    #slider_label.config(text=f'{int(mySlider.get())} of {int(song_length)}')
    songPlay = songBox.get(ACTIVE)
    songPlay = f'D:/Coding/Python/Tkinter/Song/{songPlay}'

    pygame.mixer.music.load(songPlay)
    pygame.mixer.music.play(loops=0, start=int(mySlider.get()))

#create volume function 
def volume(x):
    pygame.mixer.music.set_volume(volumeSlider.get())
    #currVolume = pygame.mixer.music.get_volume()
    #slider_label.config(text=currVolume*100)

#Initialize pygame
pygame.mixer.init()



#create master frame
masterFrame = Frame(root)
masterFrame.pack(pady=20)

#Create a plylist Box
songBox = Listbox(masterFrame, bg='black', fg='white', width=60, selectbackground="grey")
songBox.grid(row=0, column=0)

#Create a frame for control button
controlFrame = Frame(masterFrame)
controlFrame.grid(row=1, column=0,pady=20)

#create volume label frame
volumeFrame = LabelFrame(masterFrame, text='VOLUME')
volumeFrame.grid(row=0, column=1, padx=10)

#create player control button
backwardButton = Button(controlFrame, text='Prev', borderwidth = 4, command=prevSong)
forwardButton = Button(controlFrame, text='Next', borderwidth = 4, command=nextSong)
playButton = Button(controlFrame, text='Play', borderwidth = 4, command=play)
pauseButton = Button(controlFrame, text='Pause', borderwidth = 4, command=lambda: pause(paused))
stopButton =  Button(controlFrame, text='Stop', borderwidth = 4, command=stop)

backwardButton.grid(row =0 , column =0, padx=10)
forwardButton.grid(row =0, column =1, padx=10)
playButton.grid(row =0, column =2, padx=10)
pauseButton.grid(row =0, column =3, padx=10)
stopButton.grid(row =0, column=4, padx=10)

#Menu for song
myMenu = Menu(root)
root.config(menu=myMenu)

#Add song
addSong = Menu(myMenu)
myMenu.add_cascade(label="Add Song", menu=addSong)
addSong.add_command(label='Add One Song To Playlist', command=add_song)

#Add many song to plylist
addSong.add_command(label='Add Many Song To Playlist', command=add_many_song)

#Delete song menu
removeSong = Menu(myMenu)
myMenu.add_cascade(label='Remove Song', menu=removeSong)
removeSong.add_command(label='Delete A Song', command=delete_song)
removeSong.add_command(label='Delete All Song', command=delete_All_song)

#Create a status bar
statusBar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
statusBar.pack(fill=X, side=BOTTOM, ipady=2)

#Music slider
mySlider = ttk.Scale(masterFrame, from_=0, to=100, orient=HORIZONTAL, value=0, length=360, command=slide)
mySlider.grid(row=2, column=0, pady=30)

#volume slider
volumeSlider = ttk.Scale(volumeFrame, from_=0, to=1, orient=VERTICAL, value=1, length=125, command=volume)
volumeSlider.pack(pady=10)

#create temporary slider label
#slider_label = Label(root, text="0")
#slider_label.pack(pady=20)


root.mainloop()