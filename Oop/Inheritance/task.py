while True:

    print("\n------------------- Menu---------------------")
    print(" 1. Single Inheritance \n 2. Multilevel Inheritance \n 3. Heirarchical Inheritance \n 4. Multiple Inheritance")

    ch=int(input(" \nenter your choice : "))

    match ch:
        case 1:
            print(" Single Inheritance ")
            class Animal:
                def __init__(self):
                    print("\n Animals makes sound ")

            class Dog(Animal):
                def __init__(self):
                    super().__init__()
                    print(" Dog barks !!!")
                

            d=Dog()
            print("---------------------------------------------------------------------------------------------------------")
            


        case 2:
            class School:
                def input(self,name,place):
                    self.name=name
                    self.place=place

                def show_school(self):
                    print("\n name of school = ",self.name)
                    print(" location of school = ",self.place)

            class Classroom(School):
                def show_classroom(self,count):
                    self.count=count
                    print(" Number of classroom in school = ",self.count)

            class Student(Classroom):
                def show_student(self,total):
                    self.total=total
                    print(" Total number of students i school = ",total)


            s=Student()
            s.input("Blossom","Tathawade")
            s.show_school()
            s.show_classroom(10)
            s.show_student(50)
            print("---------------------------------------------------------------------------------------------------------")


        case 3:
            class Shape:
                def show_shape(self,color):
                    self.color=color
                    print(" \ncolour of shape = ",self.color)

            class Circle(Shape):
                def area_circle(self,rad):
                    self.rad=rad
                    area=3.14*self.rad*self.rad
                    print(" Area of circle = ",area)

            class Rectangle(Shape):
                def area_rectangle(self,l,b):
                    self.l=l
                    self.b=b
                    area=l*b
                    print(" Area of Rectangle = ",area)

            c=Circle()
            c.show_shape("Purple")
            c.area_circle(5)
            r=Rectangle()
            r.show_shape("Pink")
            r.area_rectangle(12,3)
            print("----------------------------------------------------------------------------------------------------------")
            

        
        case 4:
            class Camera:
                def __init__(self, megapixel):
                    self.megapixel = megapixel

                def show_camera(self):
                    print("\nCamera:", self.megapixel, "MP")


            class Phone:
                def __init__(self, sim):
                    self.sim = sim

                def show_phone(self):
                    print("SIM Slots:", self.sim)


            class Smartphone(Camera, Phone):
                def __init__(self, megapixel, sim, brand):
                    Camera.__init__(self, megapixel)
                    Phone.__init__(self, sim)
                    self.brand = brand

                def show_brand(self):
                    print("Brand:", self.brand)


            s = Smartphone(50, 2, "Samsung")

            s.show_camera()
            s.show_phone()
            s.show_brand()
            print("-----------------------------------------------------------------------------------------------------------")
            


        case _ :
            print("\n Inavlid Input!!!!!!    \n please enter valid input")
            print("-------
