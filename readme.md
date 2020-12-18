# Spotify Extension

Trello Board: 

---

## Overview



---

## Install Steps

<!-- You will need the latest version of python and the pip package manager to complete the installation steps. Once you have python and pip, the steps are as follows:

- Clone the repository: `git clone https://github.com/rheal3/`
- Change directory into the repository: `cd receipt_app`
- Make sure venv is installed: `pip install venv`
- Create the virtual environment: `python3 -m venv venv`
- Activate the virtual environment: `source venv/bin/activate`
- Install the dependencies from requirments.txt: `pip3 install -r requirements.txt`
- Run the app: `python src/main.py` -->

---

## CI/CD

The CI/CD pipeline was created using Github Actions. It uses Python3.8, Pip3 and runs on the latest stable version of Ubuntu. The pipeline is started on a push to master.

Once it has pulled from master it installs the dependencies form requirements.txt and then it runs the tests in the tests directory.

---

## ???

The spotify extension uses the ORM model. This provides security from SQL injections.

Storing data in the correct way is HUGELY important. If data is stored incorrectly the ramifications are not small, but large. The programmer has both an ethical and legal obligation to store data in the correct way. Ethically, the user needs to be warned of potential disasters within a terms and conditions type of disclosure. Legally, the company can be held accountable if information (such as financial information from credit cards) is stolen and used by attackers. 

Within the database, the passwords are stored in hashes rather than encrypted, becuase as we all know too well things that have been encrypted can be decrypted. DUN DUUN. The hash is a much safer option as is takes the password, does magic, and returns the same hash for that password each time making it easy to check against the stored password hash. In addition, salt can be added to make it even more uncrackable!! The salt is another secret bit that's unique to the site that is added on to the hashed password. Now the attacker would need to know the password and the salt to get in!

In general, AWS has good security and good practices. However, these can be improved upon by using a private subnet when storing your database. This will make it so the user never accesses the database directly and it is accessed by the site instead, making it much safer.

---

## Database Schema

<!-- - customer many or zero orders, orders one and only one customer

- basket zero or one users, users one and only one basket

- product many or zero orders, orders many or one product

- category many or one product, product many or one category

- basket many or zero products, products many or zero baskets

- order_details one and only one order, orders one and only one order_details
- order_details many or one product, product many or zero order_details

![](./docs/db/schema.png) -->

---

## Swagger

<!-- The swagger file shows the endpoints that will be used in the application. The endpoints include: shop, user, and orders.

The swagger file is located at `.github/swagger.yml`. To view, it can be uploaded to https://editor.swagger.io/# or viewed in the terminal using the `less` or `cat` commands. -->

