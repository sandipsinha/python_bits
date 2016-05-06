
class Foo:
    me = "foo"
 
class Bar:
    me = "bar"
    def get_me(self):
        return self.me
 
Foo.get_me = Bar.get_me
x = Foo()
 
print x.get_me()
