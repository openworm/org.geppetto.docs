


Simulation File Document
=====================

This aim of this tutorial is to guide you through the process of creating a Simulation file that can be loaded in Geppetto.

Getting Started
---------
Simulations used within Geppetto are specified within an XML file, which follows a specific schema_

.. _schema: https://github.com/openworm/org.geppetto.simulation/blob/master/src/main/resources/schema/simulationSchema.xsd

.. code-block:: xml

    <schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.openworm.org/simulationSchema"
		xmlns:tns="http://www.openworm.org/simulationSchema" elementFormDefault="qualified" 
		xmlns:jxb="http://java.sun.com/xml/ns/jaxb" jxb:version="2.0">
	<complexType name="Model">
		<sequence>
			<element name="modelInterpreterId" type="string" maxOccurs="1" minOccurs="1"></element>
			<element name="modelURL" type="string" maxOccurs="1" minOccurs="1"></element>
			<element name="instancePath" type="string" maxOccurs="1" minOccurs="0"></element>
			<element name="parentAspect" type="tns:Aspect" maxOccurs="1" minOccurs="0"></element>
			<element name="recordingURL" type="string" maxOccurs="unbounded" minOccurs="0"></element>
		</sequence>
	</complexType>

	<complexType name="Simulator">
		<sequence>
			<element name="simulatorId" type="string" maxOccurs="1" minOccurs="0"></element>
			<element name="timeStep" type="tns:TimeStep" maxOccurs="1" minOccurs="0"></element>
			<element name="instancePath" type="string" maxOccurs="1"  minOccurs="0"></element>
			<element name="parentAspect" type="tns:Aspect" maxOccurs="1" minOccurs="0"></element>
		</sequence>
	</complexType>

	<complexType name="TimeStep">
		<sequence>
			<element name="type" type="tns:TimeStepType" maxOccurs="1" minOccurs="1"></element>
			<element name="value" type="float" maxOccurs="1" minOccurs="0"></element>
		</sequence>
	</complexType>

	<complexType name="Point3D">
		<sequence>
		   <element name="x" type="float" maxOccurs="1" minOccurs="1"></element>
		   <element name="y" type="float" maxOccurs="1" minOccurs="1"></element>
		   <element name="z" type="float" maxOccurs="1" minOccurs="1"></element>
		</sequence>
	</complexType>

	<simpleType name="TimeStepType">
		<restriction base="string">
			<enumeration value="FIXED" />
			<enumeration value="VARIABLE" />
		</restriction>
	</simpleType>

	<complexType name="Aspect">
		<sequence>
			<element name="id" type="string" maxOccurs="1" minOccurs="1"></element>
			<element name="instancePath" type="string" maxOccurs="1" minOccurs="0"></element>
			<element name="model" type="tns:Model" maxOccurs="1" minOccurs="1"></element>
			<element name="simulator" type="tns:Simulator" maxOccurs="1" minOccurs="0"></element>
			<element name="parentEntity" type="tns:Entity" maxOccurs="1" minOccurs="0"></element>
		</sequence>
	</complexType>

	<complexType name="Entity">
		<sequence>
			<element name="id" type="string" maxOccurs="1" minOccurs="1"></element>
			<element name="instancePath" type="string" maxOccurs="1" minOccurs="0"></element>
			<element name="aspect" type="tns:Aspect" maxOccurs="unbounded" minOccurs="1">
				<annotation>
					<appinfo>
						<jxb:property name="aspects" />
					</appinfo>
				</annotation>
			</element>
			<element name="parentEntity" type="tns:Entity" maxOccurs="1" minOccurs="0"></element>
			<element name="entity" type="tns:Entity" maxOccurs="unbounded" minOccurs="0">
				<annotation>
					<appinfo>
						<jxb:property name="entities" />
					</appinfo>
				</annotation>
			</element>
			<element name="position" type="tns:Point3D" minOccurs="0" maxOccurs="1"></element>
		</sequence>
	</complexType>

	<element name="simulation">
		<complexType>
			<sequence>
				<element name="entity" type="tns:Entity" maxOccurs="unbounded" minOccurs="1">
					<annotation>
						<appinfo>
							<jxb:property name="entities" />
						</appinfo>
					</annotation>
				</element>
				<element name="script" type="string" maxOccurs="unbounded" minOccurs="0"></element>
			</sequence>
		</complexType>
	</element>
    </schema>

