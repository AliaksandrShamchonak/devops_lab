# psstats

## Description
Script Pull Request statistics (pr-stats) is getting statistics from GitHub:
 
## Running
 
`python prstats.py [options]` 

## Options

usage: prstats.py [-h] [-v] [-o OWNER] [-r REPO] [-a] [-cm] [-br] [-pu] [-pc]
                  [-wd] -un UNAME -ut UTOKEN

Optional arguments:
  -h, --help        show this help message and exit
  -v, --version     Prints the version of program
  -o, --owner       Owner of repository
  -r, --repo        Name of repository
  -a, --all         Show all parameters
  -cm, --commit     Show the number of commits, date and names for repository
  -br, --branches   Show number of branches, names and protections
  -pu, --pull       Show number of pull requests and create date
  -pc, --pullclose  Show pull requests is closed
  -wd, --weekday    Day of week pull request created
  -un, --uname      User name for authorization github
  -ut, --utoken     User token for authorization github
