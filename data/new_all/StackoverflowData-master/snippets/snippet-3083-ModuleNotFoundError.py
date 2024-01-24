#Source: https://stackoverflow.com/questions/48087533/with-self-driver-session-as-session-attributeerror-enter-when-link-to-neo4
from neo4j.v1 import GraphDatabase
import pandas as pd


class LeaderNeo4j(object):
    def __init__(self, driver):
        self.driver = driver

    def close(self):
        self.driver.close()

    def add_relation(self, name, friend_name):
        with self.driver.session as session:
            session.write_transaction(self.create_relation, name, friend_name)

    @staticmethod
    def create_relation(tx, name, friend_name):
        tx.run("MATCH (d1:Department {department_name: $name}),(d2:Department {department_name: $friend_name})"
               "MERGE (d1)-[:下级]->(d2)",
               name=name, friend_name=friend_name)


if __name__ == '__main__':
    uri = "bolt://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "HBUE112"))
    MyNH = LeaderNeo4j(driver)
    print(MyNH)
    directory = r"D:\Program Files\neo4j-community-3.3.1\import"
    f_name = r"bumen.csv"
    file_data = pd.read_csv(directory + '\\' + f_name, encoding='utf-8')
    for i in range(file_data.shape[0]):
        line = file_data.irow(i)
        print(line[0], line[1])
        MyNH.add_relation(line[0], line[1])