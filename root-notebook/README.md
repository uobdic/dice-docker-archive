# ROOT Notebook

The [ROOT](http://root.cern.ch) Notebook container is based on the [Jupyter Data Science stack](https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook). It adds ROOT, root_pandas, rootpy & scikit-learn. Currently only the Python2 kernel is configured (no Python3 or cling support).

You can start it with
```shell
docker run -d -p 8888:8888 kreczko/root-notebook
```
On Linux systems this will provide the Jupyter notebook on `localhost:8888` and on OS X and Windows the notebook can be reached via the docker machine IP:
```shell
docker-machine ip <machine name>
```