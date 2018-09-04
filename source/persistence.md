Persistence
===========

Background
----------

Geppetto recently developed the possibility to persist data across
multiple runs by storing it into a relational database. The Data Model
(DB Persisted) tab in this
<https://www.lucidchart.com/documents/edit/ae8bd4d6-2226-4aee-9d56-774e323188a6/2>
document describes the object-oriented design that acts as a base for
the database model.

The org.geppetto.core bundle defines interfaces corresponding to this
model in the org.geppetto.core.data.model package. Also, the same bundle
defines POJO implementations for these interfaces in the
org.geppetto.core.data.model.local package. These POJO implementations
are used for the case when Geppetto is running without DB persistence
support.

The new org.geppetto.persistence bundle provides database friendly
implementations of the interfaces defined in the org.geppetto.core
bundle in its org.geppetto.persistence.db.model package. We are using
the JDO implementation called DataNucleus which helps us hide multiple
database related details behind JDO APIs. Also, the schema is generated
from Java code, so no need to keep track of database scripts for this.
We have chosen MySQL as the database implementation for now, but if
needed at some point, we will be able to switch to another SQL or noSQL
based database engine.

Getting started with database
-----------------------------

-   Download and install MySQL. You can download the appropriate version
    of MySQL here: <http://dev.mysql.com/downloads/mysql/>
-   Once downloaded, start the MySQL server installation and follow
    the instructions. When asked about the setup type, you can select a
    "Custom" installation and manually select what extra tools may
    be needed. There will be some configuration steps as well and you
    will be asked to provide a password for the server admin user. The
    installation package includes the "MySQL Workbench" as well which is
    a client tool for managing MySQL servers. However, developers may
    want to choose another tool for this.
-   Start MySQL Workbench (or other management UI client) and create a
    new database and a new database user. You can use the script below
    for this

    > create database geppetto;
    >
    > create user user\_name identified by 'password';
    >
    > grant all privileges on geppetto.\* to <'user_name'@'localhost>'
    > identified by 'password';

-   You can now checkout the org.geppetto.persistence bundle and make
    sure Virgo deploys it as well at runtime
-   A file like the one below will need to be added to the
    {user.home}/geppetto/db.properties

    > javax.jdo.option.ConnectionURL=jdbc:mysql://localhost/geppetto
    >
    > javax.jdo.option.ConnectionDriverName=com.mysql.jdbc.Driver
    >
    > javax.jdo.option.ConnectionUserName=user\_name
    >
    > javax.jdo.option.ConnectionPassword=password

-   Now, when starting Virgo, if the persistence bundle is deployed then
    there will be database support available
-   In order to have some test data in the database, there is a
    DBTestData class available in the org.geppetto.persistence.util
    package in the org.geppetto.persistence bundle which can be run as a
    standalone Java application and which will handle the population of
    test data.

The biggest issue with all this is related to DataNucleus. There is an
"enhance" goal in the persistence pom.xml that, when running, it
enhances the model classes for being supported by DataNucleus. However,
sometimes mvn clean install, Maven Update are not sufficient. A
right-click on the Virgo Runtime server, followed by "Clean..." usually
fixes the issue with the classes.

It turns out that not even "Clean..." helps, so the remaining approach
is to stop the server, run mvn clean install on the persistence bundle,
overwrite the stage/org.geppetoo.persistence.jar/org in Virgo with the
org directory in org.geppetto.persistence/target/classes and try again.

A longer term solution would be to find the way to make sure that the
enhancer runs as part of the Maven / Update Project.

Setting up for Amazon S3 support
--------------------------------

-   Ask for the GeppettoDBAdmin user credentials and save them into a
    file located in {user.home}/geppetto/aws.credentials having a
    structure like the one below:

    > accessKey=the GeppettoDBAdmin access key
    >
    > secretKey=the GeppettoDBAdmin secret key

-   Set the S3 bucket name in `org.geppetto.core/src/main/resources/Geppetto.properties`

-   The APIs for handling S3 persistence operations are located in the
    S3Manager class in the org.geppetto.core bundle

