if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    nonzero_data = data[(data['passenger_count']>0) & (data['trip_distance']>0)]
 
    non_zero_passengers_count = nonzero_data['passenger_count'].count()

    nonzero_data['lpep_pickup_date'] = nonzero_data['lpep_pickup_datetime'].dt.date

    nonzero_data['lpep_dropoff_date'] = nonzero_data['lpep_dropoff_datetime'].dt.date
    
    print(non_zero_passengers_count)

    print(nonzero_data.shape)

    print(nonzero_data['VendorID'].value_counts())

    # Function to convert Camel Case
    def camel_to_snake(column_name):
        result = [column_name[0].lower()]

        for char in column_name[1:]:
            if char.isupper():
                if len(result)>2:
                    if result[-2]== '_':
                        result.append(char.lower())
                    else:
                        result.extend(['_', char.lower()])
                else:
                        result.extend(['_', char.lower()])
            else:
                result.append(char)
        return ''.join(result)

    # Rename columns in the DataFrame
    nonzero_data.columns = [camel_to_snake(col) for col in nonzero_data.columns]

    return nonzero_data 

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert 'vendor_i_d' in output.columns, 'Vendor_ID is missing'
@test
def test_output(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'
@test
def test_output(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum()== 0, 'There are rides with zero trip distance'