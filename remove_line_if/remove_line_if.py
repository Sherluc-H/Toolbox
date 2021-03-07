import sys;

if (len(sys.argv) != 3):
    print("nb arg incorrect");
    exit(1);
file = open(sys.argv[1]);
out_str = "";
for line in file:
	if (line.find(sys.argv[2]) != -1):
		pass;
	else:
		out_str += line;

output_filename = "res.js";
outfile = open(output_filename, "w");
outfile.write(out_str);
file.close();
outfile.close();
print("file: " + output_filename + " written");