from ..base import Task, TaskRecord


class RunningTask(Task):
    """ Model for running task
        User needs to set running duration days and distance as 
        objective
    """
    duration_days = models.IntegerField(null=False)
    distance = models.FloatField(null=False)


class RunningTaskRecord(TaskRecord):
    """ Model for running task record
        To save user's actual running distance per day
    """
    distance = models.FloatField(default=0)
    # A screenshot image to show current running distance
    voucher = models.ImageField(blank=True)
