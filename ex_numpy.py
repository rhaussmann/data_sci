# In[1]:


import ex_pandas as pd
import ex_numpy as np
import ex_matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

# # Pandas is built on Numpy
# * Numpy is one of the fundamental packages for scientific computing in Python.
# * Before we dive into `pandas`, let's review `numpy`
#
#
# ## Numpy Arrays
# * Or NdArrays (n-dimensional array)
# * They are like lists in Python however they allow faster computation
#     1. They are stored as one contiguous block of memory, rather than being spread out across multiple locations like a list.
#     2. Each item in a numpy array is of the same data type (i.e. all integers, all floats, etc.), rather than a conglomerate of any number of data types (as a list is). We call this idea homogeneity, as opposed to the possible heterogeneity of Python lists.
#
#
# Just how much faster are they? Let's take the numbers from 0 to 1 million, and sum those numbers, timing it with both a list and a numpy array.
#

# In[2]:


numpy_array = np.arange(0, 1000000)
python_list = range(1000000)

# In[3]:


get_ipython().run_cell_magic('timeit', '', '# python built-ins\nsum(python_list)')

# In[4]:


get_ipython().run_cell_magic('timeit', '', '# numpy array with numpy sum\nnp.sum(numpy_array)')

# In[5]:


get_ipython().run_cell_magic('timeit', '',
                             '# but beware! combining a numpy array with standard library sum is slower than either one!\nsum(numpy_array)')

# ## Numpy NdArrays
#
# * have types
# * Each array is of one type

# In[6]:


ints = np.array(range(5))
floats = np.array(np.random.rand(5, ))
bools = np.array([True] * 5)
chars = np.array(list('ABCDE'))
strings = np.array(['A', 'BC', "DEF", "GHIJ", "KLMNO"])

# `numpy.dtype` describes how the bytes in the fixed-size block of memory corresponding to an array item should be interpreted. It describes the following aspects of the data:
#
# - `type` : integer, float, Python object, etc...
# - `itemsize` : number of bytes used to represent the data type
# - `byteorder` : little-endian or big-endian
# - `fields` : a dictionary of named fields defined for this data type,
#
# See https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.dtypes.html#attributes for a full list

# In[96]:


dt = ints.dtype
print('data type {}'.format(dt.type))
print('byte representation {}'.format(dt.itemsize))
print('is a numpy.int the same as a base int?', dt.type is int)
print('does a numpy.int inherit from base class int?', isinstance(dt.type, int))

# In[97]:


dt = bools.dtype
print('data type {}'.format(dt.type))
print('byte representation {}'.format(dt.itemsize))
print('is {} the same as base bool? {}'.format(dt.type, dt.type is bool))
print('does {} inherit from base class bool?', isinstance(dt.type, bool))

# In[98]:


print(ints.dtype)
print(floats.dtype)
print(bools.dtype)
print(chars.dtype)  # unicode string of max length 1
print(strings.dtype)  # unicode string of max length 5

# You can also specify the dtype directly, but this is rarely done in practice

# In[99]:


dt = np.dtype('i4')  # 32-bit signed integer
dt = np.dtype('f8')  # 64-bit floating-point number
dt = np.dtype('c16')  # 128-bit complex floating-point number
dt = np.dtype('a25')  # 25-length zero-terminated bytes
dt = np.dtype('U25')  # 25-character string

# ## Creating and using NdArrays

# In[11]:


ndarray_from_list = np.array([1, 2, 3, 4, 5])
ndarray_from_tuple = np.array((1, 2, 3, 4, 5), np.int32)

# In[12]:


print(ndarray_from_list.dtype)
print(ndarray_from_tuple.dtype)

# In[13]:


print(ndarray_from_list.shape)
print(ndarray_from_tuple.shape)

# ## Multi D

# In[14]:


nd_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
nd_arr

# ## Access elemens in an ndarray
# * Individual data
# * Slices of data

# In[15]:


nd_arr[1, 1]

# In[16]:


nd_arr[0:2, 0:2]

# In[17]:


nd_arr.shape

# In[18]:


nd_arr.sum()

# In[19]:


nd_arr.sum(axis=1)

# In[20]:


nd_arr.max()

# In[21]:


index_corresponding_to_max_value = nd_arr.argmax()
nd_arr.ravel()[index_corresponding_to_max_value]

# ## Broadcasting
# Broadcasting is your best friend and potentially your worst enemy.
# Do not broadcast blindly! This may cause unexpected results.
# Broadcasting and reshaping ndarrays will become paramount when we get to linear algebra.

# In[22]:


a = np.array([[10], [-10]])
b = np.array([[1, 2], [-1, -2]])

print(a)
print(b)
print(a + b)

# elements will "duplicate, expand, and fill up"
# to make the dimensions compatible for element-wise operations


# In[23]:


a = np.array([[10, 0, -10, 0], [-10, 0, -10, 0]])
b = np.array([[2, 2], [-1, 0]])

print(a)
print(b)

try:
    print(a + b)
except ValueError as e:
    print('ERROR: {}'.format(e))

# it's not clear how it should fill up in this case... so it can't/doesn't

