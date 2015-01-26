#      QMS Classes/Functions stored in this file
#      Main methods are used from Shipyard class
#      (ie. traverseGrabPackageInside uses traverseGrabPackage
#      within container class) to access container/package class methods.
#

# double linked list functions taken from Ron's lecture slides / DLListV2.py
# to hold the container nodes
class Shipyard :
    
    # this Node class acts as the holder of each element of the linked list
    # each node holds a value for the forward and backwards element unless it is a head or tail which it is then None.
    class _Node :
        def __init__(self, elem, next = None, back = None) :
            self._elem = elem
            self._next = next
            self._back = back
            
    # on initialization, this list is empty so make sure front and rear are None
    # same with the size, it is 0 until something is put into it.
    def __init__(self) :
        self._header = self._Node(None) # prepares the sentinel node
        self._trailer = self._Node(None) # prepares the sentinel node
        self._header._next = self._trailer # prepares the sentinel node
        self._trailer._back = self._header # prepares the sentinel node
        self._size = 0  # initial size of doubly linked list
        self.uniqueID = 0   # unique id generation for packages
        self.uniqueContainerID = 0  # unique id generation for containers
        self.containers = ""
        # main yard data file, can save/load
        # current functioning system into this file
        self._destContainer = ""
    
    # overload len so that if you len(q) it will show the number of items in the linked list
    def __len__(self) :
        return self._size # details how many containers there are in the shipyard
    
    # create a container node holding pointer to container object
    # elem = destination, id = container id
    # they are alphabetically sorted
    def createContainer(self, id, elem) :
        
        # if file loading, uses this function and puts in saved id's in text file
        if id != "None":
            self.containers = self.Container(id, "Calgary")
        # if creating a container, the system will generate a id
        if id == "None":
            self.uniqueContainerID += 1    
            testcid = self.traversePrint(self.uniqueContainerID)
            # keep trying new container id's till one is available
            while (testcid == "used"):
                self.uniqueContainerID += 1
                testcid = self.traversePrint(self.uniqueContainerID)
            self.containers = self.Container(testcid, "Calgary")
            # store the id as id for later
            id = testcid
            
        # sorted insert containers in alphabetical order
        # increase size + 1
        self._size += 1
        
        # Duplicate values are inserted in this method. I have a check function for duplicates.
        
        insPoint = self._header
        while (insPoint._next != self._trailer and elem >= insPoint._next._elem) :
            insPoint = insPoint._next
        postPoint = insPoint._next
        newNode = self._Node(elem, postPoint, insPoint) # creation of new node
        newNode._container = self.containers # contain the pointer to the created container
        newNode._container._id = id # store container id
        newNode._container._destination = elem # store destination information inside the container
        insPoint._next = newNode   # to allow sorted insert
        postPoint._back = newNode  # to allow sorted insert
        return (self.containers)
        
      
    # Packages are sorted by weight.  
    # Creates a package, checks if container is ready, makes one if it isn't
    # then, inserts package into the container.
    # it will check if weight will exceed 2000 lbs within container, if so,
    # a new container is made
    # a check for a package exceeding 2000 lbs is done via the menu
    # the system will not allow a package over 2000 lbs entered via the menu
    def createPackage(self, id, name, destination, weight) :
        # init vars
        #packageholder holds pointer to created package object
        packageholder = ""
        #_destContainer holds pointer to container object
        self._destContainer = ""
        
        # traverse containers to check for matching destination + suitable weight
        self._destContainer = self.traverseFindDest(destination, weight)
        
        # if new container needed where no container made
        # or not enough weight
        if (self._destContainer == "new container needed"):
            self._destContainer = self.createContainer("None", destination)
        
        # if given id, use given id (when loading from file)
        if id != "None":
            packageholder = self.Package( str(id), name, weight, destination)
            #save pointer to package in container node
            self._destContainer.insertPackage(packageholder)
            # increase number of packages by 1
            # increase total weight of container
            self._destContainer._numpkgs += 1
            self._destContainer._weight += int(weight)
        
        # when inserting package via menu with no id, system generates id
        if id == "None":         
            self.uniqueID += 1
            # make sure packageID is unique
            checkPID = self.traverseGrabPackageInside(str(self.uniqueID))
            # duplication check on unique id, increase by 1 if id found
            while (checkPID[0] != "Package Not Found"):
                self.uniqueID += 1
                checkPID = self.traverseGrabPackageInside(str(self.uniqueID))
            packageholder = self.Package( str(self.uniqueID), name, weight, destination)
            #save pointer to package in container node            
            self._destContainer.insertPackage(packageholder)
            # increase count of number of packages
            self._destContainer._numpkgs += 1
            # decrease weight by removed package
            self._destContainer._weight += int(weight)
            
    # Store package into specified container
    # This function is used when loading yard data with containers and packages
    def loadStorePackage(self, id, name, destination, weight, cid) :
        # init vars
        packageholder = ""
        self._destContainer = ""
        
        # traverse containers to check for matching destination + suitable weight
        self._destContainer = self.traverseFindByCID(cid)
        
        # if new container needed where no container made
        # or not enough weight
        if (self._destContainer == "new container needed"):
            self._destContainer = self.createContainer("None", destination)
        
        # if given id, use given id (when loading from file)
        if id != "None":
            packageholder = self.Package( str(id), name, weight, destination)
            #save pointer to package in container node
            # increase container's number of package count
            # increase total weight of container
            self._destContainer.insertPackage(packageholder)
            self._destContainer._numpkgs += 1
            self._destContainer._weight += int(weight)
        
        # when inserting package via menu with no id, system generates id
        if id == "None":         
            self.uniqueID += 1
            # make sure packageID is unique
            checkPID = self.traverseGrabPackageInside(str(self.uniqueID))
            # duplication check on unique id, increase by 1 if id found
            while (checkPID[0] != "Package Not Found"):
                self.uniqueID += 1
                checkPID = self.traverseGrabPackageInside(str(self.uniqueID))
            packageholder = self.Package( str(self.uniqueID), name, weight, destination)
            #save pointer to package in container node            
            self._destContainer.insertPackage(packageholder)
            # increase count of number of packages
            self._destContainer._numpkgs += 1
            # decrease weight by removed package
            self._destContainer._weight += int(weight)
    
    # delete specific package by its package ID looking through containers
    # it accesses the function deletePackageByID in the container class
    # once the container containing the package is found
    # otherwise it reports package not found
    def deletePackageByIDInside(self, findpkgid) :
        tmpRef = self._header._next
        while (tmpRef != self._trailer):
            findpkg = tmpRef._container.traverseGrabPackage(findpkgid)
            if (findpkg[0] != "Package Not Found"):
                tmpRef._container.deletePackageByID(int(findpkg[0]))
                tmpRef._container._numpkgs -= 1
                tmpRef._container._weight -= int(findpkg[3])
                return ("Package Deleted From System")
            tmpRef = tmpRef._next
        return ("Package Not Found", "", "", "", "")                      
    
    # Delete Containers based on destination which accesses container CID
    # to delete specified container
    # Not used, but it is a useful function.
    # it can delete all the containers that have the same destination given.
    def deleteContainersDest(self, dest) :
        tmpRef = self._header._next
        # keep doing till all containers with the destination are removed
        while (tmpRef != self._trailer):
            # if matching destination, delete container by matching CID
            if (tmpRef._container._destination == dest):
                self.deleteContainerByCID(tmpRef._container._id)
            tmpRef = tmpRef._next
        return ("Package Not Found", "", "", "", "")                      
    
    # Delete based on container id
    def deleteContainerByCID(self, elem) :
        # This performs a sequential search so it can
        # be used for any DLList().
        # decrease size by 1
        self._size -= 1
        delPoint = self._header._next
        # when found, remove the element and update the doubly linked list
        while (delPoint != self._trailer and str(elem) != str(delPoint._container._id)) :
            delPoint = delPoint._next
        if (delPoint == self._trailer) :
            print ("No more containers to delete")
            return
        pred = delPoint._back
        succ = delPoint._next
        pred._next = succ
        succ._back = pred
        return               

    
    # traversePrint is used to check container to make sure
    # container id is unique when container is created
    def traversePrint(self, cid) :
        tmpRef = self._header._next
        while (tmpRef != self._trailer) :
            if tmpRef._container._id == cid:
                return ("used")
            tmpRef = tmpRef._next
        # return container id because it is unused
        return (cid)
    
