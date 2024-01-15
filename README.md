# SpaceX Launch Data

This is a python celery app that polls data from space_x launches API and loads it into a postgres database.

## Installation

1. Clone the repository: `git clone https://github.com/username/spacex_launch_data.git`
2. Navigate to the project directory: `cd spacex_launch_data`
3. Run `docker-compose up`
4. Follow the logs or access celery flower instance http://localhost:5555 to see the status of tasks
5. To see the contents of the database run the following commands:
```
docker-compose exec db bash
su postgres
psql
\c space_x
select * from launches
```