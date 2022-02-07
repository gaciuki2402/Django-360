from tabnanny import verbose
from django.db import models


class question(models.Model):
    question_text=models.CharField(max_length=500)
    published_date=models.DateTimeField("date that it was published")

    def __str__(self):
        return f"{self.question_text}"
class details(models.Model):
    Person=models.CharField(max_length=29)
    first_name=models.CharField(max_length=200)
    middle_name=models.CharField(max_length=50)
    surname=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Person}"
    
    class Meta:
        verbose_name_plural="Details"

class Books(models.Model):
    category_choices=(
        ("Novel","Novel"),
        ("Maths","Maths")
    )
    Librarian=models.CharField(max_length=29)
    Book=models.CharField(max_length=30)
    ISBN_No=models.CharField(max_length=39)
    Date_Added=models.DateTimeField(auto_now_add=True)
    Date_Updated=models.DateTimeField(auto_now=True)
    category=models.CharField(max_length=30,choices=category_choices)
    Author=models.CharField(max_length=30)
    Date_published=models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return f"{self.Librarian}"

    class Meta:
        verbose_name_plural="Books"
class Mess(models.Model):
    Food_Choices=(
        ("Chapati","Chapati"),
        ("African_Stew","African_Stew"),
        ("Viazi","Viazi"),
        ("Coffee","Coffee"),
        ("Ugali","Ugali"),
        ("Sukuma","Sukuma"),
        ("Cabbage","Cabbage")

    )
    Food=models.CharField(max_length=20,choices=Food_Choices,unique=True)
    Meal_Time_Choices=(
        ("Lunch","Lunch"),
        ("Breakfast","Breakfast"),
        ("supper","supper")

    )
    Price=models.FloatField(max_length=20)
    Date_Added=models.DateTimeField(auto_now_add=True)
    Date_Updated=models.DateTimeField(auto_now=True)
    Meal_Time=models.CharField(max_length=30,choices=Meal_Time_Choices)
    Available=models.BooleanField(default=True)
    Number_of_Plates=models.IntegerField(max_length=5)

    def __str__(self):
        return f"{self.Food}"

    class Meta:
        verbose_name_plural="Mess"


class Fruit(models.Model):
    name=models.CharField(max_length=30, primary_key=True, unique=True)

    def __str__(self):
        return f"{self.name}"






