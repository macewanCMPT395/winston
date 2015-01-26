
# CMPT 200 Lab 5 Queue Management System
# 
# Author: Winston Kouch
# MacEwan ID: 1645889
#
# Date: November 3, 2014
#
# To start program:  type in console:       main()
#          WARNING:  !!! to avoid graphics.py crashes, use the rectangular exit
#                        buttons within the menu instead of clicking x or pressing
#                        alt+f4      !!!
#
#            The program will boot up the graphics menu when you run
#            this command.
#
# I/O Test Files: load.txt - load packages only text file
#                 YardData.txt - load container/package data state that was saved from last time
#                 SaveData.txt - saved text file of load.txt after being entered into system
#
# Description: Queue Management System to simulate shipping packages in a shipyard.
#              The menu is done in graphics.py and fully functional (there are some
#              exception handles such as weight not allowed to exceed 2000 lbs
#              and system generated id cannot be altered by user.
#              Functionality works regardless of lower and upper-case.
#
# Note: I did not perform print shipping manifest functions in graphics
#       display because I did not know how to create an autoflow method
#       for text in the case where the shipping manifest would be too
#       large to fit all the text on the screen. 
#
# Important: To exit a menu/form, do not use the x button, use the Exit boxes.
#            Please view the print outs in the python console after clicking
#            the option and then clicking update console.

from graphics import *
# QMS.py contains my shipyard class which also contain package and container
# class inside it
from QMS import *
import time

# Menu where you can choose to perform several functions in the system
# Functions: Load from packages, Load Yard Data, Save Yard Data, and
#            many other Shipyard Package Functions
def graph_menu():
    # Functional menu done in graphics.py
    front = "Winston's QMS Menu V1.0011"
    front_Text = Text(Point(630, 25), front)
    front_Text.setSize(16)    
    front_Text.draw(win)
    
    # Shipyard logo modified and found from
    # https://www.iconfinder.com/icons/175943/
    # basic_ship_shipyard_traffic_transport_transportation_travel_icon
    logo = Image(Point(710,110), "shipyardlogo.gif")
    
    # The 4 Menu Options (graphics.py)
    opt1 = Rectangle(Point(150, 190), Point(600, 240))
    opt2 = Rectangle(Point(150, 260), Point(600, 310))
    opt3 = Rectangle(Point(150, 330), Point(600, 380))
    opt4 = Rectangle(Point(150, 400), Point(600, 450))
    opt1.setFill('yellow')
    opt2.setFill('yellow')
    opt3.setFill('yellow')
    opt4.setFill('yellow')
    
    # Help and Exit Button Drawing (graphics.py)
    opt5 = Rectangle(Point(700, 520), Point(780, 580)) # box for exit
    opt6 = Rectangle(Point(20, 480), Point(140, 580))   # box for help
    opt5.setFill('red')
    opt6.setFill('green')
    opt1.draw(win)
    opt2.draw(win)
    opt3.draw(win)
    opt4.draw(win)
    opt5.draw(win)
    opt6.draw(win)
    exit_Text = Text(Point(740, 550), 'Exit') # box is opt 5
    help_Text = Text(Point(80,530), 'Help') # box is opt 6
    help_Text.draw(win)
    exit_Text.draw(win)
    logo.draw(win)
    
    # Option Texts
    txt1 = Text(Point(375, 215), "Load New Packages Into System From File (ie. load.txt)")
    txt2 = Text(Point(375, 285), "Load Container and Package Data From File (ie. YardData.txt)")
    txt3 = Text(Point(375, 355), "Save Yard System Data To File (ie. YardData.txt)")
    txt4 = Text(Point(375, 425), "Launch System Functions Menu (New Window)")
    txt1.draw(win)
    txt2.draw(win)
    txt3.draw(win)
    txt4.draw(win)    
    
