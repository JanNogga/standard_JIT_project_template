# standard_JIT_project_template
A template for standard projects.

## Setup

1. Clone this repository.
2. Build the docker image.
```console
./build.sh
```
3. Run a container.
```console
./run.sh
```
4. (Optional) For quick prototyping setup jupyter notebook in the container.
```console
jupyter notebook password
```
```console
cd /repos
```
```console
jupyter notebook --no-browser --ip 0.0.0.0 --port 9999 &
```
Then connect to the machine hosting the container, for example using:
```console
ssh -L 9999:localhost:9999 -J USER@login-stud/staff.informatik.uni-bonn.de USER@cudaX
```
The notebook is now available locally at [http://localhost:9999/](http://localhost:9999/).
