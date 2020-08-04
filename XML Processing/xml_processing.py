# xml processing

import xml.etree.ElementTree as ET

open_file = True
while open_file:
    try:
        xml_file_input = input("Enter the name of the XML file: ")
        mytree = ET.parse(xml_file_input)
        myroot = mytree.getroot()
        open_file = False
    except:
        print("Error in opening file")
        try_again = ''
        while try_again not in ['y', 'Y', 'n', 'N']:
            try_again = input("Try again?(y/n): ")
        if try_again == 'y' or try_again == 'Y':
            pass
        else:
            exit()

def find_attribs(key, mytree):
	for elem in mytree.iter():
		if key == elem.tag:
			attr = {}
			for x in elem.attrib.keys():
				value = input(f'Enter {x}: ')
				attr[x] = value

			for elems in mytree.iter():
				if key == elems.tag and attr == elems.attrib:
					flag = 1
					print('--------------------------------------')
					new_key = input(f'Enter a tag to search in {key} with attrib {attr}: ')
					return find_tag_value(new_key, elems)

			return []


def find_tag_value(key, mytree):
	flag = 0
	my_list = []

	for elem in mytree.iter():
		L1 = []
		if key == elem.tag:
			L1.append(elem.tag)
			if len(elem.attrib) != 0:
				flag = 1
				L1.append(elem.attrib)
			L1.append(elem.text)
			T1 = tuple(L1)
			my_list.append(T1)

	if flag == 1:
		return find_attribs(key, mytree)
	else:
		return my_list

while True:
    key = input("Enter a tag to search: (or 'q' to quit): ")
    if key=='q':
        break
    else:
        result = find_tag_value(key, mytree)

        print('\n')
        if len(result) == 0:
                print('No tag found')
        else:
                for x,y in result:
                        print(x, end='\t')
                        print(y)
