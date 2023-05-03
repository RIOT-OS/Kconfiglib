FOO.val = True
BAR.val = True
# Expect the following to fail since BAR is True and depends on FOO.
FOO.val = False