# prints out shipping manifest of containers and its package contents with
# matching criteria for destination
# uses containerPackageInfo function to display package info of containers
    def shippingManifestDest(self, destination) :
        # Display headings
        print ("---Shipping Manifest With Specific Destination---")
        print ("-"*25)
        tmpRef = self._header._next
        # while traversing the nodes, detailing information for specific destination
        while (tmpRef != self._trailer) :
            if (tmpRef._container._destination.upper() == destination.upper()):
                print("Container ID: " + str(tmpRef._container._id) + ", Destination: " + str(tmpRef._container._destination) + ", Total Weight: " + str(tmpRef._container._weight) + ", Number of Packages: " + str(tmpRef._container._numpkgs))
                print ("[Package Contents]")
                # print out package information for the container
                tmpRef._container.containerPackageInfo()
                print ("")
            tmpRef = tmpRef._next
        return    
    
# prints out entire shipping yard manifest of containers and its package contents
# uses containerPackageInfo function to display package info of containers
    def shippingManifestAll(self) :
        # Display headings
        print ("---Shipping Manifest With All Information---")
        print ("-"*25)        
        tmpRef = self._header._next
        while (tmpRef != self._trailer) :
            # Display container info
            print("Container ID: " + str(tmpRef._container._id) + ", Destination: " + str(tmpRef._container._destination) + ", Total Weight: " + str(tmpRef._container._weight) + ", Number of Packages: " + str(tmpRef._container._numpkgs))
            print ("[Package Contents]")
            # call container func to grab packages info
            tmpRef._container.containerPackageInfo()
            print ("") # new line spacing to space out each container
            tmpRef = tmpRef._next
        return     
    
    # Prints out a list of containers with their information, including
    # capacity but not their contents.
    def getContainersNoContents(self) :
        # Display headings
        print ("---Container Information With Capacity No Contents---")
        print ("-"*25 + "\n")          
        tmpRef = self._header._next
        while (tmpRef != self._trailer) :
            # set up capacity variable since max load is 2000 lbs.
            wgt = 2000 - int(tmpRef._container._weight)
            # Display container info
            print("Container ID: " + str(tmpRef._container._id) + ", Destination: " + str(tmpRef._container._destination) + ", Total Weight: " + str(tmpRef._container._weight) + ", Number of Packages: " + str(tmpRef._container._numpkgs) + ", Capacity: " + str(wgt))
            tmpRef = tmpRef._next
        return    
    
