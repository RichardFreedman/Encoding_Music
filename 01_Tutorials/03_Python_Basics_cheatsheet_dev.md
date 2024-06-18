# Python Basics

## Data Types

* **Integer**: whole number

  ```python
  x = 10
  ```

* **Float**: decimal number
  
  ```python
  x = 2.25
  ```

* **String**: text

  ```python
  text1 = "Encoding Music"
  text2 = 'Music 255'
  ```

* **Boolean**: `True` or `False`
  
  ```python
  b = True
  ```

## Collections

* **List**: ordered sequence of data of any type, including mismatched data
  
  ```python
  list1 = ["Blues", "Gospel", "Country"]
  list2 = [3, "Dog", False]
  ```

  * Access by index: 
  
    ```python
    print(list1[0])   # "Blues"
    print(list2[2])   # False
    ```

  * Change list item:

    ```python
    list1[1] = "Pop"
    ```
    
    Now `list1` is `["Blues", "Pop", "Country"]`

* **Tuple**: ordered sequence of data of any type, including mismatched data, *that cannot be changed*

  ```python3
  tuple1 = ("Blues", "Gospel", "Country")
  tuple2 = (3, "Dog", False)
  ```

  * Access by index: 
    
    ```python
    tuple1[0]   # "Blues"
    tuple2[2]   # False
    ```

  * *Hint*: Use a tuple if the data in a list should *never* be changed. Storing a list as a tuple can prevent you from accidentally modifying a very important list. However, lists and tuples are nearly identical.
* **Dictionary**: unordered sequence of **key : value** pairs, where the **values** can be of any data type. Usually keys are strings.
  ```python
  dict1 = {
    "artist" : "McCartney, Paul",
    "title" : "Yesterday"
    }
  dict2 = {"album" : "Abbey Road", "songs" : 17}
  ```

## Checking Data Types

```python
type(item)  # Outputs type of `item`
```

## Output

```python
print(my_variable)
```

Note you can also output a variable in Jupyter by writing it as the last line in a cell:

```python
my_variable
```

## Operations on Data Types

### Math

The same operations work on both integers and floats.

```python
a = 5
b = 2.5
c = 6

# Operator      # Output

# Addition
print(a + b)    # 7.5
# Subtraction
print(a - b)    # 2.5
# Multiplication
print(a * b)    # 12.5
# Division
print(c / b)    # 2.4
# Remainder
print(c % b)    # 1
# Floor Division
print(c // b)   # 2.0
```

### Comparison

You can compare two items of any data type, as long as they are the same data type.

```python

# Operator      # Output

# Equality
print(a == b)   # False
# Not Equals
print(a != b)   # True
# Less Than
print(a < b)    # False
# Less Than or Equal To
print(a <= b)   # False
# Greater Than
print(a > b)    # True
# Greater Than or Equal To
print(a >= b)   # True
```

### Strings

A small selection of important built-in methods for strings. Note none of these methods change the variable.

```python
text1 = 'encoding music'
text2 = '--Music 255--'

# Method                        # Output

# Title Case
print(text1.title())            # 'Encoding Music'
# Upper Case
print(text1.upper())            # 'ENCODING MUSIC'
# Lower Case
print(text2.lower())            # '--music 255--'
# Replace
print(text1.replace(" ", "_"))  # "encoding_music"
# Find
print(text1.find("i"))          # 5
# Strip
print(text2.strip("-"))         # 'Music 255'
# Split
print(text1.split(" "))         # ['encoding', 'music']
```

Find more methods at [W3Schools](https://www.w3schools.com/python/python_strings_methods.asp).

### Lists

