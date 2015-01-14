""" Script to scan wgets for specified year entries and generate a new script"""
from __future__ import print_function
import sys
import glob


def gen_script(infolder,outfnm,all_script=True):
    ''' Module to generate the wget script of specified years, from searching wgets
    within a folder.
    '''
    # Boiler-plate code
    in_path = 'Input/'+infolder+'/'
    out_path = 'Output/'
    dep_path = 'Depend/'
    wget_list = glob.glob(in_path+'*.sh')
    add_path = '/work/users/blaken/ECCO/CORDEX/Data_CORDEX/'
    #outf = out_path + 'test.sh'
    outf = out_path + outfnm
    outgrp = []
    stest_list =['19710101','19760101','20010101','20060101','20310101','20360101',
                '20610101','20660101','20910101','20960101']

    # Gather list of files
    print('Reading from the following files:')
    for n in wget_list:
        print(n)

    # Gather head and tail information of wget script if required
    if all_script == True:
        head=[]
        tail=[]
        headfile = open(dep_path+'script_head.sh','r')   
        for line in headfile:
            head.append(line)      
        headfile.close()
        tailfile = open(dep_path+'script_tail.sh','r')   
        for line in tailfile:
            tail.append(line)      
        tailfile.close()

    # Identify the lines in each file required and append them to a list
    for diff_script in wget_list:            # For each autogenerated wget script
        searchfile = open(diff_script,'r')   # Read the script
        for line in searchfile:
            for stest in stest_list:         # Find lines which match to stest_list entries
                if stest in line: 
                    #print line,'\n'
                    outgrp.append(line)      # Append the line if matched
        searchfile.close()
    outgrp = sorted(outgrp)  # Sort the list of variables aphabetically (on variable here)

    # Write the script   
    with open(outf,'w') as out_file:
        if all_script == True:
            out_file.writelines(head)
            for nentries in outgrp:
                out_file.write('\''+add_path + nentries[1:])  #Write the lines and add a path
            out_file.writelines(tail)
        if all_script == False:    
            for nentries in outgrp:
                out_file.write('\''+add_path + nentries[1:])  #Write the lines and add a path
    print('Created script %s'%{outf,})



def main():
    """Main entry point for the script"""
    print('Please run the function gen_script(inputfolder,output_filename,all_script=True)')
    pass


if __name__ == '__main__':
    sys.exit(main())