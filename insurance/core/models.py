from django.db import models

# Create your models here.
class DefaultEntityManager(models.Manager):
    use_in_migrations = True
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset()

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    objects = DefaultEntityManager()

class Insured(BaseModel):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    profission = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    cpf = models.CharField(max_length=14)
    instagram = models.CharField(max_length=255, null=True)
    observation = models.TextField(null=True)
    recomentation_observation = models.TextField(null=True)

class Spouse(BaseModel):
    insured = models.ForeignKey(Insured, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    profission = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    cpf = models.CharField(max_length=14)
    instagram = models.CharField(max_length=255, null=True)
    observation = models.TextField(null=True)

class Dependent(BaseModel):
    insured = models.ForeignKey(Insured, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bith_date = models.DateField()
    independence_age = models.SmallIntegerField()
    observation = models.TextField(null=True)

class QuestionType(BaseModel):
    question_type = models.CharField(max_length=255)

class Question(BaseModel):
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)

class InsuredAnswer(BaseModel):
    insured = models.ForeignKey(Insured, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000)

    class Meta:
        unique_together = ('insured', 'question')

class AnswerTypeObservation(BaseModel):
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    insured = models.ForeignKey(Insured, on_delete=models.CASCADE)
    observation = models.TextField()

    class Meta:
        unique_together = ('insured', 'question_type')

class Recomentation(BaseModel):
    insured = models.ForeignKey(Insured, on_delete=models.CASCADE)
    recomentation = models.TextField()
