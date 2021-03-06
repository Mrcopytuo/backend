from django.db import models

# Create your models here.


class QuestionType(models.IntegerChoices):
    SINGLE = 0
    MULTIPLE = 1


class Contest(models.Model):
    contest_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    publisher_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    participant_number = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    chapter = models.IntegerField()
    description = models.CharField(max_length=512)


class AttendContest(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    contest_id = models.ForeignKey('Contest', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        unique_together = (('user_id', 'contest_id'),)


class ContestQuestion(models.Model):
    contest_id = models.ForeignKey('Contest', on_delete=models.CASCADE)
    question_id = models.IntegerField()
    question_type = models.IntegerField(
        choices=QuestionType.choices,
        default=QuestionType.SINGLE
    )

    class Meta:
        unique_together = (('contest_id', 'question_id', 'question_type'),)


class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    contest_id = models.ForeignKey('Contest', on_delete=models.CASCADE)
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    match_tag = models.IntegerField(default=0)


class ContestSubmission(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    contest_id = models.ForeignKey('Contest', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    question_id = models.IntegerField()
    question_type = models.IntegerField(
        choices=QuestionType.choices,
        default=QuestionType.SINGLE
    )
    answer = models.CharField(max_length=16)

    class Meta:
        unique_together = (('user_id', 'contest_id', 'question_id', 'question_type'),)
