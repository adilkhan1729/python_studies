# class Sample:
#     pencil,erasor=10,10
# s=Sample()
# print("value of x = ",s.pencil)
# print("value of y=",s.erasor)
# print("value of sum x and y = ",s.pencil+s.erasor)        
class student:
    mark1,mark2,mark3=45,91,71
    def process(self):

        sum =student.mark1+student.mark2+student.mark3
        avg=sum/3
        print("total marks=",sum)
        print("average marks =",avg)
s=student()
s.process()        