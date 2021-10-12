#!/usr/bin/env python3
import sys
from os import listdir
from os.path import isfile, join
import getopt
import json
import fastjsonschema


HELP = """Usage: validate-all-tools.py -s <SCHEMA_DEFINITION_FILE1> -t <TOOLS_DIRECTORY>"""
SCHEMA_DEFINITION_FILES = []
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
            global SCHEMA_DEFINITION_FILES
            SCHEMA_DEFINITION_FILES.append(arg)
        elif opt in ("-t"):
            global TOOLS_DIRECTORY
            TOOLS_DIRECTORY = arg

    if not SCHEMA_DEFINITION_FILES:
        print("Missing SCHEMA_DEFINITION_FILE argument", file=sys.stderr)
        print(HELP)
        sys.exit(2)
    if not TOOLS_DIRECTORY:
        print("Missing TOOLS_DIRECTORY argument", file=sys.stderr)
        print(HELP)
        sys.exit(2)


def validate_tools():
    validate_fns = []
    for schema in SCHEMA_DEFINITION_FILES:
        print("Reading schema", schema)
        try:
            with open(schema) as schema_file:
                json_data = json.loads(schema_file.read())
                validate = fastjsonschema.compile(json_data)
                validate_fns.append(validate)
        except json.JSONDecodeError as xc:
            print("! Error in json schema, file {}:\n\t{}\n".format(schema, xc))
            sys.exit(2)
        except fastjsonschema.JsonSchemaDefinitionException as xc:
            print("! Error in json schema, file {}:\n\t{}\n".format(schema, xc))
            sys.exit(2)

    tool_dir_entries = [join(TOOLS_DIRECTORY, f) for f in listdir(TOOLS_DIRECTORY)]
    tool_files = [f for f in tool_dir_entries if isfile(f)]

    failed = False
    tool_ids = set()
    for filepath in tool_files:
        print("Validating", filepath)
        failures = []
        with open(filepath) as file:
            try:
                json_data = json.loads(file.read())
            except json.JSONDecodeError as xc:
                print("! JSON decoding error: file {}\n\t{}".format(filepath, xc))
                sys.exit(2)
            tool_name = json_data.get("name")
            if json_data.get("id") is None:
                failures.append(f"Null ID in tool: {tool_name}")
            elif json_data.get("id") <= 0:
                failures.append(f"Negative or 0 ID in tool: {tool_name}")
            else:
                if json_data.get("id") in tool_ids:
                    failures.append(f"Duplicate ID in tool: {tool_name}")
                tool_ids.add(json_data.get("id"))
            for validate in validate_fns:
                try:
                    validate(json_data)
                except fastjsonschema.JsonSchemaException as xc:
                    failures.append(xc)
        if len(failures) == len(validate_fns):
            print("! Error in json file {}:\n".format(filepath))
            for i, xc in enumerate(failures):
                print("    --- failed to match schema {}: {}\n".format(i, xc))
            failed = True

    if failed:
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