# splash screen to program
def splash_Screen():
    closing = ""
    intro = """
    Hi! Welcome to the shipyard management system, QMS.
    
    Note: Many functions present information in graphics.py.
          The print shipping information functions will ONLY print data
          to the python console because the information will
          likely not fit in a graphics.py window.
          
    Please click your option after the system has loaded. Enjoy!
    """    
    # Draws the rectangle splash box
    rect = Rectangle(Point(10, 10), Point(790, 590))
    rect.setFill('grey')
    rect.draw(win)
    
    # Draw Splash Title of Game and set constraints for text style.
    banner_Text = Text(Point(400, 350), 'System Loading!')
    banner_Text.setSize(32)
    banner_Text.setFace('helvetica')
    banner_Text.setStyle('bold italic')
    intro_Text = Text(Point(380, 200), intro)
    intro_Text.setSize(14)
    closing_Text = Text(Point(640, 470), closing)
    closing_Text.draw(win)
    intro_Text.draw(win)
    banner_Text.draw(win)
    
    # Keeps splash screen on screen using 1 second sleeps for a total of 3 secs.
    for i in range(3):
        closing = "Closing in " + str(3-i) + " . . ."
        closing_Text.setText(closing)
        time.sleep(1)
        
    # undraw splash elements
    closing_Text.undraw()
    banner_Text.undraw()
    intro_Text.undraw()
    
# Bring up the help menu when called
def help_menu():
    helptext = """
    
    
       User guide for shipyard controls...     (click to return)
       
       Click Load New Packages into System From File
       to Load Packages from a Text File
       
       Click Load Container and Package Data From File
       to Restore Saved Yard Data
       
       Click Save Yard System Data to Save Yard Data To File
       
       Click Launch System Functions Menu to Open A New Window
       With Functions to Operate The System
       
       Remember: New windows must be closed to use the main menu.
       """    
    
    # Draws the rectangle splash box
    helprect = Rectangle(Point(10, 180), Point(790, 590))
    helprect.setFill('brown')
    helprect.draw(win)    
    intro_Text = Text(Point(380, 320), helptext)
    intro_Text.setSize(14)       
    intro_Text.draw(win)

    # Wait for user mouse click to go back to the program
    win.getMouse()
    # undraw code
    helprect.undraw()   
    intro_Text.undraw()
    
# Mouse Click Event Handler for main menu
def detect_actions():
    global win2
    program_running = True
    textentry = Text(Point(250, 100), "Please enter filename here:")
    filenameentry = Entry(Point(300,150), 20)
    filenameentry.setText("Filename?")
    filenameentry.draw(win)    
    textentry.draw(win)
    while program_running:
        #detect mouse clicks
        mouseCoord = win.getMouse()
            
        # if click option 1
        if mouseCoord.x >= 150 and mouseCoord.x <= 600 and mouseCoord.y >= 190 and mouseCoord.y <= 240:
            print("Option 1 Initial Load Data New System clicked")
            file = filenameentry.getText()
            print ("Loading", str(file))
            textentry.setText("Your file should have loaded.\nCheck console for filename if you like.\nClick anywhere again to allow navigation.")
            win.getMouse()
            textentry.setText("Please enter filename here:")
            # Run the load packages from a specified file
            q.loadPackagesFromFile(file)
                
        # if click option 2    
        if mouseCoord.x >= 150 and mouseCoord.x <= 600 and mouseCoord.y >= 260 and mouseCoord.y <= 310:
            print("Option 2 Load Packages and Containers into system")        
            file = filenameentry.getText()
            print ("Loading", str(file))
            textentry.setText("Your file should have loaded.\nCheck console for filename if you like.\nClick anywhere again to allow navigation.")
            win.getMouse()
            textentry.setText("Please enter filename here:")                
            # Run the Load Yard Data Function from a specified file
            q.loadYardData(file)
        
        # if click option 3, saving data
        if mouseCoord.x >= 150 and mouseCoord.x <= 600 and mouseCoord.y >= 330 and mouseCoord.y <= 380:
            print("Option 3 Save Yard Data")        
            file = filenameentry.getText()
            print ("Saving", str(file))
            textentry.setText("Your file is saved.\nCheck console for filename if you like.\nClick anywhere again to allow navigation.")
            win.getMouse()
            textentry.setText("Please enter filename here:")            
            # Save the Yard Data to a specified file
            q.saveYardData(file)
        
        # if click option 4
        if mouseCoord.x >= 150 and mouseCoord.x <= 600 and mouseCoord.y >= 400 and mouseCoord.y <= 450:
            print("Option 4 Launch Package Functions")
            
            # open win2 with launch package function
            win2 = GraphWin("Package Functions - QMS", 600, 300)
            win2.setBackground('lightblue')
            findPackageGUI() # reads user input to find specific package info
            win2.getMouse()
            
        # Detect mouse click in help/exit
        if mouseCoord.x >= 700 and mouseCoord.x <= 780 and mouseCoord.y >= 520 and mouseCoord.y <= 580:
            print("Exiting")
            win.close()
        if mouseCoord.x >= 20 and mouseCoord.x <= 140 and mouseCoord.y >= 480 and mouseCoord.y <= 580:
            print("Help Clicked")
            help_menu() # launch help menu window
                
