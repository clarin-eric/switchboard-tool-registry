# The Switchboard Tool Registry

This repository hosts the registry of all tools used by the Switchboard (https://switchboard.clarin.eu).

The repository has two important branches:
- `production` is hosting the tools used by the production instance (https://switchboard.clarin.eu).
- `master` is the development branch, with the tools used by testing and development versions of the Switchboard. The staging instance is https://beta-switchboard.clarin.eu.

## How to add a tool to the Switchboard
1. Take any of the directory with json file describing a service in the repository and modify it to describe your tool. The directory and json file must be both renamed, and the name must be descriptive and unique.
1. Make sure that the new json file is correct according to the json schema defined in the specification file: [spec-v1.schema.json](./spec-v1.schema.json). You can use one of the online schema validators (see https://json-schema.org/implementations.html#validators).
1. Add the new directory with the json file to a new branch in your own fork of the repository.
1. Create a pull request for merging your branch in the `master` branch of this repository.
1. After the pull request has been merged, check the availability of your tool in the development instance of the Switchboard: https://beta-switchboard.clarin.eu.
1. If you are satisfied with how the tool is integrated, create a new issue requesting the publication of your changes from `master` to `production`. Our team will do the merge and close the issue.
