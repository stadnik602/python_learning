from address import Address
from mailing import Mailing
address_1 = Address("G2B 6Z1", "Toronto", "Lake Shore", "456", "124")
address_2 = Address("N7R 0T1", "Vaughn", "Jane", "34", "15")
address_3 = Address("B7R 0U1", "Richmond Hill", "Bathurst", "89B", "1")
address_4 = Address("W3E 4T7", "Niagara Falls", "Main Street", "3C", "100")
address_5 = Address("J4K 9R1", "Saint John", "Jameson", "22", "9")
address_6 = Address("P2O 8I0", "Victoria", "Swanlake", "13", "32")

mail1 = Mailing(address_1, address_2, 125, "TR0001")
mail2 = Mailing(address_3, address_4, 125, "TR0002")
mail3 = Mailing(address_5, address_6, 125, "TR0003")

mailing = [mail1, mail2, mail3]

for mail in mailing:
      print(f"Shipping {mail.track} from {mail.address_from.city}, {mail.address_from.street}, {mail.address_from
            .building}-{mail.address_from.apt} to {mail.address_to.city}, {mail.address_to.street}, {mail.address_to
            .building}-{mail.address_to.apt}. The cost is {mail.cost}")