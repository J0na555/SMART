from django.db import models





class Grade(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name



class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    student_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254, unique=True)
    gender = models.CharField(max_length= 7, choices= GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    grade = models.ForeignKey(Grade, on_delete= models.CASCADE)

    class Meta:
        ordering = ['first_name', 'last_name']

 

    def __str__(self):
        return f"{self.first_name}{ self.last_name}"



class Subject(models.Model):
    name = models.CharField(max_length=20)
    code = models.IntegerField(unique=True)
    description = models.TextField()


    def __str__(self):
        return self.name





class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique= True)



    def __str__(self):
        return f"{self.first_name}{ self.last_name}"




class Assessment(models.Model):

    TESTCHOICES = [
        ('Quiz', 'Quiz'),
        ('MidTerm', 'MidTerm'),
        ('Assignment', 'Assignment'),
        ('Final', 'Final'),
        ('Project', 'Project')
    ]

    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=TESTCHOICES)
    max_score = models.DecimalField(max_digits=10, decimal_places= 4)
    weight = models.DecimalField(max_digits= 5, decimal_places= 2)
    date = models.DateField(auto_now_add=True)


    subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete= models. CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete= models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['name', 'grade', 'subject'], name='unique_assessment')
        ]


    def __str__(self):
        return self.name


class AcademicYear(models.Model):
    name = models.CharField(max_length= 20)
    start_date = models.DateField()
    end_date = models.DateField()



    def __str__(self):
        return self.name




class Semester(models.Model):
    name = models.CharField(max_length= 20)
    start_date = models.DateField()
    end_date = models.DateField()

    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'academic_year'], name= 'unique_term')
        ]

    def __str__(self):
        return self.name

class Mark(models.Model):
    score = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    comment = models.TextField()

    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete= models.CASCADE)


    def __str__(self):
        return str(self.score)
