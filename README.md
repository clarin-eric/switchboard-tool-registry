[![CI](https://github.com/clarin-eric/switchboard-tool-registry/workflows/CI/badge.svg?branch=master)](https://github.com/clarin-eric/switchboard-tool-registry/actions?query=workflow%3ACI+branch%3Amaster)

# The Switchboard Tool Registry

This repository hosts the registry of all tools used by the Switchboard (https://switchboard.clarin.eu).

The repository has two important branches:
- `production` is hosting the tools used by the production instance (https://switchboard.clarin.eu).
- `master` is the development branch, with the tools used by testing and development versions of the Switchboard. The staging instance is https://beta-switchboard.clarin.eu.

## How to add a tool to the Switchboard
1. Take any of the json files describing a service from the `tools` directory in the repository and rename it and modify it to describe your tool. The json file name must be descriptive and unique, and should match the tool name in the json file. The `logo` entry in the file should contain your unique logo file name. See the [Tool description specification](https://github.com/clarin-eric/switchboard-doc/blob/master/documentation/ToolDescriptionSpec.md) for more detailed explanations on the meaning of each field.
1. Add the new json file to a new branch in your own fork of the repository, in the `tools` directory.
1. Add the logo file to the same branch, in the `logos` directory.
1. Make sure that the new json file is correct according to the json schema defined in the specification file: [spec-v1.schema.json](./schemas/spec-v1.schema.json). You can use one of the online schema validators (see https://json-schema.org/implementations.html#validators), or locally run the python script [validate-all-tools.py](./schemas/validate-all-tools.py) in the `schemas` directory.
1. Make sure your tool responds correctly when called by the Switchboard. See the [Tool Call API](https://github.com/clarin-eric/switchboard-doc/blob/master/documentation/ToolCallAPI.md) for more detailed explanations on how a tool is called and what parameters are being sent to the tool.
1. Create a pull request for merging your branch in the `master` branch of this repository.
1. After the pull request has been merged, check the availability of your tool in the development instance of the Switchboard: https://beta-switchboard.clarin.eu.
1. If you are satisfied with how the tool is integrated, create a new issue requesting the publication of your changes from `master` to `production`. Our team will do the merge and close the issue.

## Documentation links

The [Tool description specification](https://github.com/clarin-eric/switchboard-doc/blob/master/documentation/ToolDescriptionSpec.md) provides more information on the json description of the tools.

For details on how a tool is matched for a specific resource, see the [Tool Matching](https://github.com/clarin-eric/switchboard-doc/blob/master/documentation/ToolMatching.md) document.

For details on how a tool is actually invoked when selected by the user, see the [Tool Call API](https://github.com/clarin-eric/switchboard-doc/blob/master/documentation/ToolCallAPI.md) document.

