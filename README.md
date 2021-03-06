# pylogic-module
[![Build Status](https://www.travis-ci.org/fran-bravo/pylogic-module.svg?branch=master)](https://www.travis-ci.org/fran-bravo/pylogic-module)
[![codecov](https://codecov.io/gh/fran-bravo/pylogic-module/branch/master/graph/badge.svg)](https://codecov.io/gh/fran-bravo/pylogic-module)

Python module for logical programming

## 

It provides functionalities for developing accordingly to the logical programming paradigm such as:
  * Cases
  * Knowledge Bases
  * Predicates (WIP)
  
## Elements

### Case

Defines a simple element consisting of a selector to identify the relation of data it represents as well as a tuple to store the data of the realtion itself.

#### Example

##### Creation

You can create a Case object directly by using the Case class constructor like this:

```python
from pylogic.case import Case

case = Case('parent', 'Bob', 'John')
```

Selector|Data
--------|--------
  parent|('Bob','John')

Or, due to the fact that Cases work associated to a Knowledge Base, you can use the `@case(knowledge_base)` decorator:

```python
from pylogic.decorators import case
from pylogic.knowledge_base import KnowledgeBase

base = KnowledgeBase(2)

@case(base)
def parent(father, son):
  pass
```

_Note: you can also add functionality for the parent cases instead of just using pass._

##### Tally

Once you have your case object, you can tally it against a value:

```python
case.tally('Bob') # ('Bob', 'John')
```

Or even against a tuple of values:

```python
case.tally(('Bob', 'John')) # True
```

### Knowledge Base

A knowledge base consists of Strains of case objects and an Arity. A Strain groups case objects based on their selector, while the Arity defines the amount of elements stored in the case tuple supported by the Knowledge Base.

|Knowledge Base|Strains|Cases
|--------------|-------|-------
|  family_tree |parent |('Bob','John')
|              |       |('Bob','Fred')
|              |brothers|('Fred','John')
|              |        |('John','Fred')

#### Example

##### Creation

```python
from pylogic.knowledge_base import KnowledgeBase
from pylogic.decorators import case

family_tree = KnowledegBase(2)

@case(family_tree)
def parent(father, son):
  pass

@case(family_tree)
def brothers(brother_one, brother_two):
  pass

parent('Bob', 'John')
parent('Bob', 'Fred')

brothers('John', 'Fred')
brothers('Fred', 'John')
```

##### Tally

```python
from pylogic.functions import _

family_tree.tally("parent", "Bob", _) # [('Bob', 'John'),('Bob', 'Fred')]
```

_We recommend the usage of _ from the functions file for easier tallies (functions module just defines an alias for None in a variable named _ )_

### Predicate (WIP)

Predicates aim to add extra filtering options in conjunction with Knowledge Bases, allowing for more powerful tallies.

#### Example

##### Using lambdas

```python
predicate = Predicate('brothers') # The predicate will work on the brothers strain
predicate.add_base(family_tree)
predicate.add_rule(lambda tup: tup[0].startswith('F')) # We add a rule in the predicate to check if the parent name starts with B

predicate.tally(_, _) # [('Fred', 'Bob')]
```

###### Using def

```python
predicate = Predicate('brothers')
predicate.add_base(family_tree)

def not_bob(tup):
  return (tup[0] != 'Bob') and (tup[1] != 'Bob')
  
predicate.add_rule(not_bob)

predicate.tally(_, _) # []
```
