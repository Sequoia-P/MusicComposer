# Music Note Generator, Editor, and Composer
# Author: Sequoia Pflug
# Music Advisor: Denali Pflug
# 12-31-2021
# Update 1: 5-30-2022: Added save file feature
# Update 2: 12-26-2022: Added undo button, new music player, new sound, removed unnecessary button refresh 




import random
import StdDraw
import sys
import picture
import threading
from sys import platform

if platform == "linux" or platform == "linux2" or platform == "darwin":
    from noteSound import noteSound

elif platform == "win32":
    from winNoteSound import winNoteSound

notes = ["C", "Db", "D" , "Eb", "E", "F", "Gb", "G", "Ab","A", "Bb" ,"B","C", "Db", "D" , "Eb", "E", "F", "Gb", "G", "Ab","A", "Bb" ,"B"]
singleNotes = ["C", "Db", "D" , "Eb", "E", "F", "Gb", "G", "Ab","A", "Bb" ,"B", "Done"]
randomList = []
memory = []
keys = []
XPosList = []
textYPosList = []
noteYPosList = []
buttonXList = []
buttonYList = []
saveFile = 1
start = 1

StdDraw.setCanvasSize(768, 632)
StdDraw.setXscale(0, 768)
StdDraw.setYscale(0, 632)
background = picture.Picture("../graphics/staff.png")
StdDraw.setFontFamily("SansSerif")
StdDraw.setFontSize(20)
StdDraw.setPenRadius(1)

# Media Functions------------------------------------------------------------

def buttons(auto, clearBoard):

    if clearBoard == 1:
        StdDraw.setPenColor(StdDraw.WHITE)
        StdDraw.filledRectangle(0, 404, 768, 146)
        StdDraw.show(0.0001)

    global buttonXList
    global buttonYList

    z = len(keys)
    
    if z <= 8:
        spacing = 768/(z+1)
        for y in range(0, len(keys)):
            buttonXList.append(int(spacing * (y+1)))
            buttonYList.append(int(490))
    else:
        if z % 2 == 0:
            spacing = 768/((z/2)+1)
            for b in range(0, int(z/2)):
                buttonXList.append(int(spacing * (b+1)))
                buttonYList.append(int(518))
            for c in range(0, int(len(keys)) - int(z/2)):
                buttonXList.append(int(spacing * (c+1)))
                buttonYList.append(int(461))
        else:
            spacing = 768/(((z+1)/2)+1)
            for b in range(0, int((z+1)/2)):
                buttonXList.append(int(spacing * (b+1)))
                buttonYList.append(int(518))
            for c in range(0, int(len(keys)) - int((z+1)/2)):
                buttonXList.append(int(spacing * (c+1)))
                buttonYList.append(int(461))
            
    pressed = 20
    if auto == 1:
        while pressed == 20:
            pressed = checkButtons()
                        
        resetButtons(clearBoard)
        
        return pressed

def checkButtons():
    pressed = 20
    
    for x in range(0, len(keys)):
        buttonPic = picture.Picture("../graphics/" + str(str(keys[x]) + ".png"))
        buttonY = buttonYList[x]
        buttonX =  buttonXList[x]
        StdDraw.picture(buttonPic,buttonX,buttonY)
        StdDraw.show(0.0001)
        if StdDraw.mousePressed():
            for x in range(0, len(keys)):
                buttonY = buttonYList[x]
                buttonX =  buttonXList[x]
                if buttonX - 40 < int(StdDraw.mouseX()) < buttonX + 40 and buttonY - 23 < int(StdDraw.mouseY()) < buttonY + 23:
                    pressed = x

    return pressed

def resetButtons(clearBoard):
    buttonXList.clear()
    buttonYList.clear()                          
    keys.clear()
    if clearBoard == 1:
        StdDraw.setPenColor(StdDraw.WHITE)
        StdDraw.filledRectangle(0, 404, 768, 146)
        StdDraw.show(0.0001)

def buttonTitle(title):
    StdDraw.setPenColor(StdDraw.WHITE)
    StdDraw.filledRectangle(0, 550, 768, 82)
    StdDraw.setPenColor(StdDraw.BLACK)
    StdDraw.setFontSize(25)
    StdDraw.text(384, 575, str(title))
    StdDraw.setFontSize(20)
    StdDraw.show(0.0001)

