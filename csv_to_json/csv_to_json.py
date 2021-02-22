import sys

def ft_remove_last_newline(data):
    try:
        index = data.index('\n');
        if (index == len(data) - 1):
            data = data[:index];
        return (data);
    except:
        return (data);

def ft_raise_argc():
    raise NameError("Wrong nb of arguments");

def ft_raise_lines():
    raise NameError("files have different nb of lines");

#check arguments
argc = len(sys.argv);
if (argc < 2):
    ft_raise_argc();

#save the nb of lines of the first file
nb_of_lines_save = 0;
input_file = open(sys.argv[1], "r");
for f in input_file:
    nb_of_lines_save += 1;
input_file.close();

#compare the number of lines of each next file with the number of the first file
if (argc > 2):
    argv = sys.argv[2:];
    nb_of_lines = 0;
    for f in argv:
        input_file = open(f, "r");
        for lines in input_file:
            nb_of_lines += 1;
        input_file.close();
        if (nb_of_lines != nb_of_lines_save):
            ft_raise_lines();
        nb_of_lines = 0;

#open each csv files and store them in a list
files = [];
argv = sys.argv[1:];
for i in argv:
    files.append(open(i, "r"));

#open the file to write to
output_filename = "res.js";
output_file = open(output_filename, "w");
output_file.write("const users = [");

#read line by line each csv files and write each lines after a split in output_file except the first line of each csv file which are the titles of each columns
i = 0;
title_list = [];
while i < nb_of_lines_save:
    j = 0;
    if (i != 0):
        output_file.write("{\n");
    for f in files:
        if (i == 0):
            l = f.readline().split(", ");
            l2 = [];
            for m in l:
                l2.append(ft_remove_last_newline(m));
            title_list.append(l2);
        else:
            l = f.readline().split(", ");
            l2 = [];
            for m in l:
                l2.append(ft_remove_last_newline(m));
            k = 0;
            if (j != 0):
                output_file.write(",\n");
            try:
                index = argv[j].index(".csv");
                output_file.write("\t" + argv[j][:index] + ": {");
            except:
                output_file.write("\t" + argv[j] + ": {");
            while (k < len(title_list[j])):
                if (k != 0):
                    output_file.write(", ");
                output_file.write(title_list[j][k] + ":\"" + l2[k] + "\"");
                k += 1;
            output_file.write("}");
            if (j == argc - 2):
                output_file.write("\n");
        j += 1;
    if (i != 0 and i != nb_of_lines_save - 1):
        output_file.write("},\n");
    elif (i == nb_of_lines_save - 1):
        output_file.write("}");
    i += 1;

for f in files:
    f.close();
output_file.write("]\nmodule.exports = users;");
output_file.close();
print("file: " + output_filename + " written");