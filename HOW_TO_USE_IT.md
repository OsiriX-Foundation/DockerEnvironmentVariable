### variables mandatory with default value

`ENV name=default_value`

### Variable mandatory without default value

`ENV name=`

### Variable optional

`ENV name=""`

### Both
```
ENV name1=default_value \
     name2="" \
     name3= \
     name4=another_default_value
 ```
