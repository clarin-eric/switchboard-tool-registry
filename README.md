# The Switchboard Tool Registry

This repository hosts the registry of all tools used by the Switchboard (https://switchboard.clarin.eu). 

The repository has two important branches: 
- `master` is the development branch, with the tools used by testing and development versions of the Switchboard. Hosts the tools used by the staging instance (https://beta-switchboard.clarin.eu)
- `production` is hosting the tools used by the production instance (https://switchboard.clarin.eu).

## How to add a tool to the Switchboard
1. Take any of the json files describing a service in the repository and modify it to describe your tool. The json file must be also renamed, as it is required to be descriptive and unique.
1. Add the new json file to a new branch in your own fork of the repository.
1. Create a pull request for merging your branch in the `master` branch of this repository.
1. After the pull request has been merged, check the availability of your tool in the development instance of the Switchboard: https://beta-switchboard.clarin.eu. 
1. If you are satisfied with how the tool is integrated, create a new issue requesting the publication of your changes from `master` to `production`. Our team will do the merge and close the issue.
