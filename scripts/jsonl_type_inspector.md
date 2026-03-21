# JSONL type inspector

I am examining the data schema for the EVE Online static data. The data is versioned by buildNumber, and comes as a compressed directory of JSONL files.

There is an implementation of this at
[First Effort](../src/eve_static_data/sde_type_sigs.py) but I believe it could use some refinement, especially in defining the output data structure.

Using python, write a set of functions that will read json data from a JSONL file, where each line of the file is a string that can be decoded by json.loads().

Assumptions:
- Each line is usually a json Object (dict), but this might not always be true. The best result would accept any valid json type, but if this is too difficult, then a dict as the top level type will meet current use cases.
- All of the lines in a single file can be expected to resolve to the the same data structure. e.g. one line is an int, and another is a list of strings, is not expected imput.

Requirements:
- the number of occurences for each type should be tracked. For example:
  - The total number of values (lines in the file)
  - if the item is a dict, then a count of the occurences of each key, by value type. 
  
  So if there are 30 lines in the jsonl, and each line decodes to a dict, and 20 of the dicts has a key "car" whose value type is a string, then the inspection function should return data that indicates out of 30 values, dict with key "car" showed up 20 times.

- TypedDicts describing the inspector output should be defined.

From this inspection data I want to be able to generate a TypedDict schema for a jsonl file.
If the file `cars.jsonl`,  has 30 lines that are a dict with the keys ```["car","city","mpg","address"]```, but the `"mpg"` key only shows up 25 times, then the schema will look like:
```python
class Cars(TypedDict):
    car:str
    city:str
    mpg:NotRequired[str]
    address:str

```
Note the class name is the file name without the suffix, with appropriate case.

If one of the fields is also a dict, then the schema would be:
```python
class Cars_Address(TypedDict):
    street:str
    zipcode:str

class Cars(TypedDict):
    car:str
    city:str
    mpg:NotRequired[str]
    address:Cars_Address
```
Note that the child schema name is a combination of the parent class, and field name.

The TypedDicts are ment to be included in markdown documentation, not used as actual code. But they shouls be valid python code. An option to generate a python file might be useful later.

write a function to generate a markdown documentation file that would describe the file names, line count (top level object count), and schemas of a directory of JSONL files. Start simple, and make it easy to add info later.

I also want to be able to compare the inspections of two different sets of data, calling out changes in the count and structur beween the two.

All code should be written to a new, single, file.