# detect mouse events in the second window for package functions                
# traverseGrabPackageInside uses traverseGrabPackage to get the package information
# from within the container
# it then displays the package information for the user to see.
def detect_pkg_actions():
    global win3, win4, win5
    func_running = True
    while func_running:
        # listen for mouse click on package window
        mouseCoord = win2.getMouse()
        
        # if click search button
        if mouseCoord.x >= 400 and mouseCoord.x <= 580 and mouseCoord.y >= 20 and mouseCoord.y <= 100:
            print("Search clicked")
            # perform search and grab results change to search inside containers function after from shipyard
            grabid = pkgidbox.getText()
            # get the 5 values from the container and package retrieved by matching package id
            storage = q.traverseGrabPackageInside(str(grabid))
            pkgidbox.setText(storage[0])
            pkgidname.setText(storage[1])
            pkgiddest.setText(storage[2])
            pkgidweight.setText(storage[3])
            pkgidCID.setText(storage[4])
        
        # if click exit button        
        if mouseCoord.x >= 450 and mouseCoord.x <= 590 and mouseCoord.y >= 240 and mouseCoord.y <= 290:
            print ("Exit function")
            win2.close()
            func_running = False
            # run event handler for main menu
            detect_actions()
        
        # if click print func button
        if mouseCoord.x >= 300 and mouseCoord.x <= 420 and mouseCoord.y >= 240 and mouseCoord.y <= 290:
            # open win3 with print functions
            win3 = GraphWin("Print Functions - QMS", 600, 300)
            win3.setBackground('purple')   
            # run print menu event handler
            print_menu()
            
        # if click add func button
        if mouseCoord.x >= 10 and mouseCoord.x <= 160 and mouseCoord.y >= 240 and mouseCoord.y <= 290:
            # open win4 with add package function
            win4 = GraphWin("Add Package Window - QMS", 600, 300)
            win4.setBackground('lightgreen')       
            # run add menu event handler
            add_menu()        
            
        # if click del func button
        if mouseCoord.x >= 170 and mouseCoord.x <= 290 and mouseCoord.y >= 240 and mouseCoord.y <= 290:
            # open win4 with add package function
            win5 = GraphWin("Delete Package Window - QMS", 600, 300)
            win5.setBackground('orange')        
            # run delete menu event handler
            del_menu()                    
            