# Search containers by container id
# this function is used for loading packages into specific containers
# determined by loading a Yard Data file
    def traverseFindByCID(self, cid) :
        # in the case that the doubly linked list of containers have no contents
        # make the container to contain the package
        tmpRef = self._header._next   # copy the address of the head node into node
        while (tmpRef != self._trailer):
            if tmpRef._container._id == cid:
                # return the container with matching container id
                return (tmpRef._container)
            tmpRef = tmpRef._next
        return
    
# search containers to find destination
    def traverseFindDest(self, dest, weight) :
        # in the case that the doubly linked list of containers have no contents
        # make the container to contain the package
        tmpRef = self._header._next   # copy the address of the head node into node
        # traverse nodes
        while (tmpRef != self._trailer):
            # if destination matches, and weight is okay, return container that
            # will fit the package
            if tmpRef._container._destination == dest:
                if (int(tmpRef._container._weight) + int(weight)) <= 2000:
                    return (tmpRef._container)
            tmpRef = tmpRef._next
        # new container needed if no container that can fit
        return ("new container needed")
        
    # This function tells how many containers are in the system.
    # Unused, but useful function.
    def checkContainerCount(self):
        count=0
        tmpRef = self._header._next
        while (tmpRef != self._trailer) :
            count+=1
            tmpRef = tmpRef._next
        return (count)
    
    # It will ship out containers from the shipyard, removing the containers
    # information from the system. Will report # of containers and total weight
    # delivered.
    def shipOutContainersDest(self, dest):
        container_Count = 0
        total_Weight = 0
        # pass dest and 0 as weight because we are not using weight
        theContainer = self.traverseFindDest(dest, 0)
        if theContainer == "new container needed":
            print ("\nNo containers to be shipped for this destination.")
            container_Count = 0
            total_Weight = 0
            return
            
        # add each package weight in the container to the total_Weight
        # add count to each container being sent to the destination
        total_Weight += int(theContainer._weight)
        container_Count += 1
        self.deleteContainerByCID(theContainer._id)
        theContainer = self.traverseFindDest(dest, 0)
        # while loop to delete all containers to the destination
        # keep checking containers till no more containers with the destination
        while (theContainer != "new container needed"):
            container_Count += 1
            total_Weight += int(theContainer._weight)
            self.deleteContainerByCID(theContainer._id)
            theContainer = self.traverseFindDest(dest, 0)
        # display how many containers shipped and the weight
        print (str(container_Count) + " Containers Shipped to " + str(dest))
        print ("Total of " + str(total_Weight) + " lbs. shipped to " + str(dest))
        container_Count = 0
        total_Weight = 0
    
    # It traverses the containers and searches for matching package id
    # using the container method, traverseGrabPackage
    def traverseGrabPackageInside(self, findpkgid) :
        tmpRef = self._header._next
        # traverse nodes
        while (tmpRef != self._trailer):
            # while package not found yet, keep cycling
            findpkg = tmpRef._container.traverseGrabPackage(findpkgid)
            if (findpkg[0] != "Package Not Found"):
                findpkgupdate = (findpkg[0], findpkg[1], findpkg[2], findpkg[3], tmpRef._container._id)
                # if found, return the values so it can be displayed in the menu
                return (findpkgupdate)
            tmpRef = tmpRef._next
        # if package is not found return that it is not found
        return ("Package Not Found", "", "", "", "")        

    # Function to save a state of the shipyard into a designated filename
    # save current yard data to container and package format file
    def saveYardData(self, filename) :
        wholeString = ""
        saveString = ""
        print ("---Saving All Shipyard Data---")
        print ("-"*25)
        
        tmpRef = self._header._next
        while (tmpRef != self._trailer) :
            # to indicate it is the container
            saveString = "% "
            # join together save string data
            saveString = saveString + str(tmpRef._container._id) + ", " + str(tmpRef._container._destination)
            # call container func to grab packages info
            saveString = tmpRef._container.containerSavePackageInfo(saveString)
            wholeString = wholeString + saveString
            tmpRef = tmpRef._next
        file = open(filename, "w")
        file.write(wholeString)
        print ("Yard Data Saved to " + str(filename))
        return            

