#!/usr/bin/env bash
export USERID=`id -u`
export HOST=`hostname -f`
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd $DIR
docker-compose build

if [ $? -eq 0 ]; then
    echo "Image $USER/keras-gpu is now ready for use, run with"
    echo "export SRC=<path to folder containing your code>"
    echo "export DATA=/storage/$USER/<path to folder containing your data>"
    echo "nvidia-docker run -it --rm -v \${SRC}:/src/workspace -v \${DATA}:/data --net=host --env KERAS_BACKEND=tensorflow --name ${USER}_keras_gpu $USER/keras-gpu"
else
    echo ">> Something went wrong"
fi
popd
