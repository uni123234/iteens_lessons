from db import Session, Group, Student, init_db
from sqlalchemy import select, update


def init_data():
    with Session() as session:
        group1y_5 = Group(name="Python 1y_5_23_3")
        group1y_7 = Group(name="Python 1y_7_22")
        group1y_2 = Group(name="Python 1y_2_22")

        group1y_7.students.extend(
            [
                Student(name="Андрій", second_name="Яцура",
                        email=f"example{i}@mail.io")
                for i in range(10)
            ])
        group1y_2.students.extend(
            [
                Student(name="Андрій", second_name="Яцура",
                        email=f"example2{i}@mail.io")
                for i in range(5)
            ])
        group1y_5.students.extend(
            [
                Student(name="Андрій", second_name="Яцура",
                        email=f"example3{i}@mail.io")
                for i in range(5)
            ])

        # for multiple models
        session.add_all([group1y_7, group1y_2, group1y_5])
        # session.add(group1y_5)
        session.commit()


def update_data():
    with Session() as session:

        request = select(Group).where(Group.name.like("%1y_5_23_3%"))
        group = session.scalars(request).one()
        group.name = "New name2"

        session.commit()


def select_data():
    with Session() as session:
        request = select(Group).where(Group.name.like("%1y_5_23_3%"))
        # print(request)
        # group = session.scalars(request).one()
        request = select(Student).where(Student.email.like("example3%"))
        # print(group.students)
        result = session.scalars(request).all()
        print(result)
        result[0].email = "malva.scrot@example.io"
        session.commit()


def main():
    init_db()
    init_data()
    select_data()
    update_data()


if __name__ == "__main__":
    main()
