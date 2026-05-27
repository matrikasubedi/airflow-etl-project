from airflow.sdk import dag, task

@dag(
        dag_id = "versioned_dag",
)
def versioned_dag():

    @task.python
    def first_task():
        print("This is the first Task")

    
    @task.python
    def second_task():
        print("This is the second Task")

    @task.python
    def third_task():
        print("This is the third Task")

    @task.python
    def versioned_task():
        print("This is the versoning Task")



    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
    version = versioned_task()

    first >> second >> third >> version


# Instantiating the dag
versioned_dag()