def title(text, duration):
    StdDraw.setPenColor(StdDraw.WHITE)
    StdDraw.filledRectangle(0, 404, 768, 228)
    StdDraw.show(0.0001)
    
    StdDraw.setPenColor(StdDraw.BLACK)
    StdDraw.setFontSize(40)
    StdDraw.text(384, 513, str(text))
    StdDraw.setFontSize(20)
    StdDraw.show(duration)

    StdDraw.setPenColor(StdDraw.WHITE)
    StdDraw.filledRectangle(0, 404, 768, 228)
    StdDraw.show(0.0001)
    
            
def position(note):
    if note == "A":
        position = 200
    elif note == "Ab":
        position = 184
    elif note == "B":
        position = 215
    elif note == "Bb":
        position = 200
    elif note == "C":
        position = 122
    elif note == "D":
        position = 138
    elif note == "Db":
        position = 122
    elif note == "E":
        position = 153
    elif note == "Eb":
        position = 138
    elif note == "F":
        position = 168
    elif note == "G":
        position = 184
    elif note == "Gb":
        position = 168

    return position

def clear():
    XPosList.clear()
    textYPosList.clear()
    noteYPosList.clear()
    StdDraw.picture(background,384,216)

    StdDraw.setPenColor(StdDraw.BLACK)
    StdDraw.filledRectangle(0, 399, 768, 5)

    
    StdDraw.show(0.0001)

def visualize():
    clear()
    
    separation = 648 / len(randomList)

    XPos = 120

    XPosList.append(XPos)

    for x in range(0, len(randomList)):
        StdDraw.setPenColor(StdDraw.BLACK)
        
        if x % 2 == 0:
            textYPos = 60
        else:
            textYPos = 339
        textYPosList.append(textYPos)
        
        spaces = ""
        note = str(randomList[x])
        if len(note) == 1:
            spaces += " "
        if len(str(x)) == 1:
            spaces += " "
        txt = str(x+1) + ": " + spaces + note
        StdDraw.text(int(XPos), textYPos, str(txt))

        pic = picture.Picture(str("../graphics/" + note + "note.png"))
        noteYPos = position(note)
        noteYPosList.append(noteYPos)
        StdDraw.picture(pic,XPos,noteYPos)

        StdDraw.setPenColor(StdDraw.LIGHT_GRAY)
        if textYPos < noteYPos:
            StdDraw.line(XPos, textYPos + 8, XPos, noteYPos - 12)     
        if textYPos > noteYPos:
            StdDraw.line(XPos, textYPos - 8, XPos, noteYPos + 12)

        XPos += separation
        XPosList.append(XPos)
        StdDraw.show(0.0001)

def highlightNote(x):
    XPos = XPosList[x]
    note = str(randomList[x])
    textYPos = textYPosList[x]
    noteYPos = noteYPosList[x]
    spaces = ""
    if len(note) == 1:
        spaces += " "
    if len(str(x)) == 1:
        spaces += " "
    txt = str(x+1) + ": " + spaces + note
    
    StdDraw.setPenColor(StdDraw.RED)
    StdDraw.text(int(XPos), textYPos, str(txt))
    if textYPos < noteYPos:
        StdDraw.line(XPos, textYPos + 8, XPos, noteYPos - 12)     
    if textYPos > noteYPos:
        StdDraw.line(XPos, textYPos - 8, XPos, noteYPos + 12)
    StdDraw.show(0.0001)

def unhighlightNote(x):
    XPos = XPosList[x]
    note = str(randomList[x])
    textYPos = textYPosList[x]
    noteYPos = noteYPosList[x]
    spaces = ""
    if len(note) == 1:
        spaces += " "
    if len(str(x)) == 1:
        spaces += " "
    txt = str(x+1) + ": " + spaces + note
    
    StdDraw.setPenColor(StdDraw.WHITE)
    StdDraw.filledRectangle(XPos-20, textYPos-6, 50, 12)
    StdDraw.setPenColor(StdDraw.BLACK)
    StdDraw.text(int(XPos), textYPos, str(txt))
    StdDraw.setPenColor(StdDraw.LIGHT_GRAY)
    if textYPos < noteYPos:
        StdDraw.line(XPos, textYPos + 8, XPos, noteYPos - 12)     
    if textYPos > noteYPos:
        StdDraw.line(XPos, textYPos - 8, XPos, noteYPos + 12)
    resetButtons(0)
    StdDraw.show(0.0001)