The Simulation file starts with the head tag pointing to the different schema location that will be used to describe the file as seen below. 

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <tns:simulation xmlns:tns="http://www.openworm.org/simulationSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
		    xsi:schemaLocation="http://www.openworm.org/simulationSchema ../../src/main/resources/schema/simulationSchema.xsd ">
    </tns:simulation>

Then, inside the Simulation tag, you need to define; the configuration type of the file, name and entities. The configuration tag is used to define the output format of the Simulation, typically RAW format, the name does as the word suggests, and the entities define the different models for the simulation. A Simulation file must have at least one entity, but there’s no cap on the maximum amount it can have.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <tns:simulation xmlns:tns="http://www.openworm.org/simulationSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
		    xsi:schemaLocation="http://www.openworm.org/simulationSchema ../../src/main/resources/schema/simulationSchema.xsd ">
        <tns:configuration>
            <tns:outputFormat>RAW</tns:outputFormat>
        </tns:configuration>
        <tns:entities>
            <tns:entity>
            </tns:entity>
        <tns:entities>
        <tns:name>example1</tns:name>
    </tns:simulation>


Using Entities
---------------
As explained in previous section, a Simulation can have multiple entities, and each entity can define multiple entities, they will form a tree structure. 

The tags used to describe an entity are the following:

- **ID** : Use to locate the entity, can be the name of entity as well

- **aspect**: Defines the model and simulator of an entity, multiples aspects can be specified within an entity. Each aspect specifies a simulator and a model, which are used for the simulation. 

- **simulator** : Defines the simulator use to run the entity via `<simulatorid>` inside the <simulator>
tag.

- **model** : The model that defines the entity, points to an external URL for the model. Two tags are used for the model, `<modelURL>` which points to the URL and `<modelInterpreterId>` which is used to load the model.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <tns:simulation xmlns:tns="http://www.openworm.org/simulationSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
		    xsi:schemaLocation="http://www.openworm.org/simulationSchema ../../src/main/resources/schema/simulationSchema.xsd ">
        <tns:configuration>
            <tns:outputFormat>RAW</tns:outputFormat>
        </tns:configuration>
        <tns:entities>
            <tns:entity>
                <tns:id>muscle_cell</tns:id>
                <tns:aspects>
                    <tns:aspect>
                        <tns:modelInterpreter>lemsModelInterpreter</tns:modelInterpreter>                                 
                        <tns:modelURL>https://dl.dropboxusercontent.com/u/7538688/GeppettoSimulations/SingleComponentHH/LEMS_NML2_Ex5_DetCell.xml?dl=1</tns:modelURL>
                        <tns:simulator>jLemsSimulator</tns:simulator>
                        <tns:id>example1</tns:id>
                        <tns:group>group1</tns:group>
                    </tns:aspect>
                    <tns:aspect>
                        <tns:modelInterpreter>lemsModelInterpreter
                        </tns:modelInterpreter>
                        <tns:modelURL>https://dl.dropboxusercontent.com/u/7538688/GeppettoSimulations/SingleComponentHH/LEMS_NML2_Ex5_DetCell.xml?dl=1</tns:modelURL>
                        <tns:simulator>jLemsSimulator</tns:simulator>
                        <tns:id>example1</tns:id>
                        <tns:group>group1</tns:group>
                    </tns:aspect>
                </tns:aspects>
            </tns:entity>   
        <tns:entities>
        <tns:name>example1</tns:name>
    </tns:simulation>
Scripts
---------------
You can specify a `<script>` tag within the root `<simulation>` tag. This tag should point to an external URL containing a javascript files with a set of Geppetto Commands_. The script will be executed right after the simulation is loaded, and the commands within the script executed in order one after another.

.. _Commands: http://docs.geppetto.org/en/latest/intro.html#g-object-commands
  
.. code-block:: xml

    <tns:scripts>
      <tns:script>
        <tns:URL>https://dl.dropboxusercontent.com/u/7538688/electrofluid.py</tns:scriptURL>
       </tns:script>
    </tns:scripts>
    