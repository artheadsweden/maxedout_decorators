from Add_to import add_to_instance, add_to_class


class AClass:
    def __init__(self, name):
        self.name = name



def main():

    a = AClass("Lisa")

    @add_to_instance(a)
    def reverse(self):
        return self.name[::-1]

    @add_to_class(AClass)
    def get_vowels(self):
        return "".join(c for c in self.name if c in "aeiou")

    print(a.reverse())
    a1 = AClass("Bertha")
    print(a1.get_vowels())
    #print(a1.reverse())
    print(a.get_vowels())

if __name__ == '__main__':
    main()
