import random;
import string;
import sys;

def ft_char():
    letters = string.ascii_lowercase;
    return (letters[random.randint(0, 25)]);

def ft_word(min, max):
    word_len = random.randint(min, max);
    i = 0;
    word = "";
    while i < word_len:
        word += ft_char();
        i += 1;
    return (word);

def ft_pick(l, min, max):
    return (l[random.randint(min, max)]);

def ft_number(min, max):
    return (random.randint(min, max));

def ft_raise_line_short(i):
    raise NameError("Line data too short at line " + str(i + 1));

def ft_raise_cond_arg(i):
    raise NameError("Line doesn't have a right number of arguments at line " + str(i + 1));

def ft_raise_data_type(i):
    raise NameError("data type not handled at line " + str(i + 1));

def ft_raise_not_num(i):
    raise NameError("data condition should be numeric at line " + str(i + 1));

def ft_raise_cond_bigger(i):
    raise NameError("data condition 1 > data condition 2 at line " + str(i + 1));

def ft_raise_email_not_ok():
    raise NameError("email at line " + str(i + i) + "need to use a previous data");

def ft_check(line_list, result_list, i, data_index_save):
    if (len(line_list) < 2):
        ft_raise_line_short(i);
    data_type = line_list[1];
    if (data_type == "str"):
        if (len(line_list) == 4):
            if (not line_list[2].isnumeric() or not line_list[3].isnumeric()):
                ft_raise_not_num(i);
            if (int(line_list[2]) > int(line_list[3])):
                ft_raise_cond_bigger(i);
        elif (len(line_list) < 3):
            ft_raise_line_short(i);
        else:
            ft_raise_cond_arg(i);
    elif (data_type == "int"):
        if (len(line_list) == 4):
            if (not line_list[2].isnumeric() or not line_list[3].isnumeric()):
                ft_raise_not_num(i);
            if (int(line_list[2]) > int(line_list[3])):
                ft_raise_cond_bigger(i);
        elif (len(line_list) == 3):
            if (not line_list[2].isnumeric()):
                ft_raise_not_num(i);
        elif (len(line_list) < 3):
            ft_raise_line_short(i);
        else:
            ft_raise_cond_arg(i);
    elif (data_type == "email"):
        if (len(line_list) != 5):
            ft_raise_cond_arg(i);
        found = False;
        index = 0;
        for l in result_list:
            if (line_list[2] == l[0]):
                found = True;
                break;
            index += 1;
        l = [];
        l.append(index);
        l.append("");
        data_index_save.append(l);
        line_list.append(index);
        if (not found):
            ft_raise_email_not_ok();
    elif (data_type == "pick"):
        if (len(line_list) < 4):
            ft_raise_cond_arg(i);
        if (line_list[2] == "int"):
            j = 3;
            while (j < len(line_list)):
                if (not line_list[j].isnumeric()):
                    ft_raise_not_num(i);
                j += 1;
        elif (line_list[2] != "str"):
            ft_raise_data_type(i);
    else:
        ft_raise_data_type(i);

def ft_add_data(line_list, result_list, data_index_save, i):
    ft_check(line_list, result_list, i, data_index_save);
    result_list.append(line_list);

#check arguments
argc = len(sys.argv);
if (argc < 2):
    print("Error wrong nb of arguments || setup file not found");
    exit(1);
elif (argc >= 3):
    if (sys.argv[1] == sys.argv[2]):
        raise NameError("setup file and destination file can't be the same");

#read the setup of the csv data file
setup_file = open(sys.argv[1], "r");
result_list = [];
title_list = [];
data_index_save = [];
times = 1;
i = 0;
for line in setup_file:
    line_list = line.split();
    if (i == 0 and len(line_list) == 1):
        if (not line_list[0].isnumeric):
            ft_raise_not_num(i);
        times = int(line_list[0]);
    elif (len(line_list) > 0):
        ft_add_data(line_list, result_list, data_index_save, i);
        title_list.append(line_list[0]);
    i += 1;
setup_file.close();

print(result_list);
print(data_index_save);

#write to the output file
output_filename = "res.csv" if len(sys.argv) == 2 else sys.argv[2];
output_file = open(output_filename, "w");

#write the first line of csv (columns names)
i = 0;
for title in title_list:
    if (i != 0):
        output_file.write(", ");
    output_file.write(title);
    i += 1;
output_file.write("\n");

#write to output_file according to the setup result_list
i = 0;
data = "";
while i < times:
    k = 0
    for j in result_list:
        if (k != 0):
            output_file.write(", ");
        if (j[1] == "str"):
            data = ft_word(int(j[2]), int(j[3]));
            output_file.write(data);
        elif (j[1] == "int"):
            data = "";
            if (len(j) == 4):
                data = str(ft_number(int(j[2]), int(j[3])));
            elif (len(j) == 3):
                data = j[2];
            output_file.write(data);
        elif (j[1] == "email"):
            data = "";
            for l in data_index_save:
                if (l[0] == j[5]):
                    data += l[1];
                    break;
            data += "@";
            data += j[3];
            data += ".";
            data += j[4];
            output_file.write(data);
        elif (j[1] == "pick"):
            data = "";
            data = str(ft_pick(j, 3, len(j) - 1));
            output_file.write(data);
        for l in data_index_save:
            if (l[0] == k):
                l[1] = data;
                break;
        k += 1;
    output_file.write("\n");
    i += 1;
output_file.close();
print("file: " + output_filename + " written");