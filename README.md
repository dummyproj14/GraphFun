README.md
#playersMindset

##I/ Introduction

This program aimed at solving automatically a graph-like problem of finding the maximum datapoints connected with each others in an unordered ensemble.

The program has been written in python3 and tested with **python3.10** (latest available version of the interpreter).
This source code is only intented at solving a coding test given by SecondMind (UK registered company).
Any damage resulting from the execution of the given program is at the own responsability of the user.
The author decline any *responsability* in any misuse of the given code/program.

For any additional question or concern, please email <bjorn.goriatcheff@gmail.com>.

##II/ Description

This program takes a **text file** (.txt extension or heading) as input representing a list of *players* (entities) and their associated list of visible players.
The program understands those entries as a list of state and their associated list of accessible states : this makes the input space *viewable as an oriented graph*.

The goal of the program is to find the length of the longest subset of *players* (or states) that are connected with each others. There must be a symmetrical link between two *players* (or states) for them to be considered as connected.

This program uses a technic called **adjacency matrix** to represent the input in a simple data structure that can be processed efficiently. 


The complexity is ***O(mn)*** as in the worst case the program will go through all the states, **m states at most** and *for each state* it will go through its associated list of accessible states, **n states at most**.

**Note** : the early stopping condition based either on the unvisited list of nodes or the length of the longest chain *usually* prevents from reaching such scenario.



##II/ Setup

####1) Minimum required configuration (no container)

- An environment with **python3.6** and **pip21.2.3** installed (WIN/MACOSX/UNIX), *the python binaries are not provided for safety reasons*.
- A working *Internet access* to *download* any listed requirements such as numpy, wheel, setuptools.
- A single processor of 1.5GHz and a memory of 4Gb (8Gb would be preferable).


####2) Standalone installation 

#####UNIX-like

1. build the binaries from the provided gzip archive

>```bash$ pip install dist/playersMindset-0.0.1b0.tar.gz```

2. execute the program using command line interface

>```bash$ python -m playersMindset.manager <path_to_input_textfile>```

3. (Optional) it is also possible to execute the program from a python interpreter

>```bash$ python```

>```>>> import playersMind```

>```>>> fpath = "path/to/input/file.txt"```

>```>>> playersMind.cmd(fpath)```



#####WINDOWS 10

Note : CMD can be either cmd.exe or powershell (both are spported)

1. build the binaries from the provided wheel/gzip archive

>```CMD$ pip install dist/playersMindset-0.0.1b0.tar.gz```

2. execute the program using command line interface

>```CMD$ python -m playersMindset.cmd <path_to_input_textfile>```

---

####3) Containerized Installation (NOT WORKING)

Pre-requisite : a working docker environment

```bash$ docker build .```

```bash$ docker run 'image-name'```

```bash$ docker ls | grep 'image-name'```

```bash$ docker cp <path_to_input> 'image-name':/app/data```

```bash$ docker logs 'instance-name'```


##III/ Algorithm

Here the summary of the most important steps of the algorithm :
 
1. The *input text* is read/parsed and transformed into a **adjacency matrix**
2. The adjancency matrix is restricted to its *symmetrical connexions* (A->B and B->A) which results in a **triangular matrix**
3. The triangular matrix is processed as a list of **non-zero indices** which makes it able to process very **large sparse matrices**.
4. The list of non-zero indices is sorted to take first the indices that contains the most connexions
5. The chains of states are then built sequentially based on the list of accessible states and their own list of accessible states and so on
6. This chains are **merged periodically** to consolidate progressively the output
7. Once a chain reaches the **maximum length** (all players/states) have been visited or if **every states have been visited**, the algorithm **stops** (terminal condition).

The algorithm is *proven to finish* as the list of unvisited states/nodes is reducing progressively at each iteration until it reaches 0.

**Commentary** : An additional logic has been implemented to handle specific cases related to high dimensional matrices. 2 main subcases were identified : sparse and dense matrices which necessit a specific implementation. This logic is still in developpment. 

It is recommended to **avoid inputs greater than pow(10,8) entries (roughly 100M entries)** in order to reach a **finite computation time**. 

In summary, the supported ***matrix size should not exceed a shape of (10000, 10000)***.



