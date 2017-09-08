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

#### Example

```python
from pylogic.knowledge_base import KnowledgeBase
from pylogic.decorators import case

base = KnowledegBase(2)

@case(base)
def parent(father, son):
  pass

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

#### Example

```python
from pylogic.knowledge_base import KnowledgeBase
from pylogic.decorators import case

base = KnowledegBase(2)

@case(base)
def parent(father, son):
  pass
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
|       ˪      |   ˪   |('Bob','Fred')
|       ˪      |brothers|('Fred','John')
|       ˪      |    ˪   |('John','Fred')

#### Example

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

brother('John', 'Fred')
brother('Fred', 'John')
```
