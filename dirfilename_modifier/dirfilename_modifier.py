import sys
import os

argc = len(sys.argv);
print(sys.argv);

#setup the files
input_file = open("user.csv", "r");

folder_name = "./dir/";
output_filename = "img.csv";
output_file_csv = open(output_filename, "w");
column_title = "username";

#read each lines of the input csv file and change files in the dir list in order
img_name_list = os.listdir(folder_name);
i = 0;
j = 0;
index = 0;
for line in input_file:
    if (i == 0):
        l = line.split(", ");
        found = False;
        for data in l:
            if (data == column_title):
                found = True;
                break;
            index += 1;
        if (not found):
            raise NameError("column title not found");
        output_file_csv.write("img_name" + "\n");
    else:
        l = line.split(", ");
        if (not os.path.isfile(folder_name + l[index] + "_img.png")):
            os.rename(folder_name + img_name_list[j], folder_name + l[index] + "_img.png");
        else:
            print("file exists");
        output_file_csv.write(l[index] + "_img.png" + "\n");
        j += 1;
    i += 1;

#remove surplus
while (j < len(img_name_list)):
    os.remove(folder_name + img_name_list[j]);
    j += 1;

input_file.close();
output_file_csv.close();
print("folder used: " + folder_name);
print("file: " + output_filename + " written");