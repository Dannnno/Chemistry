import sysimport subprocessimport jsonusage = """USAGE:    >> python to_blockdiag.py output_file [, input_file]"""if len(sys.argv) not in [2, 3]:    raise Exception(usage)directory = "C:/Users/Dan/Desktop/Programming/Python/BlockDiag/"output_file_name = directory + sys.argv[1]image_file_name, _, _ = output_file_name.partition('.')image_file_name += ".png"with open(sys.argv[2], "r") as json_file:    atree = json.load(json_file)orig = sys.stdoutwith open(output_file_name, "w") as output_file:    sys.stdout = output_file    def print_blockdiag(tree, parent=None):        if not parent:            print('blockdiag { orientation = landscape')        if not isinstance(tree, basestring):            for key in tree:                if parent:                    print('   {} -> {};'.format(parent, key))                try:                    print_blockdiag(tree[key], key)                except TypeError:                    print('   {} -> {};'.format(parent, key))            if not parent: print('}')        else:            if tree == "":                tree = "None"            print('   {} -> {};'.format(parent, tree))    print_blockdiag(atree)sys.stdout = origtry:    subprocess.check_call(["blockdiag", output_file_name])except subprocess.CalledProcessError as e:    print e    print "Error with blockdiag command. Exiting"else:    try:        subprocess.check_call([image_file_name], shell=True)    except subprocess.CalledProcessError as e:        print e        print "Error with opening <{}>. Exiting".format(image_file_name)ledProcessError as e:

    print e

    print "Error with blockdiag command. Exiting"

else:

    try:

        subprocess.check_call([image_file_name], shell=True)

    except subprocess.CalledProcessError as e:

        print e

        print "Error with opening <{}>. Exiting".format(image_file_name)






Ò
e_name)






Ò