# Description: A new window that has buttons to initiate delete package function.
#              it calls deletePackageByIDInside in Shipyard class which finds the
#              container and used the deltePackageByID method in the container
#              class to remove the package.
#
# Functions used: deletePackageByIDInside, deletePackageByID
#
# deletePackageByIDInside finds the container holding the package and passes
# package id to deletePackageByID to delete the package
def del_menu():
    # Text Displays for information on packages
    del_text = Text(Point(180,20), "Delete Package From System")
    del_text.setSize(18)
    del_text.draw(win5)
    delpkgid=Text(Point(120,50),"Package ID: ")
    delpkgid.draw(win5)                
    del_running = True
    
    # Create entry boxes to get & set input data
    delpkgidbox = Entry(Point(300,50), 20)
    delpkgidbox.setText("1")
    delpkgidbox.draw(win5)                
    
    # Draws the rectangle splash box
    delsearchbox = Rectangle(Point(400, 40), Point(580,100))
    delsearchbox.setFill('green')
    delsearchbox.draw(win5)  
    
    # Search text to tell user to click here to interact                    
    delpkgsearch=Text(Point(490,50),"<---  Enter Package ID")
    delpkgsearch.draw(win5)
    delpkgsearch1=Text(Point(490,80),"Click to delete package")
    delpkgsearch1.draw(win5)
    
    # Exit button
    delexitFunc = Rectangle(Point(450, 240), Point(590, 290)) # box for exit
    delexitFunc.setFill('red')
    delexitText = Text(Point(520, 265), "Exit")
    delexitFunc.draw(win5)
    delexitText.draw(win5)    
        
    while del_running:
        # listen for mouse click on package window
        mouseCoord = win5.getMouse()
            
        # if click exit button        
        if mouseCoord.x >= 450 and mouseCoord.x <= 590 and mouseCoord.y >= 240 and mouseCoord.y <= 290:
            print ("Exit function")
            win5.close()
            del_running = False
            # run specify package event menu handler
            detect_pkg_actions()  
            
        # if click search button
        if mouseCoord.x >= 400 and mouseCoord.x <= 580 and mouseCoord.y >= 20 and mouseCoord.y <= 100:
            print("Delete package clicked")
            one = delpkgidbox.getText()
            
            # perform search and grab results change to search inside containers function after from shipyard
            thereturn = q.deletePackageByIDInside(str(one))
            print ("Package Delete Clicked")
            delpkgidbox.setText(str(one) + " is removed!")
            if (thereturn[0] == "Package Not Found"):
                delpkgidbox.setText("Package not found!")

            
