A web application that allows you to work with orders by making http requests to the application's API. An order is an entity that provides information about what customers want to buy. A single order can contain different products with different quantities and different prices. The entity that contains this information in an Order is called an Order Detail. An Order can be linked to an entity that represents the same order in an external system. Orders are created with a "new" status. Users processing the Orders may transfer them to the following statuses: "accepted" or "rejected". Users should not be able to delete "accepted" Orders.<br>
Full description: https://github.com/cloudblue/connect-intern-program-python-task

____
**Docker:**
- docker-compose in dev/docker-compose.yml to run only db on the localhost and develop locally. <br>
- docker-compose in the main directory to run app with db.

____
**.env:** <br>
SECRET_KEY=django-insecure-*5ca^0m=+-rd)6e_h2=2w)vz*!1(mj3hp6j%nq=+c_gshbax2& <br>
DEBUG=True <br>
POSTGRES_HOST=localhost <br>
POSTGRES_PROD_HOST=db <br>
POSTGRES_PORT=5432 <br>
POSTGRES_DB=ingramTask <br>
POSTGRES_USER=postgres <br>
POSTGRES_PASSWORD=123456 <br>
