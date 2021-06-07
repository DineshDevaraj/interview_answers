# Simple hotel booking program
Write a program to automate the allocation / deallocation of rooms upon check in / check out at a property. Some hotels prefer allocating rooms from lower floors to higher floors. For example - Jaisalmer as higher floors become very hot. Some hotels prefer allocating rooms from higher floors first - For example Goa or other beach destinations due to better views on higher floors.
For the purpose of this assignment assume that all rooms are of the same type and all room stays are of equal duration of 1 day.

I would like to see how you initialize the hotel data structure, a check in function and a check out function.
The check in function should take in the number of rooms as an argument and return the room numbers of the allocated rooms as a List

The check out function should take in the room numbers to check out and vacate the rooms.

A room that has been checked in once should not be allocated again until it is checked out.
Keep your design scalable such that you can demonstrate the top to bottom and bottom to top allocation mechanisms (one hotel will have a unique allocation mechanism) but can easily support other mechanisms in the future. Do support your code with appropriate unit tests.
