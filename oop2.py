class students:
    def __init__(self,name,course,gender,age):
        self.name=name
        self.corse=course
        self.gender=gender
        self.age=age
    def dispaly(self):
        print("name:%s \ncourse:%s\ngender:$s\nage:%d")
        % (self.name,self.course,self.gender,self.age))
students("Brian kipkoech","data science","male",19)