# load Yard Data into system so the system can shutdown and resume where it left off
    def loadYardData(self, filename) :
        # set initial states for comma detection
        contcomma = False
        firstcomma = False
        secondcomma = False
        # initialize variables
        box1 = ""
        box2 = ""
        box3 = ""
        contbox1 = ""
        contbox2 = ""
        # open the file for reading
        file = open (filename)
        #store file data into readYardData
        readYardData = file.readlines()
        
        # deal with % meaning this is a container
        # resets destination, contbox2 when a new container is found
        for data in readYardData:
            if data[0] == '%':
                contbox1 = ""
                contbox2 = ""
                # organize data based on text file format
                for cont_entry in data:
                    for letter in cont_entry:
                        if letter != ',' and letter != '%' and contcomma == False:
                            contbox1 = contbox1 + letter
                        if letter == ',' and contcomma == False:
                            contcomma = True
                        if letter != ',' and contcomma == True:
                            contbox2 = contbox2 + letter
                # strip whitespaces from beginning and end
                contbox1 = contbox1.strip()
                contbox2 = contbox2.strip().upper()
                # create containers given the information
                self.createContainer(int(contbox1), contbox2)
                contcomma = False
                
        # deal with packages portion of loading
            if data[0] != '%':
                for letter in data:
                    if letter != ',' and firstcomma == False and secondcomma == False:
                        box1 = box1 + letter
                    if letter ==',' and firstcomma == True and secondcomma == False:
                        secondcomma = True                
                    if letter == ',' and firstcomma == False and secondcomma == False:
                        firstcomma = True
                    if letter != ',' and firstcomma == True and secondcomma == False:
                        box2 = box2 + letter
                    if letter != ',' and firstcomma == True and secondcomma == True:
                        box3 = box3 + letter
                # strip white spaces from beginning and end
                box1 = box1.strip()
                box2 = box2.strip().upper()
                box3 = box3.strip().upper()
                # create packages, contbox2 = destination grabbed from above
                self.loadStorePackage(box1, box2, contbox2, str(box3), int(contbox1))
                # reset the box to grab next value
                box1 = ""
                box2 = ""
                box3 = ""
                # reset the comma checks
                firstcomma = False
                secondcomma = False
        print ("Yard Data Loaded from " + str(filename))
            
        
# function to load package-only data into system ie. packages.txt
    def loadPackagesFromFile(self, filename):
        global box1, box2, box3
        box1=""
        box2=""
        box3=""
        firstcomma = False
        secondcomma = False
        file = open (filename)
        readYardData = file.readlines()
        for entry in readYardData:
            for letter in entry:
                if letter != ',' and firstcomma == False and secondcomma == False:
                    box1 = box1 + letter
                if letter ==',' and firstcomma == True and secondcomma == False:
                    secondcomma = True                
                if letter == ',' and firstcomma == False and secondcomma == False:
                    firstcomma = True
                if letter != ',' and firstcomma == True and secondcomma == False:
                    box2 = box2 + letter
                if letter != ',' and firstcomma == True and secondcomma == True:
                    box3 = box3 + letter
            # set upper case to necessary values so it is easier to search
            # strip is to strip the white spaces
            box1 = box1.upper().strip()
            box2 = box2.upper().strip()
            box3 = box3.strip()
            self.createPackage("None", box1, box2, int(box3))
            box1 = ""
            box2 = ""
            box3 = ""
            firstcomma = False
            secondcomma = False
        print ("Packages loaded from " + str(filename))

    
