# from dotenv import dotenv_values
# import psycopg2
#
# config = dotenv_values(".env")
#
# host = config["HOST"]
# port = config["PORT"]
# user = config["USER_ID"]
# password = config["USER_PW"]
# database = config["DB_NAME"]
#
# # try:
# #     connection = psycopg2.connect(
# #         host=host,
# #         port=port,
# #         user=user,
# #         password=password,
# #         database=database
# #     )
# #     connection.autocommit = True
# #
# #
# #     with connection.cursor() as cursor:
# #         cursor.execute(
# #             '''
# #                 create table project (
# #                     id int primary key,
# #                     name varchar(50) not null,
# #                     description varchar(255) not null
# #                 );
# #             '''
# #         )
# #
# #
# #     with connection.cursor() as cursor:
# #         cursor.execute(
# #             '''
# #                 insert into project (id, name, description) values
# #                 (1, 'project1', 'project1 description'),
# #                 (2, 'project2', 'project2 description'),
# #                 (3, 'project3', 'project3 description');
# #             '''
# #         )
# #
# #
# #     with connection.cursor() as cursor:
# #         cursor.execute(
# #             '''
# #                 insert into project (id, name, description) values
# #                 (%s, %s, %s), (%s, %s, %s), (%s, %s, %s);
# #             ''',
# #             [(4, 'project4', 'project4 description'),
# #                 (5, 'project5', 'project5 description'),
# #                 (6, 'project6', 'project6 description')]
# #         )
# #
# #
# #     with connection.cursor() as cursor:
# #         cursor.execute(
# #             '''
# #                 select * from project;
# #             '''
# #         )
# #
# #         print(cursor.fetchone())
# #
# #         for line in cursor.fetchall():
# #             print(f'ID: {line[0]}')
# #             print(f'Name: {line[1]}')
# #             print(f'Description: {line[2]}')
# #             print()
# #
# #
# #     with connection.cursor() as cursor:
# #         cursor.execute(
# #             '''
# #                 alter table project
# #                 add column created_on timestamp not null default now();
# #             '''
# #         )
# #
# #
# #     with connection.cursor() as cursor:
# #         cursor.execute(
# #             '''
# #                 update project
# #                 set description = 'new desc'
# #                 where name = 'new project';
# #             '''
# #         )
# #
# #
# #     with connection.cursor() as cursor:
# #         cursor.execute(
# #             '''
# #                 delete from project
# #                 where name = 'new project';
# #             '''
# #         )
# #
# #     connection.close()
# #
# # except Exception as e:
# #     print(e)


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return 'Hello World!'

@app.get("/about")
def about():
    return 'About page'


cars = [
    {'1': 'BMW'},
    {'2': 'Mercedes'},
    {'3': 'Audi'},
    {'4': 'Lada'}


]

@app.get('/cars/{car_id}/name')
def get_car(car_id: int):
    return cars[car_id - 1][1]






