class myClass:

    __privatevar = 27;
    def __privMeth(self):
        print("im inside my myClass")
    def hello(self):
            print("private variable value: ", myClass.__privatevar)
foo = myClass()
foo.hello()
foo.__privMeth