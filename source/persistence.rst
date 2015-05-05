*************
Persistence
*************

Background
**********

Geppetto recently developed the possibility to persist data across multiple runs by storing it into a relational database. The Data Model (DB Persisted) tab in this https://www.lucidchart.com/documents/edit/ae8bd4d6-2226-4aee-9d56-774e323188a6/2 document describes the object-oriented design that acts as a base for the database model.

The org.geppetto.core bundle defines interfaces corresponding to this model in the org.geppetto.core.data.model package. Also, the same bundle defines POJO implementations for these interfaces in the org.geppetto.core.data.model.local package. These POJO implementations are used for the case when Geppetto is running without DB persistence support.

The new org.geppetto.persistence bundle provides database friendly implementations of the interfaces defined in the org.geppetto.core bundle in its org.geppetto.persistence.db.model package. We are using the JDO implementation called DataNucleus which helps us hide multiple database related details behind JDO APIs. Also, the schema is generated from Java code, so no need to keep track of database scripts for this. We have chosen MySQL as the database implementation for now, but if needed at some point, we will be able to switch to another SQL or noSQL based database engine.

Getting started with database
*****************************

* Download and install MySQL. You can download the appropriate version of MySQL here: http://dev.mysql.com/downloads/mysql/
* Once downloaded, start the MySQL server installation and follow the instructions. When asked about the setup type, you can select a "Custom" installation and manually select what extra tools may be needed. There will be some configuration steps as well and you will be asked to provide a password for the server admin user. The installation package includes the "MySQL Workbench" as well which is a client tool for managing MySQL servers. However, developers may want to choose another tool for this.
* 