def playSounds():
    global keys

    resetButtons(1)
    
    option = 0
    pause = 0
    x = 0
    done = 0
    
    while option != 4 and done != 1:
        if x == len(randomList):
                x = 0
        highlightNote(x)
        keys += ["Backward", "Play", "Forward", "Done"]
        buttonTitle("Music Player")
        option = buttons(1, 0) + 1
        if option == 1:
            unhighlightNote(x)
            if x == 0:
                x = len(randomList) -1
            else:
                x -= 1
        if option == 2:
            unhighlightNote(x)
            while x < len(randomList):
                if pause == 1 or done == 1:
                    pause = 0
                    break

                highlightNote(x)

                note = str(randomList[x])
                sound = threading.Thread(target=noteSound, args=[note])
                sound.start()
                StdDraw.show(0.0001)

                keys += ["BackwardGray", "Pause", "ForwardGray", "Done"]
                buttonTitle("Music Player")
                buttons(0, 0)
                while sound.is_alive():
                    option = checkButtons() + 1
                    if option == 2:
                        pause = 1 
                    if option == 4:
                        done = 1
                unhighlightNote(x)
                x += 1
        if option == 3:
            unhighlightNote(x)
            if x == len(randomList):
                x = 0
            else:
                x += 1
    if x != 0:           
        unhighlightNote(x-1)
    if x != len(randomList):
        unhighlightNote(x)

    resetButtons(1)

# Mechanical Functions---------------------------------------------------

def undo():
    memory.pop(-1)
    randomList.clear()
    
    for note in range(0, len(memory[-1])):
        randomList.append(memory[-1][note])
                                       
    memory.pop(-1)

    if randomList == []:
        clear()
    else:
        visualize()

def saveList():
    fName = str("../saveFiles/save" + str(saveFile) + ".txt")
    with open(fName, "w") as f:
        for note in randomList:
            f.write(note + " ")
    f.close()

def loadList():
    fName = str("../saveFiles/save" + str(saveFile) + ".txt")
    randomList.clear()
    with open(fName, "r") as f:
        line = f.readline().split()
        for note in range(0, len(line)):
                randomList.append(line[note])
    f.close()
    if len(randomList) != 0:
        visualize()
    else:
        clear()

def randomNotes(number, dupStat):

    resetButtons(1)
    
    if dupStat == "0":
        maxDups = int((number + len(randomList))/2)
        if maxDups == 1:
            maxDups = 0
    else:
        maxDups = 20
    
    dups = 0
    x = 0

    if randomList != []:
        for z in range(0, 12):
            count = randomList.count(notes[z])
            if count > 1:
                dups += count
            
    while x < number:
        position = random.randint(0, 11)
        note = notes[position]
        if note in randomList:
            if dups < maxDups:
                count2 = randomList.count(note)
                if count2 % 2 == 0:
                    dups += 1
                    randomList.append(note)
                elif dups == maxDups - 1:
                    dups += 1
                    x -= 1
                else:
                    dups += 2
                    randomList.append(note)
            else:
                x -= 1
        else:
            randomList.append(note)
        x += 1

    visualize()
    saveList()
    resetButtons(1)

def manualNotes():
    global keys
    global randomList

    resetButtons(1)
    
    new = 0
    x = 1 + len(randomList)
    while x <= 16:
        keys += singleNotes
        buttonTitle(str("Choose a note to add for space #" + str(x) + ":"))
        number = buttons(1, 0)
        note = singleNotes[number]
        if note == "Done":
            break
        else:
            randomList.append(note)
            new += 1
            visualize()
        x += 1
        saveList()
    if x > 16:
        title("Maximum number of notes reached", 1000)
    if new != 0 and len(randomList) > 1:
        keys += ["Yes", "No"]
        buttonTitle("Would you like to shuffle all notes?")
        shuffleStat = buttons(1, 1)
        if shuffleStat == 0:
            random.shuffle(randomList)
            saveList()
            visualize()

    resetButtons(1)

def transpose(direction, magnitude):
    global randomList

    resetButtons(1)
    
    transposedList  = [] 

    if direction == 1:
        for x in range(0, len(randomList)):
            index = notes.index(str(randomList[x]))
            transposedList.append(notes[int(index+magnitude)])

    elif direction == 0:
        for x in range(0, len(randomList)):
            index = notes.index(str(randomList[x]))
            transposedList.append(notes[int(index-magnitude)])

    if transposedList != []:
        randomList = transposedList
        visualize()

    saveList()
    resetButtons(1)