# Container class where a new container is created in the circumstance that there
# is a new destination or when packages to the same destination exceed 2000 lbs.
# Uses a doubly linked list.
    class Container :
        
        def __init__(self, id, destination) :
            self._header = self._Node(None) # sentinel node
            self._trailer = self._Node(None)    # sentinel node
            self._header._next = self._trailer  # set up linking
            self._trailer._back = self._header  # set up linking
            self._size = 0  # initial size of doubly linked list            
            self._numpkgs = 0 # container variable for number of packages
            self._weight = 0 # sum of weight of packages
            self._destination = destination # destination
            self._id = id # container id
        
# this Node class acts as the holder of each element of the linked list
# each node holds a value for the forward and backwards element unless
# it is a head or tail which it is then None.
        class _Node :
            
            # sentinel node declarations
            def __init__(self, elem, next = None, back = None) :
                self._elem = elem
                self._next = next
                self._back = back        
      
        # displays package contents info of container
        def containerPackageInfo(self) :
            tmpRef = self._header._next
            while (tmpRef != self._trailer) :
                print("Package ID: " + str(tmpRef._package._id) + ", Owner: " + str(tmpRef._package._name) + ", Weight: " + str(tmpRef._package._weight) + ", Destination: " + str(tmpRef._package._destination))
                tmpRef = tmpRef._next
            return     
        
        # used when saving yard data for the package information
        def containerSavePackageInfo(self, saveString) :
            saveString = saveString + ("\n")
            tmpRef = self._header._next
            while (tmpRef != self._trailer) :
                saveString = saveString + str(tmpRef._package._id) + ", " + str(tmpRef._package._name) + ", " + str(tmpRef._package._weight) + "\n"
                tmpRef = tmpRef._next
            return (saveString)
        
        # it traverses the container and searches for matching package id
        def traverseGrabPackage(self, findpkgid) :
            tmpRef = self._header._next
            while (tmpRef != self._trailer):
                # if matching, return package information to be used in the menu
                if (tmpRef._package._id == findpkgid):
                    return (tmpRef._package._id, tmpRef._package._name, tmpRef._package._destination, tmpRef._package._weight)
                tmpRef = tmpRef._next
            # if it gets here, package wasn't found
            return ("Package Not Found", "", "", "")        
        
        # inserts package pointer into container node
        def insertPackage(self, packageholder) :
            self._size += 1
            insPoint = self._header
            while (insPoint._next != self._trailer and str(packageholder._weight) >= str(insPoint._next._elem)) :
                insPoint = insPoint._next
            postPoint = insPoint._next
            # create new node
            newNode = self._Node(packageholder._weight, postPoint, insPoint)
            newNode._package = packageholder    # store pointer to package
            insPoint._next = newNode    # link next node
            postPoint._back = newNode   # link prev node  
            
        # Delete specific package by its package ID inside a container
        def deletePackageByID(self, elem) :
        # This performs a sequential search so it can
        # be used for any DLList().
        # If the value is not there, an error message is presented.
            self._size -= 1
            delPoint = self._header._next
            # when deletion point is found, update the list to exclude the node
            while (delPoint != self._trailer and str(elem) != str(delPoint._package._id)) :
                delPoint = delPoint._next
            if (delPoint == self._trailer) :
                print ("Not in this container")
                return
            # update doubly linked list pointers
            pred = delPoint._back
            succ = delPoint._next
            pred._next = succ
            succ._back = pred
            return                  
            
    
    # This function tells how many packages are in the container
    # Did not actually use, used _numpkgs stored as a variable in the container
        def checkPackageCount(self):
            count=0
            tmpRef = self._header._next
            while (tmpRef != self._trailer) :
                count+=1
                tmpRef = tmpRef._next
            return (count)
    
    
# Package class where each package created is entered into containers where
# they will be shipped out of the shipyard eventually
    class Package :
        
        def __init__(self, id, name, weight, destination) :
            self._id = id     # system generated package id
            self._name = name   # owner name
            self._weight = weight # package weight in lbs.
            self._destination = destination   # destination