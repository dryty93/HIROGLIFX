from lineCount import countLines
from variable import Variable
from dictionary import Dictionary
from lib_funcs import Lib_Funcs
from loops import loopThrough
from bool_logic import Bools
from lineCount import line_location
from user_defined_functions import Functions
from user_blueprints import UserBP
from gui_capabilities import makeWindow

import time


countLines()


print("Hir\x07Glifx v.0.1:")

class StartInterpret():

    def __init__(self):
        pass

    def initialize_interpreter(self):
        """This starts the HiroGlifx interpretter """

        time.sleep(1)
        print("Interpretting.\x07.\x07.\x07")
        self.run_interpreter()

    @classmethod
    def run_interpreter(self):
        while True:


            line_list = []
            dict_look_up = []
            with open('scroll.glif', 'r') as readFile:

                self.readFile = readFile
                self.line_list = line_list

                self.dict_look_up = dict_look_up


                for line in readFile:
                    self.line = line


                  #  print(self.line_class_var)
                    #print(self.line)

                    var = Variable()


                    if '/*' in self.line:
                        self.line = next(self.readFile)


                    if 'loop_through' in line:
                        self.line = self.line + next(self.readFile)
                        loopThrough()
                    if '!' in self.line:
                        Bools().ifs_init()
                    if 'dict' in self.line:

                        if 'write' not in self.line:
                            if '!' not in self.line:
                                if '^' not in line:
                                    Dictionary().dictMaker()


                    if '^' in self.line:
                        self.dict_look_up.append(line)

                    if 'BluePrint' in line:
                        UserBP.bp_find_name(self,line)


                    if 'have' in line:
                        UserBP.bp_get_attributes(self,line)




                    if 'var' in self.line:
                        if '!' not in self.line:
                            if 'write' not in self.line:
                                if 'list' not in self.line:
                                    if 'dict' not in self.line:
                                        Variable().newVariable()


                    if 'def func' in self.line:
                        Functions().init_function()

                    if 'write' in line:
                        if 'func' not in line:
                            Lib_Funcs().write()
                    if 'index' in line:
                        Dictionary().init_indexDict()
                    if 'gui' in line:
                        if 'window' in line:
                            n = line.split('=')[1]
                            length = n.split(' ')[1].split(',')[0]
                            width = n.split(',')[1].split('\n')[0].split(' ')[-1]
                            makeWindow(int(length),int(width))

                    if 'brk' in line:
                      #  print(line_location)

                        exit()

StartInterpret().initialize_interpreter()