# Description: A new window that has buttons to initiate print functions.
#              Destination Box is used to specific destination.
#
# Functions used: createPackage, traverseGrabPackageInside, traverseGrabPackage 
#
# createPackage creates a package after getting information from the user
# traverseGrabPackageInside is used to make sure unique package id is ready
def add_menu():

    # Text Displays for information on packages
    add_text = Text(Point(140,20), "Add Package to System")
    add_text.setSize(18)
    add_text.draw(win4)
    addpkgid=Text(Point(120,50),"Package ID: ")
    addpkgid.draw(win4)                
    addpkgowner=Text(Point(120,90),"Package Owner: ")
    addpkgowner.draw(win4)                                
    addpkgdest=Text(Point(120,130),"Package Destination: ")
    addpkgdest.draw(win4)                                
    addpkgweight=Text(Point(120,170),"Package Weight: ")
    addpkgweight.draw(win4)    
    
    # Create entry boxes to get & set input data
    addpkgidbox = Text(Point(300,50), 20)
    addpkgidbox.setText("")
    addpkgidbox.draw(win4)                
    addpkgidname = Entry(Point(300,90), 20)
    addpkgidname.setText("")
    addpkgidname.draw(win4)                                
    addpkgiddest = Entry(Point(300,130), 20)
    addpkgiddest.setText("")
    addpkgiddest.draw(win4)                                
    addpkgidweight = Entry(Point(300,170), 20)
    addpkgidweight.setText("")
    addpkgidweight.draw(win4)  
    
    
    # Draws the rectangle splash box
    addsearchbox = Rectangle(Point(400, 40), Point(580,100))
    addsearchbox.setFill('green')
    addsearchbox.draw(win4)  
    
    # Search text to tell user to click here to interact                    
    addpkgsearch=Text(Point(490,50),"<-- Sys-gen Pkg ID")
    addpkgsearch.draw(win4)
    addpkgsearch1=Text(Point(490,80),"Click to Add Package")
    addpkgsearch1.draw(win4)
    
    # Exit button
    addexitFunc = Rectangle(Point(450, 240), Point(590, 290)) # box for exit
    addexitFunc.setFill('red')
    addexitText = Text(Point(520, 265), "Exit")
    addexitFunc.draw(win4)
    addexitText.draw(win4)
    
    # Set up a unique ID that isnt in use in the system
    checkPkgID = q.traverseGrabPackageInside(str(q.uniqueID))
    if q.uniqueID == 0:
        checkPkgID = q.traverseGrabPackageInside(str(1))
    # duplication check on unique id, increase by 1 if id found
    while (checkPkgID[0] != "Package Not Found"):
        q.uniqueID += 1
        checkPkgID = q.traverseGrabPackageInside(str(q.uniqueID))
    addpkgidbox.setText(str(q.uniqueID))   
    if q.uniqueID == 0:
        q.uniqueID += 1
    addpkgidbox.setText(str(q.uniqueID))
    # for the case where initial scenario where uniqueID is 0 and no packages
    # in system
    #if addpkgidbox.getText() == "0":
    #    q.uniqueID += 1
    #    addpkgidbox.setText("1")
    # set mouse watching state
    add_running = True
    while add_running:
        # listen for mouse click on package window
        mouseCoord = win4.getMouse()
            
        # if click exit button        
        if mouseCoord.x >= 450 and mouseCoord.x <= 590 and mouseCoord.y >= 240 and mouseCoord.y <= 290:
            print ("Exit function")
            win4.close()
            add_running = False
            detect_pkg_actions()  
            
        # if click add button
        if mouseCoord.x >= 400 and mouseCoord.x <= 580 and mouseCoord.y >= 20 and mouseCoord.y <= 100:
            print("Add package clicked")
            one = addpkgidbox.getText()
            two = addpkgidname.getText().upper()
            three = addpkgiddest.getText().upper()
            four = addpkgidweight.getText()
            if two == "" or three == "" or four == "":
                msgbox = Text(Point(300,250), "All Package Information must have values!\n Entry canceled!\nClick anywhere to close window")
                msgbox.draw(win4)
                win4.getMouse()
                win4.close()
                detect_pkg_actions()            
            if int(four) > 2000:
                msgbox = Text(Point(300,250), "Overweight! Entry not entered!\n Click anywhere to close window")
                msgbox.draw(win4)
                win4.getMouse()
                win4.close()
                detect_pkg_actions()
            # Display message when package entered
            message = "Package entered into system as\nPackage ID: " + str(one) +"\nClick to continue"
            msgbox = Text(Point(300,250), message)
            msgbox.draw(win4)
            win4.getMouse()
            msgbox.undraw()
            
            # perform search and grab results to search inside containers function after from shipyard
            q.createPackage(str(one), two, three, four)
            print ("Package Created")
            # check to generate next auto package number
            checkPkgID = q.traverseGrabPackageInside(str(q.uniqueID))
            while (checkPkgID[0] != "Package Not Found"):
                q.uniqueID += 1
                checkPkgID = q.traverseGrabPackageInside(str(q.uniqueID))
            # update package entry boxes
            addpkgidbox.setText(str(q.uniqueID))    
            addpkgidname.setText("")
            addpkgiddest.setText("")
            addpkgidweight.setText("")
            win4.update()

              
