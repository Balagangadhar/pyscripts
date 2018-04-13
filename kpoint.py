import xml.etree.ElementTree as ET
import os
import glob

#A function to extract eigen value data  from xml file and returns data as a list.
def extract_eigenvalues(path):
    tree = ET.parse(path)
    root = tree.getroot()
    evals_element = root[2]
    # total amount of items
    d = str.strip(evals_element.text).splitlines()
    data_in_ev = []
    for val in d:
        data_in_ev.append(float(val)*27.2114)
    kindex = root[0].attrib['ik']    
    return [kindex]+data_in_ev

thefile = open('kpoint.txt', 'w')

#Read all the folders with extension .save
for d in glob.glob('*.save'):
    #List all the k* directories within the *.save directory
    for k_dir in glob.glob(d+'/'+'K*'): 
        #Path to xml data file
        xml_file_path=k_dir+'/eigenval.xml'
        data = extract_eigenvalues(xml_file_path)
              
        #Write eigen value data as a row into the file correspoinding to each k-point
        for item in data:
                thefile.write("%s\t" % item)
        thefile.write("\n")

            
            
            