import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    print("This is the path to convert the file xml files to csv " + str(path))
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            #reading this xml information and storing in a tuple, and then appeneding to a list
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
            #print("This is the value to be appended to the list.>")
            #print(value)
    # print("Here is the final list...")
    # print(xml_list)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    # pandas will convert the list of the elements into a dataframe!!
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    print("Here is the dataframe...")
    print(xml_df)
    return xml_df


def main():
    print("The current directory .." + str(os.getcwd()))
    image_path = os.path.join(os.getcwd(), 'annotations')
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('csvFilewithImageDetails.csv', index=None)
    print('Successfully converted xml to csv.')


main()
