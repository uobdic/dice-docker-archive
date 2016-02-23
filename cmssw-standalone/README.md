# cmssw-standalone
This container is quite big (~19 GB) when built, but has the advantage that
parts will work without network (unless you have to query the conditions DB)
or with poor network. If your network is good, I recommend the smaller image
[hepsw/cvmfs-cms](https://github.com/hepsw/docks/tree/master/cvmfs-cms).

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
