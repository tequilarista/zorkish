import os
import json

class Character:
    """Player attributes, inventory, other metadata"""

    def __init__(self, name, debug=False):
        print ("Initializing...")
        self.name = name
        self.debug = debug
        self.stateFile = self.name + "_state.json"
        self.currentState = self.LoadState()
        if self.debug:
            print("FCN: LoadState")
            print("name: ", self.name)
            print(self.debug)
            print("stateFile: ", self.stateFile)

    def initStateFile(self):
        """ template for character metadata.  Create and cache out. """
        if self.debug:
            print("FCN: initStateFile")

        stateStruct = {
            'name': self.name,
            'location': [],
            'inventory':{}
        }
        
        with open(self.stateFile, 'w') as outfile:
            json.dump(stateStruct, outfile)                    

        return stateStruct


    def LoadState(self):
        """ checks to see if there's an existing player state file.
        If not, creates one """

        if os.path.isfile(self.stateFile):
            print("Path exists")
            with open(self.stateFile) as json_file:
                self.currentState = json.load(json_file)
        else:
            print("Path does not exist, initializing")
            self.currentState = self.initStateFile()            

        print("currentState: ", self.currentState)
