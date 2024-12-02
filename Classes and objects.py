class Student:
  name="karan"

s1=Student()
print(s1.name)

class Car:
  color="blue"
  brand="bmw"

c1=Car()
print(c1.color)
print(c1.brand)

class Demo():
  a=10

  def square(self,a,b):
    print(a+b)

d=Demo()
d.square(2313,24234)

class Complex():

  def __init__(self,r,i):
    self.real=r
    self.imag=i

  def display(self):
    print(self.real,'+',self.imag,'i')

  def __str__(self):
        return f"{self.real} + {self.imag}i"

  def add(self,r):
    x=self.real+r.real
    y=self.imag+r.imag
    result=Complex(x,y)
    print(result)
    return result

  def subt(self,r):
    x=self.real-r.real
    y=self.imag-r.imag
    result=Complex(x,y)
    print(result)
    return result

  def mult(self,r):
    x=self.real*r.real-self.imag*r.imag
    y=self.imag*r.real+self.real*r.imag
    result=Complex(x,y)
    print(result)
    return result

  def truediv(self, other):
        denominator = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        result=Complex(real,imag)
        print(result)
        return result

c1=Complex(2,3)
c2=Complex(7,9)

print(c1.display())
print(c2.display())

c1.add(c2)
c1.subt(c2)
c1.mult(c2)
c1.truediv(c2)




# create a matrix using user input

r=int(input('Enter no. of rows : '))
c=int(input('Enter no. of columns : '))
main=[]
for i in range(r):
  l=[]
  for j in range(c):
    n=int(input('Enter the element : '))
    l.append(n)
  main.append(l)
print(main)

class Matrix:
    def __init__(self, r, c):
        self.rows = r
        self.cols = c
        self.arr = []

    def Fill_Matrix(self):
        print('Enter the elements of matrix row-wise')
        self.arr = []
        for i in range(self.rows):
            l = []
            for j in range(self.cols):
                n = int(input('Enter the element : '))
                l.append(n)
            self.arr.append(l)
        print('Matrix completed')

    def Display_Matrix(self):
        for row in self.arr:
            print(" ".join(map(str, row)))

    def Add_Matrix(self, m):
        if self.rows != m.rows or self.cols != m.cols:
            raise ValueError("Matrices dimensions do not match for addition.")
        mat = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            lst = []
            for j in range(self.cols):
                lst.append(self.arr[i][j] + m.arr[i][j])
            mat.arr.append(lst)
        return mat

    def multiply(self, m):
        if self.cols != m.rows:
            raise ValueError("Matrices dimensions do not match for multiplication.")
        mat = Matrix(self.rows, m.cols)
        for i in range(self.rows):
            lst = []
            for j in range(m.cols):
                temp = 0
                for k in range(self.cols):
                    temp += self.arr[i][k] * m.arr[k][j]
                lst.append(temp)
            mat.arr.append(lst)
        return mat

    def transpose(self):
        mat = Matrix(self.cols, self.rows)
        for i in range(self.cols):
            lst = []
            for j in range(self.rows):
                lst.append(self.arr[j][i])
            mat.arr.append(lst)
        return mat

print('Fill Matrix 1:')
mat1 = Matrix(3, 3)
mat1.Fill_Matrix()
print('Fill Matrix 2:')
mat2 = Matrix(3, 3)
mat2.Fill_Matrix()
print('First Matrix: ')
mat1.Display_Matrix()
print('Second Matrix: ')
mat2.Display_Matrix()
print('After addition: ')
mat3 = mat1.Add_Matrix(mat2)
mat3.Display_Matrix()
print('After multiplication: ')
mat4 = mat1.multiply(mat2)
mat4.Display_Matrix()
print('Transpose of Matrix 1: ')
mat5 = mat1.transpose()
mat5.Display_Matrix()


class Solid:
    def __init__(self, len_cbd=0, br_cbd=0, ht_cbd=0, len_cube=0, ht_cyl=0, rad_cyl=0, rad_sphere=0):
        self.len_cbd = len_cbd
        self.br_cbd = br_cbd
        self.ht_cbd = ht_cbd
        self.len_cube = len_cube
        self.ht_cyl = ht_cyl
        self.rad_cyl = rad_cyl
        self.rad_sphere = rad_sphere

    def sa_cbd(self):
        sa = 2 * (self.len_cbd * self.br_cbd) + 4 * (self.br_cbd * self.ht_cbd)
        print('Surface area of cuboid:', sa)

    def vol_cbd(self):
        vol = self.len_cbd * self.br_cbd * self.ht_cbd
        print('Volume of cuboid:', vol)

    def sa_cube(self):
        sa = 6 * (self.len_cube ** 2)
        print('Surface area of cube:', sa)

    def vol_cube(self):
        vol = self.len_cube ** 3
        print('Volume of cube:', vol)

    def sa_cyl(self):
        sa = 2 * 3.14 * self.rad_cyl * (self.rad_cyl + self.ht_cyl)
        print('Surface area of cylinder:', sa)

    def vol_cyl(self):
        vol = 3.14 * (self.rad_cyl ** 2) * self.ht_cyl
        print('Volume of cylinder:', vol)

    def sa_sphere(self):
        sa = 4 * 3.14 * (self.rad_sphere ** 2)
        print('Surface area of sphere:', sa)

    def vol_sphere(self):
        vol = (4 / 3) * 3.14 * (self.rad_sphere ** 3)
        print('Volume of sphere:', vol)

while True:
    x = int(input('''
    1. Cuboid
    2. Cube
    3. Cylinder
    4. Sphere
    5-9. Exit
    Enter your choice: '''))

    if x == 1:
        len_cbd = int(input('Enter length of cuboid: '))
        br_cbd = int(input('Enter breadth of cuboid: '))
        ht_cbd = int(input('Enter height of cuboid: '))
        s = Solid(len_cbd=len_cbd, br_cbd=br_cbd, ht_cbd=ht_cbd)
        s.sa_cbd()
        s.vol_cbd()

    elif x == 2:
        len_cube = int(input('Enter side of cube: '))
        s = Solid(len_cube=len_cube)
        s.sa_cube()
        s.vol_cube()

    elif x == 3:
        rad_cyl = int(input('Enter radius of cylinder: '))
        ht_cyl = int(input('Enter height of cylinder: '))
        s = Solid(rad_cyl=rad_cyl, ht_cyl=ht_cyl)
        s.sa_cyl()
        s.vol_cyl()

    elif x == 4:
        rad_sphere = int(input('Enter radius of sphere: '))
        s = Solid(rad_sphere=rad_sphere)
        s.sa_sphere()
        s.vol_sphere()

    else:
        break
