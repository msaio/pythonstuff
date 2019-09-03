#######################################################
# class First(object):
#     def __init__(self):
#         print "first"

# class Second(First):
#     def __init__(self):
#         print "second"

# class Third(First):
#     def __init__(self):
#         print "third"

# class Fourth(Second, Third):
#     def __init__(self):
#         super(Fourth, self).__init__()
#         print "that's it"

# f4 = Fourth()
# Output:
# second
# that's it

#######################################################
class First(object):
  def __init__(self):
    print "First(): entering"
    super(First, self).__init__()
    print "First(): exiting"

class Second(object):
  def __init__(self):
    print "Second(): entering"
    super(Second, self).__init__()
    print "Second(): exiting"

class Third(First, Second):
  def __init__(self):
    print "Third(): entering"
    super(Third, self).__init__()
    print "Third(): exiting"

third = Third()

# Output:
# Third(): entering
# First(): entering
# Second(): entering
# Second(): exiting
# First(): exiting
# Third(): exiting