def removeNotes(choice2):
    global keys
    resetButtons(1)
    
    if choice2 == "1":
        randomList.clear()
        clear()
        saveList()
        title("All notes have been cleared!", 1000)
        
    elif choice2 == "2":
        while len(randomList) != 0:
            for t in range(1, len(randomList) +1):
                keys.append(t)
            keys.append("done")
            currentNotes = []
            currentNotes += keys
            buttonTitle("Choose an index to delete:")
            j = buttons(1, 1) 
            if currentNotes[j] == "done":
                currentNotes.clear()
                break
            else:
                currentNotes.clear()
                if int(j) <= len(randomList):
                    randomList.pop(int(j))
                    if len(randomList) == 0:
                        clear()
                        title("Note list is empty", 1000)
                    else:
                        visualize()
            saveList()
        
                
    elif choice2 == "3":
        while len(randomList) != 0:
            for w in range(0, len(singleNotes)-1):
                if str(singleNotes[w]) in randomList:
                    keys.append(str(singleNotes[w]))
            keys.append("done")
            currentNotes = []
            currentNotes += keys
            buttonTitle("Choose a note type to delete:")
            j = buttons(1, 1)
            k = currentNotes[j]
            currentNotes.clear()
            if k == "done":
                break
            elif k in randomList:
                while k in randomList:
                    randomList.remove(str(k))
                if len(randomList) == 0:
                    clear()
                    title("Note list is empty", 1000)
                else:
                    visualize()
            saveList()
    resetButtons(1)

def manageFiles():
    global saveFile

    resetButtons(1)
    current = saveFile
    while current != 6:
        for new in range(1, 6):
            if new != current:
                keys.append(new)
            else:
                keys.append(str(new) + "selected")
        keys.append("done")

        if start == 1:
            buttonTitle("Welcome! Please Select A Save File To Begin:")
        else:
            buttonTitle("Select the save file that you want to use:")
        current = buttons(1, 0) + 1
            
        if current != 6:
            saveFile = current
            loadList()

        elif start != 1 and memory[-1] != randomList:
            memory.clear()
    resetButtons(1)
            
            

# Menu---------------------------------------------------------------

clear()
loadList()
manageFiles()
start = 0

while True:
    if memory == []:
        memory.append(randomList.copy())
    elif memory[-1] != randomList:
        memory.append(randomList.copy())
        
    keys += ["Undo", "AddNotes", "RemoveNotes", "Transpose", "PlaySounds", "ChangeFile"]
    buttonTitle("Please Select An Option:")
    option = buttons(1, 0) + 1

    if option == 1:
        if len(memory) < 2:
            title("Memory is empty", 1000)
        else:
            undo()     
    
    if option == 2:
        if len(randomList) >= 16:
            title("Note list is full", 1000)
        else:
            keys += ["Random", "Manual"]
            buttonTitle("How would you like to add notes?")
            choice = buttons(1, 1) 
            if choice == 0:
                count = 1 
                while 0 < count <= 16 and len(randomList) + count <= 16:
                    count += 1
                for v in range(1, count):
                    keys.append(str(v))
                buttonTitle("How many notes would you like to add?")
                number = buttons(1, 1) + 1
                
                maxDups = int((number + len(randomList))/2)
                if maxDups == 1:
                    maxDups = 0
                if randomList != []:
                    for z in range(0, 12):
                        count = randomList.count(notes[z])
                        if count > 1:
                            maxDups -= count
                
                keys += ["Yes", "No"]
                if maxDups == 0:
                    buttonTitle("Would you like to prevent new duplicate notes?")
                    dupStat = buttons(1, 1)
                else:
                    buttonTitle("Would you like to reduce the number of new duplicate notes to a maximum of " + str(maxDups) + "?")
                    dupStat = buttons(1, 1)
                randomNotes(number,str(dupStat))
                    
            elif choice == 1:
                manualNotes()
        
    if option == 3:
        if randomList == []:
            title("Note list is empty!", 1000)
        else:
            keys += ["All", "Index", "Value"]
            buttonTitle("How would you like to remove notes?")
            choice2 = buttons(1, 1) + 1
            removeNotes(str(choice2))

    if option == 4:
        if randomList == []:
            title("You need to generate notes first!", 1000)
        else:
            keys += ["Backwards", "Forwards"]
            buttonTitle("In which direction would you like to transpose?")
            direction = buttons(1, 1)
            keys += ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
            buttonTitle("By how many notes?")
            magnitude = buttons(1, 1) + 1
            transpose(direction, magnitude)

    if option == 5:
        if randomList == []:
            title("You need to generate notes first!", 1000)
        else:
            playSounds()

    if option == 6:
        manageFiles()
        

        



