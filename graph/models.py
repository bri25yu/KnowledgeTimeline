from django.db import models


class Group(models.Model):
    name = models.TextField()
    color = models.CharField(max_length=20, default="aliceblue")

    def __repr__(self) -> str:
        return f"Group(name={self.name}, color={self.color})"

    def __str__(self) -> str:
        return repr(self)


class Node(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.TextField()
    summary = models.TextField()
    description = models.TextField()
    link = models.TextField()
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    authors = models.TextField()

    def __repr__(self) -> str:
        group = f"group={self.group}"
        summary = f"summary={self.summary}"
        year = f"year={self.year}"
        month = f"month={self.month}"
        return f"Node({group}, {summary}, {year}, {month})"

    def __str__(self) -> str:
        return repr(self)
