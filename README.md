![Screen Shot 2022-12-28 at 8 20 16 PM](https://user-images.githubusercontent.com/48298639/209899047-bf375b38-fde8-4a87-b138-33679d145f44.png)

# Music Passage Composer - by Sequoia Pflug

**Music Passage Composer is a prototype software tool built to aid music artists in the creation of excerpts for new compositions.** It has been built from the ground up with suggestions and feedback from a talented pianist in order to ensure usefulness. With the ability to quickly create, test, and randomly generate sheet music for passages up to 16 notes long, instantly transpose music up to 11 spaces in either direction, and much more, Music Passage Composer is a very unique tool that will bring your creativity to the next level! See below for a full list of features, instructions on how to download, and future development plans!

Features:
-	Live Staff Display
-	Random music generator
-	Manuel music composition
-	Music transposer (up to 11 spaces forwards or backwards)
-	Note removal by position or value
-	Music player with selection controls and piano sounds
-	5 save files with immediate auto-save
-	Undo button for recent changes in current save file

[Watch a demonstration video here](https://youtu.be/-hTbvwLepy8)


# Instructions

This project is availible for anyone to download and use and can be opened by running the MusicComposer.py file in the "dev" folder. Use the following instructions to set it up on your Windows or MacOS device. If you have any questions about using the program or its settup process, feel free to DM me on Instagram @planecrazy.mt!

**Setup:** This project is currently in the form of Python Scripts and will need the following in order to run:
- The latest stable release of Python for [MacOS](https://www.python.org/downloads/macos/) or [Windows](https://www.python.org/downloads/windows/)
- pygame (installed using `pip install pygame` in terminal)
- numpy (installed using `pip install numpy` in terminal)

**Download:** If you are not familiar with github or running Python files:
- Click the green "< > Code" button near the top right of this page and select "Download Zip"
- Unzip the file in your downloads folder 
- Run the MusicComposer.py file in the "dev" folder in terminal using `python` or `python3` command 

**Use:** See [this video](https://youtu.be/-hTbvwLepy8) for a demonstration of the program's functions and how to use them.


# Future Plans

This project is still in a fairly early stage and much of the fundementle work was done near the beginning of my computer science education. As I have time over the next few years, I hope to do the following:

- Switch to a different library for UI: The current libraries that I am using for graphics, audio, and other key functions (stdLib, stdDraw, and stdAudio) are outdated, ineffiecient, and place many limitions on furthur development. Switching to PyQT5, Tkinter, or a similar solution would require changing much of the current code, but would make the following goals much more feasable. 
- Improve efficiency: Partly due to how StdDraw functions, the program currently consists of large, ineffocient loops that could be significantly reduced given a different library. I would also like to switch to an object-orianted approach for each note and/or save file. 
- More notes and octaves: While the current program is only meant to compose individual music passages, the current framework would allow the creation and management of entire songs and a much larger veriety of notes in different octives. This would be fairly easy to implement if the graphics are handeled more efficiently.  
- Publish as a web application: As this program is currenly built in python, inplementing it as a web-app could be a possibility and would make it much more accesable than is it in its current form. 

