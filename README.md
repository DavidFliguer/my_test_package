This is a generic example of how a python package might look

Specifically it has the proper configuration to include files that are not code

This repository as it is, can be zipped to my_test_package.zip and then in another machine install it through pip install

When installing through pip install it can be verified that in the site-packages folder, the files that are not code (But used in code) are included

Once installed, it can be used like the following:

from my_test_package.MyClass import MyClass

mc = MyClass()

mc.do_work()
