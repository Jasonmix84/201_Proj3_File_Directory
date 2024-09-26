"""
File: file_system.py
Author: Jason Rojas
Date: 11/28/22
Section: 42
E-mail: jasonr2@umbc.edu
Description:
Program simulates a file_system
"""
def check_if_dir_exists(path):
    for values in path:
        pass

def find_backslash(string):
    for character in string:
        if character == '/':
            return True
    
def add_brackets(string):
    new_string = '['+string+']'
    return new_string


def add_front_backslash(string):
    new_string= '/' + string #might have to change thsi to make more sense
    return new_string

def remove_backslash_briefly(string):
    if string[0] == '/':
        new_string = string[1::]
        return new_string
    else:
        return string

def get_directory(sub_directory):
    for dir, sub_dir in current_directory.items():
        if sub_directory == sub_dir:
            return dir

def ls(directory_name_or_path, list_of_paths):
    if directory_name_or_path[3] == '/ ': #cases where it is asking absoluse ls
        pass
    else: #normal cases
        for i in list_of_path:
            for values in file_system[i]:
                return ls(values, i)

        
def mkdir(directory_name, current_dir, file_system):
    for character in directory_name:   #set the condition that doesnt allow bad names
        if character == '/':
            print("Invalid Directory Name \n Directory Name Cannot Contain '/'")
            return
    new_dir_name = add_front_backslash(directory_name) #have a forward slash on all directories will help me later

    if file_system[current_dir] == first_dir: #first directory make a directory in first one   may have to change this not sure if i can even call first_dir
        first_dir[new_dir_name] = {}
        return
    
    else:
        for key, val in file_system.items():
            if current_dir in file_system.keys():
                if key == current_dir:
                    val[directory_name] = dict()
                    print(val)
            else:
                return mkdir(directory_name, current_dir, val) 
    
    
    # else: #another directory which may not work at a third layer of directory "I might implement a list of previous dirs and a counter so i can continue adding as many directorues ill finish everything else first tho"
    #     if file_system[current_dir] == 


def cd(directory_name_or_path, current_dir, previous_dir, first_dir): #all my directories have a secret '/' added to them
    if directory_name_or_path == "/..":
        return previous_dir #set the current_dir to the previous current_dictionary
    elif directory_name_or_path == '//':
        return first_dir #set the current_dir to root_dir so all the way back
    elif directory_name_or_path == '/.' or directory_name_or_path == '/' or directory_name_or_path == '/ ':
        return current_dir#does nothing except keet the same cd so ig make them reinput through
    #regular, absolute, and relative paths below
    #at the end of each one I have to make sure I check if that direcectory works 
    else:
        levels_list = directory_name_or_path.split('/')
        if len(levels_list) == 0: #regular case Completed
            if current_dir in file_system[previous_dir]: #if you have time make stuff below a helper function cause you use it for relative paths
                returning_list = []
                previous_dir = current_dir
                returning_list.append(previous_dir)
                new_current_dir = current_dir + add_brackets(directory_name_or_path)
                returning_list.append(new_current_dir)
                return returning_list
            else:
                returning_list = []
                returning_list.append('No Such Directory!!!')
                return returning_list
        else:
            if levels_list[0] == '' and levels_list[1] == '': #absolute path case #may have fucked up the fact that there is a forward slash infront of everything
                levels_list.remove(levels[0])
                absolute_path = file_system['/']
                for levels in range(len(levels_list)-1):
                    if levels in absolute_path:
                        previous_dir = absolute_path
                        absolute_path = absolute_path + add_brackets(levels)

                    else:
                        returning_list = []
                        returning_list.append('No Such Directory!!!')
                        return returning_list
                returning_list = []
                returning_list.append(previous_dir) #check if this is correct
                returning_list.append(absolute_path)
                return returning_list
                
                        
            else: #relative path #this may be correct  be sure to check it
                for levels in range(len(levels_list) - 1):
                    if levels in current_dir: #use the in to check and change current dir for each part of relative path
                        previous_dir = current_dir 
                        current_dir = current_dir + add_brackets(levels) #the new current_dir should be added
                    else: #this happends when at some point the relative path fails cause it doesnt exist in that order
                        returning_list = []
                        returning_list.append('No Such Directory!!!')
                        return returning_list
                returning_list = []
                returning_list.append(previous_dir) #check if this is correct
                returning_list.append(current_dir)
                return returning_list


def rm(file_name_path, current_dir): #this should work assuming that cd works
    for levels in current_dir: #might have to be more specific and might have to add.values or something
        del file_system[current_dir[levels]]
        return file_system
        #figure out how to change current dir to be list instead and then make it
        #possible to build the dir instead of what im currently doing ittle make like easier

def locate(file_name): 
    for keys, vals in dict.items():
        if keys == file_name:
            checking_dir = current_directory        
            directories_list = [current_directory]
            while checking_dir != '/':
                checking_dir = get_directory(checking_dir)
                checking_dir.append(directories_list)
            return checking_dir
        else:
            return locate(file_name)

def touch(file_name_path, current_dir):
    for character in file_name_path:
        if character == '/':
            return print("Invalid file name cannot contain a '/'")
    current_dir = file_name_path    #also wrong cause current_dir is a string not a list like it should be
    return current_dir

if __name__ == '__main__':
    #code
    file_system = {'/':{}}
    first_dir = file_system['/'] #might change this later as not sure if this would be correct to call this a file
    current_directory = '/' #set current_dirrectory to the root_directory #this is wrong it sets it to the value not what i thought it did
    previous_directory = first_dir
    running_condition = True
    while running_condition == True:
        list_of_path = ['/']
        inputs = input('[cmsc201 proj3]$ ')   #constantly ask 

        if inputs == 'exit':                #exit condition
            running_condition = False
        
        elif inputs == 'pwd':     #THis thought process is correct I think just not sure how its gonna work have to run a test on it
            checking_dir = current_directory        
            directories_list = [current_directory]
            while checking_dir != '/':
                checking_dir = get_directory(checking_dir)
                checking_dir.append(directories_list)


        elif inputs[0:2] == 'ls':
            ls(inputs)

        elif inputs[0:5] == 'mkdir': #im pretty sure i finished this
            mkdir(inputs[6::], current_directory, file_system)
            print(file_system)
            
        
        elif inputs[0:2] == 'cd': #there is something really wrong here so check it later in the meantime try to make the other functions assuming it works
            new_input = add_front_backslash(inputs[3::])
            print(new_input)
            index = len(list_of_path)
            previous_and_currrent = cd(new_input, list_of_path[index - 1], list_of_path[index - 2], list_of_path[0])
            # current_directory = current_directory + new_input #might change this 
            if previous_and_currrent[0] == 'No Such Directory!!!':
                print('No Such Directory')
                print('If an absolute or relative path was entered be sure to check directories entered')
                
            else:
                previous_directory = previous_and_currrent[0]
                current_directory = previous_and_currrent[1] 
                print(previous_directory)
                print(current_directory)

        
        elif inputs[0:2] == 'rm':
            rm(inputs[2::], current_directory)
        
        elif inputs[0:6] == 'locate':
            locate(inputs[7::])

        elif inputs[0:5] == 'touch': #check this with w3schools
            touch(inputs[6::])

        else:
            print(inputs, ': Command not found.')
             