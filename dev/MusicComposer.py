# Music Note Generator, Editor, and Player
# Author: Sequoia Pflug
# Music Advisor: Denali Pflug
# Original Version: 12-31-2021
# Update 1: 5-30-2022: Added save file feature
# Update 2: 12-26-2022: Added undo button, new music player, new sound, new button refresh functions


# Set up------------------------------------------------------------

# imports
import random
import StdDraw
import sys
import picture
import threading
from noteSound import noteSound

# variable initializations 
notes = ["C", "Db", "D" , "Eb", "E", "F", "Gb", "G", "Ab","A", "Bb" ,"B","C", "Db", "D" , "Eb", "E", "F", "Gb", "G", "Ab","A", "Bb" ,"B"] # Note list for generation/transposition 
singleNotes = ["C", "Db", "D" , "Eb", "E", "F", "Gb", "G", "Ab","A", "Bb" ,"B", "Done"] # Note list for menus
randomList = [] # list of currently displayed notes
memory = [] # list of previous iterations of currently loaded save file 
keys = [] # list of buttons to be generated
XPosList = [] #list of x positions for notes on display
textYPosList = [] # list of y positions for note text on display
noteYPosList = [] # list of y positions for notes on display
buttonXList = [] # list of x positions for buttons on display
buttonYList = [] # list of y positions for buttons on display
saveFile = 1 # currently loaded save file
start = 1 # startup mode

# initialize graphics 
StdDraw.setCanvasSize(768, 632)
StdDraw.setXscale(0, 768)
StdDraw.setYscale(0, 632)
background = picture.Picture("../graphics/staff.png")
StdDraw.setFontFamily("SansSerif")
StdDraw.setFontSize(20)
StdDraw.setPenRadius(1)

# Graphical Functions------------------------------------------------------------

# Displays buttons in “keys” list. 
# auto(int): Waits until a key is pressed and then returns which list entry was pressed if 1
# clearBoard(int): Clears the button menu before displaying if 1
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
        
        return pressed #(int) "keys" list entry that was pressed

# Checks for mouse clicks on each entry in “keys”
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

    return pressed # (int) "keys" list entry that was pressed

# Clears all buttons and their positions from memory
# clearBoard(int): Removes all buttons from display if 1
def resetButtons(clearBoard):
    buttonXList.clear()
    buttonYList.clear()                          
    keys.clear()
    if clearBoard == 1:
        StdDraw.setPenColor(StdDraw.WHITE)
        StdDraw.filledRectangle(0, 404, 768, 146)
        StdDraw.show(0.0001)

# Adds text above buttons
# title(str): text to display
def buttonTitle(title):
    StdDraw.setPenColor(StdDraw.WHITE)
    StdDraw.filledRectangle(0, 550, 768, 82)
    StdDraw.setPenColor(StdDraw.BLACK)
    StdDraw.setFontSize(25)
    StdDraw.text(384, 575, str(title))
    StdDraw.setFontSize(20)
    StdDraw.show(0.0001)

# Clears buttons and displays text in center of menu, then clears again
# title(str): text to display
# duration(int): how long to title (in milliseconds )
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
    
# Returns the appropriate position(int) to display a note icon given a note(str)       
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

# Completely resets graphical interface
def clear():
    XPosList.clear()
    textYPosList.clear()
    noteYPosList.clear()
    StdDraw.picture(background,384,216)

    StdDraw.setPenColor(StdDraw.BLACK)
    StdDraw.filledRectangle(0, 399, 768, 5)

    
    StdDraw.show(0.0001)

# Displays all notes in randomList on screen
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

# Highlights a given note in randomList x(int) in red
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

# Removes highlight from a given note in randomList x(int)
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

# Primary Functions---------------------------------------------------

# Music player and controls 
def playSounds():
    global keys

    resetButtons(1)
    
    # variable initializations 
    option = 0 # selected button
    pause = 0 # pause indicator 
    x = 0 # note being played
    done = 0 # done indicator

    #Music player menu and loop
    while option != 4 and done != 1:
        if x == len(randomList):
                x = 0
                
        highlightNote(x) #highlight current note
        keys += ["Backward", "Play", "Forward", "Done"]
        buttonTitle("Music Player")
        option = buttons(1, 0) + 1
        
        # Select previous note
        if option == 1: 
            unhighlightNote(x)
            if x == 0:
                x = len(randomList) -1
            else:
                x -= 1
                
        # Play sounds while checking for button presses
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
        
        # Select next note
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

