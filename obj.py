class Sample:
    name = "..."
    add = ""

    def val(self, name, add):
        Sample.name = name
        self.add = add

    def info(self):
        print(self.name)
        print(self.add)


s = Sample()
s1 = Sample()
s.val("raja", "pune")
s.info()
print(s1.name + "...")

print(s.name)
