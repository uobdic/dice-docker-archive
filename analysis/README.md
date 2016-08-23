HEP analysis baseline container with gcc 4.8, cmake, ROOT 6, Python 2.7, rootpy, RooUnfold, and pandas based on Centos 6.

To be run as:
```
docker run -t -i -e DISPLAY=$DISPLAY kreczko/analysis
source activate analysis
<do your thing>
```