#Sets randomList equal to most recent memory entry, then deletes the most recent memory entry
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

# Exports randomList to current save file
def saveList():
    fName = str("../saveFiles/save" + str(saveFile) + ".txt")
    with open(fName, "w") as f:
        for note in randomList:
            f.write(note + " ")
    f.close()

# Reads the current save file into randomList
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

# Generates and adds random notes to randomList
# number(int): Number of random notes to generate
# dupStat: Reduces number of duplicate notes if 1
def randomNotes(number, dupStat):

    resetButtons(1)
    
    if dupStat == "1":
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

# Interface for user to manually add notes to randomlist
def manualNotes():
    global keys
    global randomList

    resetButtons(1)
    
    new = 0 # number of newly added notes
    x = 1 + len(randomList) # number of notes currently in randomList
    
    # Allows user to add new notes until randomList has 16 entries
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
    
    #Allows user to shuffle randomList
    if new != 0 and len(randomList) > 1:
        keys += ["Yes", "No"]
        buttonTitle("Would you like to shuffle all notes?")
        shuffleStat = buttons(1, 1)
        if shuffleStat == 0:
            random.shuffle(randomList)
            saveList()
            visualize()

    resetButtons(1)

# Transposes randomList
# direction(int): transposes forward if 1, backward if 0
# magnitude(int): number of steps to transpose by (maximum of 12)
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

# Interface for user to remove notes from randomList
# choice2(int): method of removal
def removeNotes(choice2):
    global keys
    resetButtons(1)
    
    # Removes all notes from randomList and resets screen
    if choice2 == "1":
        randomList.clear()
        clear()
        saveList()
        title("All notes have been cleared!", 1000)
    
    # Allows user to remove notes in randomList by index until list is empty   
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
        
    # Allows user to remove all notes of a specific type in randomList until list is empty               
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

# Interface for user to change which save file is in use
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
    # Save current randomList to memory 
    if memory == []:
        memory.append(randomList.copy())
    elif memory[-1] != randomList:
        memory.append(randomList.copy())
    
    # Get menu choice from user (option)    
    keys += ["Undo", "AddNotes", "RemoveNotes", "Transpose", "PlaySounds", "ChangeFile"]
    buttonTitle("Please Select An Option:")
    option = buttons(1, 0) + 1
    
    # Revert to previous version of randomList if memory is not empty
    if option == 1:
        if len(memory) < 2:
            title("Memory is empty", 1000)
        else:
            undo()     
    
    # Add notes to randomList if list is not full
    if option == 2:
        if len(randomList) >= 16:
            title("Note list is full", 1000)
        else:
            #Get preferred method from user (choice)
            keys += ["Random", "Manual"]
            buttonTitle("How would you like to add notes?")
            choice = buttons(1, 1) 

            #Add randomly generated notes
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
                    dupStat = buttons(1, 1) + 1
                else:
                    buttonTitle("Would you like to reduce the number of new duplicate notes to a maximum of " + str(maxDups) + "?")
                    dupStat = buttons(1, 1) + 1
                randomNotes(number,str(dupStat))
            
            # Add notes manually         
            elif choice == 1:
                manualNotes()
    
    # Removes notes from randomList if list is not empty    
    if option == 3:
        if randomList == []:
            title("Note list is empty!", 1000)
        else:
            keys += ["All", "Index", "Value"]
            buttonTitle("How would you like to remove notes?")
            choice2 = buttons(1, 1) + 1
            removeNotes(str(choice2))
    
    # Transposes notes in randomList if list is not empty
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
    
    # Plays notes in randomList if list is not empty
    if option == 5:
        if randomList == []:
            title("You need to generate notes first!", 1000)
        else:
            playSounds()
    
    # Changes save file
    if option == 6:
        manageFiles()
        

        



