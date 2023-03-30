# standard_JIT_project_template
A template for standard projects.

## Setup

1. Clone this repository.
```console
git clone https://github.com/JanNogga/standard_JIT_project_template.git
```
2. Build the docker image.
```console
cd standard_JIT_project_template/docker && chmod +x build.sh && chmod +x run.sh && ./build.sh
```
3. Run a container.
```console
./run.sh
```
4. In the container, switch to this repository.
```console
cd module_name/
```
5. Finally run the dummy code. The cuda kernel defined in *lib/cuda* is compiled just-in-time.
```console
run.py
```
