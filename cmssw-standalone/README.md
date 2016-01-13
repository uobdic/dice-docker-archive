# Usage of cmssw-standalone
To start the docker container in bash mode:
```
docker run -ti -v <path to your code>://home/cms/cmssw/src/<package path> kreczko/cmssw-standalone
# example (on Windows)
#docker run -ti -v //c/Users/kreczko/Documents/GitHub/NTupleProduction://home/cms/cmssw/src/BristolAnalysis/NTupleTools kreczko/cmssw-standalone
# Then inside the container
cd /home/cms/cmssw/src
cmsenv
# do your thing
```
