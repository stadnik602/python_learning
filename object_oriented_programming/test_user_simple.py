import csv

def test_workers_are_adult():
    with open("users.csv") as csvfile:
        users = csv.DictReader(csvfile, delimiter=";")
        workers = [user for user in users if user["status"] == "worker"]
    for worker in workers:
        assert int(worker["age"]) > 18, f"Worker age of {worker["name"]} is lower than 18"

test_workers_are_adult()
