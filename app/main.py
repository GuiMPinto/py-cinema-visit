from app.cinema.bar import sell_product
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:

    customer_instances = []
    for customer_data in customers:
        customer = Customer(name=customer_data["name"],
                            food=customer_data["food"])
        customer_instances.append(customer)

    cleaner_instance = Cleaner(cleaner)

    hall = CinemaHall(hall_number)

    for customer_data in customer_instances:
        sell_product(customer_data.food, customer_data)

    hall.movie_session(movie, customer_instances, cleaner_instance)        
