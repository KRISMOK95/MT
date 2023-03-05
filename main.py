import aas_core3_rc02.types as aas_types

''' #this can connect to MODBUSs
# You can directly access the element properties.
another_element.value = b'\xDE\xAD\xC0\xDE'
'''



# Create the chiller temperature property
chiller_temp = aas_types.Property(
    id_short="chiller_temp",
    value_type=aas_types.DataTypeDefXsd.FLOAT,
    value="0.0"
)

# Create the chiller status property
chiller_status = aas_types.Property(
    id_short="chiller_status",
    value_type=aas_types.DataTypeDefXsd.STRING,
    value="OFF"
)

# Create the submodel for the chiller
chiller_submodel = aas_types.Submodel(
    id="chiller_submodel",
    submodel_elements=[chiller_temp, chiller_status]
)

# Create the environment to wrap it all up
environment = aas_types.Environment(
    submodels=[chiller_submodel]
)

# Now you can access and modify the properties of the chiller
environment.submodels[0].submodel_elements[0].value = 20.0 # set chiller temperature to 20.0
environment.submodels[0].submodel_elements[1].value = "ON" # set chiller status to ON