# Description: A new window that has buttons to initiate print functions.
#              Also a function here to ship out containers
#
# Functions used: shippingManifestDest, shippingManifestAll, 
#                 getContainersNoContents, shipOutContainersDest
#
# the shippingManifestDest is used in regards to a specific destination.
# the shippingManifestAll is the information for all yard + package contents.
# the getContainersNoContents retrieves container information along with
# capacity information without contents.
# the shipOutContainersDest will shipout containers with a marked destination
# and report the number of containers along with total weight delivered in
# graphics window
def print_menu():
    
    # Text Displays for information on packages
    print_text = Text(Point(240,20), "Print and Ship Out Containers Function")
    print_text.setSize(18)

    # Print out Shipping Manifest For a Specific Destination
    PrintFunc = Rectangle(Point(10, 60), Point(160, 120))
    PrintFunc.setFill('green')
    PrintText = Text(Point(80, 90), "Shipping Manifest\n with Dest")
    PrintFunc.draw(win3)
    
    # Entry box for input destination
    inputDestText = Text(Point(315, 70), "Destination:")
    inputDest = Entry(Point(300, 100), 20)
    inputDest.setText("Destination?")
    inputDestText.draw(win3)
    
    # Ship out Containers To Specific Destination
    ShipOutFunc = Rectangle(Point(450, 120), Point(590, 180))
    ShipOutFunc.setFill('white')
    ShipOutText = Text(Point(520, 145), "Ship Containers\nTo Destination")
    ShipOutFunc.draw(win3)    
   
    # Print out Shipping Manifest For All Including Contents
    PrintAllFunc = Rectangle(Point(10, 130), Point(160, 190))
    PrintAllFunc.setFill('brown')
    PrintAllText = Text(Point(80, 160), "Shipping Manifest\nAll Contents")
    PrintAllFunc.draw(win3)
    
    # Print out List of Containers with info including capacity but not contents
    PrintContFunc = Rectangle(Point(10, 200), Point(160, 260))
    PrintContFunc.setFill('lightblue')
    PrintContText = Text(Point(84, 230), "Containers+Capacity\n + No Contents")
    PrintContFunc.draw(win3)    
    
    # Exit button
    printexitFunc = Rectangle(Point(450, 240), Point(590, 290)) # box for exit
    printexitFunc.setFill('red')
    printexitText = Text(Point(520, 265), "Exit")
    printexitFunc.draw(win3)
    printexitText.draw(win3)     
    
    # Update button
    printupdateFunc = Rectangle(Point(450, 190), Point(590, 230)) # box for exit
    printupdateFunc.setFill('green')
    printupdateText = Text(Point(520, 210), "Update Console")
    printupdateFunc.draw(win3)
    printupdateText.draw(win3)       
         
    # Print order so text will show on top         
    inputDest.draw(win3)
    print_text.draw(win3)
    PrintAllText.draw(win3)
    PrintText.draw(win3)
    PrintContText.draw(win3)
    ShipOutText.draw(win3)
    
    print_running = True
    while print_running:
        # listen for mouse click on package window
        mouseCoord = win3.getMouse()
        
        # if click shipping manifest with dest
        if mouseCoord.x >= 10 and mouseCoord.x <= 160 and mouseCoord.y >= 60 and mouseCoord.y <= 120:
            print("Shipping Manifest with Dest clicked, please click update console")
            destination = str(inputDest.getText()).upper()
            q.shippingManifestDest(destination)
            inputDest.setText("Output in Console")
            
        # if click shipping manifest all
        if mouseCoord.x >= 10 and mouseCoord.x <= 160 and mouseCoord.y >= 130 and mouseCoord.y <= 190:
            print("Shipping Manifest All Clicked, please click update console")                    
            q.shippingManifestAll()
            inputDest.setText("Output in Console")
           
        # if click container with capacity no contents
        if mouseCoord.x >= 10 and mouseCoord.x <= 160 and mouseCoord.y >= 200 and mouseCoord.y <= 260:
            q.getContainersNoContents()
            inputDest.setText("Output in Console")        
        
        if mouseCoord.x >= 450 and mouseCoord.x <= 590 and mouseCoord.y >= 120 and mouseCoord.y <= 180:
            print("Ship Out Containers to Destination clicked, please click update console")
            destination = str(inputDest.getText()).upper()
            q.shipOutContainersDest(str(destination))
            inputDest.setText("Output in Console")
        
        # if click Update button, this refreshes graphics so it'll update console output
        if mouseCoord.x >= 450 and mouseCoord.x <= 590 and mouseCoord.y >= 190 and mouseCoord.y <= 230:
            print ("Update Console clicked")
            win3.update()      
            
        # if click exit button        
        if mouseCoord.x >= 450 and mouseCoord.x <= 590 and mouseCoord.y >= 240 and mouseCoord.y <= 290:
            print ("Exit function")
            win3.close()
            print_running = False
            # launch detect mouse actions function for prev menu
            detect_pkg_actions()              
            

