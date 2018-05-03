'''
Title: Thanos did he kill me with saving
Author: Riley Carpenter
'''
import random
import os
import sys
import getpass
didThanoskillme = random.randint(1,2)
user = getpass.getuser()
dir_path = os.path.dirname(os.path.realpath(__file__))
if (os.path.exists(dir_path +"/SaveforThanos")) == False:
    os.makedirs(dir_path + "/SaveforThanos")
    if didThanoskillme == 1:
        print("You were killed for the glory of Thanos")
        os.makedirs(dir_path + "\SaveforThanos\save1")
    else:
        print("Thanos spared you mere mortal")
        os.makedirs(dir_path + "\SaveforThanos\save2")
else:
    if (os.path.exists(dir_path + "\SaveforThanos\save2")) == True:
        print("You already learned that you were spared what more do you want?")
    else:
        print("You know you were killed by Thanos, bow before his glory")
