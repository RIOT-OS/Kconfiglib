TEST_TRISTATE.val = False
assert TEST_TRISTATE.val == False

# Tristates will default to False if nothing sets it to True
# This means we cannot read None...
TEST_TRISTATE.val = None
assert TEST_TRISTATE.val == False

TEST_TRISTATE.val = True
assert TEST_TRISTATE.val == True
