"""



"""

# /**
#  * @brief Takes 2 arrays, returns true if
#  *        their contents are the same;
#  *        otherwise false. 
#  * 
#  * @param {Array} xs 
#  * @param {Array} ys 
#  */
def areEquivalentArrays(xs, ys):
  return xs==ys and True


# /**
#  * @brief Takes an array, returns a new
#  *        array with no repeated values.
#  * 
#  * @param {Array} xs 
#  */
def unique_elements(xs):
  uniques = []
  for x in xs:
    if x not in uniques:
      uniques.append(x)
  return uniques

# /**
#  * @brief Takes an array, returns a new
#  *        array with no repeated values.
#  * 
#  * @param {Array} xs 
#  */
def unique_elements_simpler(xs):
  return list(set(xs))



# /**
#  * @brief Takes an array, returns a new
#  *        array with the same contents.
#  * 
#  * @param {Array} xs 
#  */
def clone(xs):
  return xs

