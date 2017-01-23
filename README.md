# queueDB

*A disk allocated queue that facilitates a database*

QueueDB is a small Python package that implements a DataQueue. A DataQueue is a special type of queue that can push or pop python values via read and write operations to a hidden file, much like a databas.

QueueDB supports the following data types:

* int
* char(length 1 string)
* bool
* long

The performance for the Queue is also optimized by using the `struct` module which deals with C-level data.
