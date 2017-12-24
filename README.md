# Forker
Simple Python script that helps to run tasks parallel using the fork system call.

# Usage
./forker.py workers/simple.py

# Motivation
Very often i have tasks todo which could be run parallel e.g. ping some hosts. This script will do the work. You have only to define a worklist and a function that should be worked on.
