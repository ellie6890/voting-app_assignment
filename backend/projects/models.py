from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def average_score(self):
        votes = self.vote_set.all()
        if votes.exists():
            return sum(v.score for v in votes) / votes.count()
        return 0

class Vote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    score = models.IntegerField()
