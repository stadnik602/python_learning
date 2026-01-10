from mailing import Mailing
from address import Address

add_to = Address("G2B 6Z1", "Toronto", "Lake Shore", "456", "124")
add_from = Address("N7R 0T1", "Vaughn", "Jane", "34", "15")
cost = 125
track = "TR0001"

request = Mailing(add_to, add_from, cost, track)
response = Mailing(add_to, add_from, cost, "TR0002")

print(f"Shipping {request.track} from {request.address_from.city}, {request.address_from.street}, {request.address_from.building}-{request.address_from.apt} to {request.address_to.city}, {request.address_to.street}, {request.address_to.building}-{request.address_to.apt}. The cost is {cost}")