from models import DeclarativeBase, engine, Session, Product, Supply, Sale, Customer

DeclarativeBase.metadata.create_all(engine)

with Session() as session:
    product1 = Product(name="Product1", stock=100)
    product2 = Product(name="Product2", stock=150)

    customer1 = Customer(name="Customer1")

    supply1 = Supply(quantity=50, product=product1)
    supply2 = Supply(quantity=75, product=product2)

    sale1 = Sale(quantity=20, product=product1, customer=customer1)
    sale2 = Sale(quantity=30, product=product2, customer=customer1)

    session.add_all([product1, product2, customer1,
                    supply1, supply2, sale1, sale2])
    session.commit()
