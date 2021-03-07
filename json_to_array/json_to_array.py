import sys;

if (len(sys.argv) != 2):
    print("nb arg incorrect");
    exit(1);
file = open(sys.argv[1]);
out_str = "";
curlb = 0;
i = 0;
for line in file:
    i = 0;
    while (i < len(line)):
        if (line[i] == '{'):
            curlb += 1;
            if (curlb > 1):
                if (curlb == 2):
                    out_str += "\t";
                out_str += line[i];
        elif (line[i] == '}'):
            curlb -= 1;
            if (curlb > 0):
                out_str += line[i];
                if (curlb == 1):
                    out_str += ',\n';
        else:
            if (curlb > 1):
                out_str += line[i];
        i += 1;

if (curlb != 0):
    print("wrong curly brackets");
    exit(1);

output_filename = "res.js"
outfile = open(output_filename, "w");
outfile.write("const array = [\n");
outfile.write(out_str);
outfile.write("];\nexport default array;");
file.close();
outfile.close();
print("file: " + output_filename + " written");