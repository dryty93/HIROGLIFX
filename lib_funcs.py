from dictionary import Dictionary,dictOfDicts
from variable import Variable, varCount,varNameList,var_look_up_list
from random import randrange
class Lib_Funcs():
    def __init__(self):
        pass

    def write_function_in_functions(self,content_to_write):
        content_to_write = content_to_write.split("write")
        print(content_to_write)

    def write(self):
        global function_state
        global line
        from main import StartInterpret
        line = StartInterpret.line
        # function state checks if the write function has been run already.
        # if the write function is the first line in the scroll.glif file
        # the code will execute and the function state keeps track of the iterations the code
        # runs to see if it is necesarry to import line again
        function_state = 0


        if function_state == 0:

#            print(line, 'line here')
            function_state += 1
        # this writes simple text to screen
        if '!' not in line:
            if ",," not in line:
                if 'var' not in line:
                    if '#' not in line:
                        if '$' not in line:
                            if 'dict' not in line:
                                if 'list' not in line:
                                    if '    ' not in line:
                                        writeThis = line.split("(")[-1].split(')')[0]
                                    if "+" or "-":
                                        print(writeThis)
                                if 'list' in line:
                                    print(line,'list')
                            if 'dict' in line:
                                Dictionary().init_indexDict()
                        if '$' in line:
                            pass
                    if '#' in line:
                        pass
                if 'var' in line:
                    Variable().writeVar()
            if ',,' in line:
                write_mult = line.split('e(')[1].split(')')[0].split(',,')
                multi_line_write_statement = []
                for items in write_mult:
                    if 'var' in items:
                        Variable().varLookUp(items)
                        multi_line_write_statement.append(var_look_up_list[-1])
                    else:
                        item_as_string = items
                        item_as_string = " " , item_as_string , " "
                        item_as_string = ''.join(item_as_string)
                        multi_line_write_statement.append(item_as_string)


                print(multi_line_write_statement)
    def writeDict(self):

        dictGetter = line.split("(")[-1].split(")")[0]

       # for i in dictOfDicts:
        #    print(dictOfDicts[i])


    def randTen(self):
        randomVar = str(randrange(1, 11))
        randomList.append(randomVar)
        randomVarF = str(randomList[0])
        #varDict[str(w[0])] = randomVarF


    def randHun(self):
        randomVar = str(randrange(1, 101))
        randomList.append(randomVar)
        randomVarF = str(randomList[0])
        #varDict[str(w[0])] = randomVarF


    def randomize(self):
        '''Creates random ranges in increments of 1-5, 1-10 and 1-100'''
        global randomList
        global randomVarF

        if 'rand5' in line:
            self.randFive()

        if 'rand100' in line:
            self.randHun()

        if 'rand10' in line:
            self.randTen()


if __name__=='__main__':
    print("Lib_Funcs Class:"
          "\nThe Lib_Funcs class is used to handle all functions"
          "\nin the HiroGlifx Standard Library(everything that comes "
          "\nshipped with Hiroglifx).")
