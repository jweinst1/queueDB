# queueDB

*A disk allocated queue that facilitates a database*

QueueDB is a small Python package that implements a DataQueue. A DataQueue is a special type of queue that can push or pop python values via read and write operations to a hidden file, much like a databas.

QueueDB supports the following data types:

* int
* char(length 1 string)
* bool
* long

The performance for the Queue is also optimized by using the `struct` module which deals with C-level data.

##Usage

To use queueDB, read the following API guidelines:

####`Constructor DataQueue(name)`:

This either initiates a new db file, or opens an existing one. The DB files are saved with the pattern `.{name}.oqueue`, to remain not visible.

####`__del__()`:

The QueueDB comes with a destructor method to automatically close the DB file upon garbage collection.

####`__len__()`:

You can use the `len()` builtin to count the number of items in the queue.

####Push:

This pushes some Python value to the back of the queue. You can push different types, like bools or ints with seperate methods.

####Pop:

Removes and returns the first item in the QueueDB, fails or raises error if empty.
