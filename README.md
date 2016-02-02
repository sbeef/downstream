# downstream
programs for managing samples that characterize watersheds

## background
This is a essentially a rewrite with an eye towards mild distribution of the samples.py script from my dirty-scripts repository.  This project grew out ArcPy scripts and an increasing desire to do as little as possible in Arc and try to move as much of the data management to Python, in part to take advantage of the language's list comprehension syntax.  The overall goal of the project is really a series of functions to facilitate more specialized and intricate scripting.

## structure
My overal vision for this is splitting the code into probably three parts: An implementation of the data strucutre (currently unwritten but refered to as 'dsample'), a series of functions using the getters and setters provided by dsample(what is 'downstream.py') and some sample scripts using the functions in downstream.py.  I want to split up downstream and dsample so that people can implement the actual sample data strucutre however they want, they just need to provide the functions that downstream calls.  Then can extend the datastructure as needed and write their own code to work with it.  dsample can be implemented in an object oriented way, it would just need functional wrappers.
