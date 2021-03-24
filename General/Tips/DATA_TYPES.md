## Status - Unfinished

# Main Data Types
> Integers <br>
> Floating Point Numbers (Floats) <br>
> Booleans <br>
> Characters <br>
> Strings <br>

# Integers
> 32-Bit Integers - ```int``` in Cpp, Java, and Python; integer values from −2147483648 to 2147483648 [-2\*10^9, 2
> *10^9]. <br>
> 64-Bit Integers - ```long long``` in Cpp, ```long``` in Java, and ```int``` in Python; these are less likely to overflow since they have a range from −9223372036854775808 to 9223372036854775808 [-9\*10^18, 9*\10^18]. <br>
> Sometimes USACO problems will have warnings that recommend the competitor to use a 64-bit integer to account for larger numbers.<br>
> It is recommended to use 64-bit integers everywhere since they can be used everywhere. However, be mindful of runtime and memory limits.
> Note that in Java, you must cast longs into ints when accessing values from arrays.

# Floating Point Numbers
> Used to store decimal numbers. <br>
> The binary system used by computers can only store decimals to a certain precision, causing floating point numbers, or floats, to not be exact.<br>
> Thus, it is generally a bad idea to use equality operators to check if two floats are the same value.<br>
> In some contest, these inconsistencies are accomodated for by checking whether your float and the actual answer's absolute or relative difference is less than some constant, typically 10^-9.<br>
> The absolute difference between an output x and an answer y is |x-y|.<br>
> The relative difference between an output x and an answer y is |x-y|/|y|.<br>
> In USACO, answers will typically be requested to be rounded to the nearest integer if the unrounded answer is a float.

# Booleans
> 2 possible states: True or False.<br>
> Typically used to check if a process is complete or check the status of a condition.<br>
> Arrays of booleans can be used to simulate movement (by marking position as True and everything else False) or to check which components of an algorithm are complete.

# Characters
> A single character, such as 'a', 'b', or 'c'.<br>
> These values are returned when accessing an index within a string.<br>
> Characters are usually represented in ASCII, which assigns each character to a corresponding integer.<br>
> ASCII allows one to do arithmetic using characters: 'f'-'a' = 5.<br>
> Characters are 16-bits in Java and 8-bits in Cpp.<br>
> Characters are treated as strings in Python. They can be converted into ASCII numbers by using the ```ord()``` function: ord('A') returns 65.<br>
> The link below is a useful ASCII table:<br>
> <a href="http://www.asciitable.com/">http://www.asciitable.com/</a>

# Strings
> Stored as arrays of characters.<br>
> Strings use ArrayLists to dynamically change depending on how a user changes a string.<br>
> Most functions or methods that work on lists, such as ```index()``` in Python work on strings.<br>
> ```substring()``` in Java returns a spliced string based off either 1 or 2 parameters (if there are 2 parameters, they are inclusive and exclusive, respectfully).<br>
> ```charAt()``` in Java finds the value at an index (passed as a parameter) of a string, much like how ```string[]``` would work in Python.<br>
> A loop can be used to access each character of an unknown string.
