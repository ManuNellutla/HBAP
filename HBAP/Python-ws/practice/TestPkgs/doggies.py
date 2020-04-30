from dog import Dog


boyDog = Dog("Mesa", 2004, 5, 15, "WOOOF")
girlDog = Dog("Sequoia",2004, 5, 6, "barkbark")
print(boyDog.speak())
print(girlDog.speak())
print(boyDog.getAge())
print(girlDog.getAge())
print(boyDog.getName())
print(girlDog.getName())
boyDog.changeBark("woofywoofy")
print(boyDog.speak())