# Find Specific Package Function (graphics.py)
# From here, you can also access the buttons to open new window for
# add package, delete package, print functions
def findPackageGUI():
    global pkgidbox, pkgidname, pkgiddest, pkgidweight, pkgidCID
    # Text Displays for information on packages
    package_text = Text(Point(140,20), "Find Specific Package")
    package_text.setSize(18)
    package_text.draw(win2)
    
    # Package Text Boxes
    pkgid=Text(Point(120,50),"Package ID: ")
    pkgid.draw(win2)                
    pkgowner=Text(Point(120,90),"Package Owner: ")
    pkgowner.draw(win2)                                
    pkgdest=Text(Point(120,130),"Package Destination: ")
    pkgdest.draw(win2)                                
    pkgweight=Text(Point(120,170),"Package Weight: ")
    pkgweight.draw(win2)
    pkgCID=Text(Point(120,210),"Container ID: ")
    pkgCID.draw(win2)    
                                    
    # Create entry boxes to get & set input & output data
    pkgidbox = Entry(Point(300,50), 20)
    pkgidbox.setText("1")
    pkgidbox.draw(win2)                
    pkgidname = Text(Point(300,90), 20)
    pkgidname.setText("")
    pkgidname.draw(win2)                                
    pkgiddest = Text(Point(300,130), 20)
    pkgiddest.setText("")
    pkgiddest.draw(win2)                                
    pkgidweight = Text(Point(300,170), 20)
    pkgidweight.setText("")
    pkgidweight.draw(win2)                                
    pkgidCID = Text(Point(300,210), 20)
    pkgidCID.setText("")
    pkgidCID.draw(win2)                                    
                    
    # Draws the rectangle splash box
    searchbox = Rectangle(Point(400, 40), Point(580,100))
    searchbox.setFill('green')
    searchbox.draw(win2)                    
    
    # Search text to tell user to click here to interact                    
    pkgsearch=Text(Point(490,50),"<---  Enter Package ID")
    pkgsearch.draw(win2)
    pkgsearch1=Text(Point(490,80),"Click to Search")
    pkgsearch1.draw(win2)                   
    
    # Exit button
    exitFunc = Rectangle(Point(450, 240), Point(590, 290)) # box for exit
    exitFunc.setFill('red')
    exitText = Text(Point(520, 265), "Exit")
    exitFunc.draw(win2)
    exitText.draw(win2)
    
    # Add package to system button
    AddFunc = Rectangle(Point(10, 240), Point(160, 290)) # box for exit
    AddFunc.setFill('orange')
    AddText = Text(Point(80, 265), "Add Package\n Window")
    AddFunc.draw(win2)
    AddText.draw(win2)    
    
    # Delete package from system button
    DelFunc = Rectangle(Point(170, 240), Point(290, 290)) # box for exit
    DelFunc.setFill('red')
    DelText = Text(Point(230, 265), "Delete Package\n Window")
    DelFunc.draw(win2)
    DelText.draw(win2)        
    
    # Print Functions Button
    PrintFunc = Rectangle(Point(300, 240), Point(420, 290)) # box for exit
    PrintFunc.setFill('purple')
    PrintText = Text(Point(360, 265), "Print Functions\n(NewWindow)")
    PrintFunc.draw(win2)
    PrintText.draw(win2)            
    
    # Run function that detects users actions in QMS Package Menu
    detect_pkg_actions()    
    
    
# main function that creates the shipyard and then loads the QMS menu
def main():
    global win, q # allow global use of win and q the shipyard class
    # Turn the system online
    q=Shipyard() # create shipyard
    # load graphical menu
    win = GraphWin("Shipyard Management System - QMS", 800, 600) 
    win.setBackground('white') # set bgcolor
    splash_Screen() # load splash screen
    graph_menu()    # load graphical menu
    detect_actions() # load mouse event handler