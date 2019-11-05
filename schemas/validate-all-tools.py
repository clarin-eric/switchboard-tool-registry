#!/usr/bin/env python3
import sys
from os import listdir
from os.path import isfile, join
import getopt
import json
import fastjsonschema


HELP = """Usage: validate-all-tools.py -s <SCHEMA_DEFINITION_FILE> -t <TOOLS_DIRECTORY>"""
SCHEMA_DEFINITION_FILE = None
TOOLS_DIRECTORY = None


def main(argv):
    load_arguments(argv)
    validate_tools()

def load_arguments(argv):
    try:
        opts, args = getopt.getopt(argv,"hs:t:")
    except getopt.GetoptError:
        print(HELP)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(HELP)
            sys.exit()
        elif opt in ("-s"):
            global SCHEMA_DEFINITION_FILE
            SCHEMA_DEFINITION_FILE = arg
        elif opt in ("-t"):
            global TOOLS_DIRECTORY
            TOOLS_DIRECTORY = arg

    if not SCHEMA_DEFINITION_FILE:
        print("Missing SCHEMA_DEFINITION_FILE argument", file=sys.stderr)
        print(HELP)
        sys.exit(2)
    if not TOOLS_DIRECTORY:
        print("Missing TOOLS_DIRECTORY argument", file=sys.stderr)
        print(HELP)
        sys.exit(2)


def validate_tools():
    print("Reading ", SCHEMA_DEFINITION_FILE)
    try :
        with open(SCHEMA_DEFINITION_FILE) as schema_file:
            json_data = json.loads(schema_file.read())
            validate = fastjsonschema.compile(json_data)
    except fastjsonschema.JsonSchemaDefinitionException as xc:
        print("! Error in json schema, file {}:\n\t{}\n".format(SCHEMA_DEFINITION_FILE, xc))
        sys.exit(2)

    tool_dir_entries = [join(TOOLS_DIRECTORY, f) for f in listdir(TOOLS_DIRECTORY)]
    tool_files = [f for f in tool_dir_entries if isfile(f)]

    failed = False
    for filepath in tool_files:
        print("Validating", filepath)
        with open(filepath) as file:
            json_data = json.loads(file.read())
            try :
                validate(json_data)
            except fastjsonschema.JsonSchemaException as xc:
                print("! Error in json file {}:\n\t{}\n".format(filepath, xc))
                failed = True

    if failed:
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
