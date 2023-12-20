# 2json 
[yaml , toml] to json

## About

Nowadays there 3 mainstream human-readable, structurized, and **non-tag-basic** format :

- ``` JSON ```
- ``` YAML ```
- ``` TOML ```

``` JSON ``` is the most machine friendly and the most grammar-strict,
and the earliest one.
It lead to some subtle differences in development ecosystem.
*E.g.* for python3 :

-  ``` json ```  is in standard library set and completly support *json* format file
- *yaml* was supported by 3-party libraries, the "most offical" one is PyYAML
-  ``` tomllib ```  became a part of python standard library since *3.12*,
	but no dump function in it.

After all, it is recommanded always send data to process in  ``` JSON ```  format.
And if they were stored in  ``` YAML ```   ``` TOML ```  for human friendly usage,
convert them.

## Some details

The main function of [2json](.) is converting:

> [yaml , toml] to json

But infact [2json](.) can transform each one to each other or itself.

Without any option to specifiy the input format,
[2json](.) will try ``` JSON ``` 1stly, ``` TOML ``` 2ndly,
and ``` YAML ``` at last.
Because it is easily to make ``` YAML ``` to treat the whole document
or a large block as a string, even if they are in other formats.
