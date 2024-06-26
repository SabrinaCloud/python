import pytest
from water_flow import pressure_loss_from_fittings, pressure_loss_from_pipe_reduction, reynolds_number, reynolds_number, water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
def test_water_column_height():
    #test cases
    test_cases=[
        (0.0,0.0,0.0),
        (0.0,10.0,7.5),
        (25.0,0.0,25.0),
        (48.3,12.8,57.9)
    ]
#Iterate through test cases
    for tower_height, tank_height, expected_height in test_cases:
        assert water_column_height(tower_height, tank_height)==pytest.approx(expected_height,rel=1e-6)

def test_pressure_gain_from_water_height():
    #Test cases
    test_cases=[
        (0.0,0.000,0.001),
        (30.2,295.628,0.001),
        (50.0,489.450,0.001)
    ]
#Iterate through test cases
    for height, expected_pressure, tolerance in test_cases:
        assert pressure_gain_from_water_height(height)==pytest.approx(expected_pressure, abs=tolerance)

def test_pressure_loss_from_pipe():
    #Test cases
    test_cases=[
        (0.048692,0.00,0.018,1.75,0.00,0.001),
        (0.048692,200.00,0.000,1.75,0.000,0.001),
        (0.048692,200.00,0.018,0.00,0.000,0.001),
        (0.048692,200.00,0.018,1.75,-113.008,0.001),
        (0.048692,200.00,0.018,1.65,-100.462,0.001),
        (0.286870,1000.00,0.013,1.65,-61.576,0.001),
        (0.286870,1800.75,0.013,1.65,-110.884,0.001)
    ]
#Iterate through test cases
    for diameter,length, friction_factor, velocity, expected_loss, tolerance in test_cases:
        assert pressure_loss_from_pipe(diameter, length, friction_factor, velocity)==pytest.approx(expected_loss, abs=tolerance)

def test_pressure_loss_from_fittings():
    test_cases=[
        (0.00,3,0.000,0.001),
        (1.65,0,0.000,0.001),
        (1.65,2,-.109,0.001),
        (1.75,2,-0.122,0.001),
        (1.75,5,-0.306,0.001),
    ]
    for velocity, fittings, expected_loss, tolerance in test_cases:
        assert pressure_loss_from_fittings(velocity,fittings)==pytest.approx(expected_loss, abs=tolerance)

def test_reynolds_number():
    test_cases=[
        (0.048692,0.00,0,1),
        (0.048692,1.65,80069,1),
        (0.048692,1.75,84922,1),
        (0.048692,1.65,471729,1),
        (0.048692,1.75,500318,1),
    ]
    for diameter, velocity, expected_reynolds, tolerance in test_cases:
        assert reynolds_number(diameter,velocity)==pytest.approx(expected_reynolds, abs=tolerance)

def test_pressure_loss_from_pipe_reduction():
    test_cases=[
        (0.28687,0.00,1,0.048692,0.00,0.001),
        (0.28687,1.65,471729,0.048692,-163.744,0.001),
        (0.28687,1.75,500318,0.048692,-184.182,0.001),
    ]
    for larger_diameter, velocity, reynolds, smaller_diameter, expected_loss, tolerance in test_cases:
        assert pressure_loss_from_pipe_reduction(larger_diameter,velocity,reynolds, smaller_diameter)==pytest.approx(expected_loss, abs=tolerance)

#Main function to execute the test functions with pytest
if __name__=="__main__":
    pytest.main(["-v","--tb=line","-rN", __file__])