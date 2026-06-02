from airflow.sdk import dag, task 
from pendulum import datetime
from airflow.timetables.trigger import CronTriggerTimetable


@dag(
        dag_id="cron_schedule_dag",
        start_date= datetime(year=2026, month=6, day=2, tz="America/Halifax"),
        schedule=CronTriggerTimetable("0 9 * * MON-FRI",timezone="America/Halifax"),
        end_date= datetime(year=2026, month=6, day=3, tz="America/Halifax"),
        is_paused_upon_creation=False,
        catchup=True
)
def cron_schedule_dag():

    @task.python
    def first_task():
        print("This is the first task")

    @task.python
    def second_task():
        print("This is the second task")
    
    @task.python
    def third_task():
        print("This is the third task. DAG complete!")
    
    
    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
    
    first >> second >> third

# Instantiating the DAG
cron_schedule_dag()