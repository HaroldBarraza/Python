from pytest import approx
import pytest
def test_water_column_height():
    pytest.approx (0, 0) == 0.0
    pytest.approx (0, 10) == 7.5
    pytest.approx (25, 0) == 25.0
    pytest.approx (48.3, 12.8) == 57.9
#=============================================================================================================
def test_pressure_gain_from_water_height():
    pytest.approx (0) == 0
    pytest.approx (30.2) == 295.628
    pytest.approx (50) == 489.450
#=============================================================================================================
def test_pressure_loss_from_pipe():
    pytest.approx (0.048692, 0, 0.018, 1.75) == 0
    pytest.approx (0.048692, 200, 0, 1.75) == 0
    pytest.approx (0.048692, 200, 0.018, 0) == 0
    pytest.approx (0.048692, 200, 0.018, 1.75) == -113.008
    pytest.approx (0.048692, 200, 0.018, 1.65) == -100.462
    pytest.approx (0.28687, 1000, 0.013, 1.65) == -61.576
    pytest.approx (0.28687, 1800.75, 0.013, 1.65) == -110.884
#=============================================================================================================
def test_pressure_loss_from_fittings():
    pytest.approx (0, 3) == 0.0
    pytest.approx (1.65, 0) == 0.0
    pytest.approx (1.65, 2) == -0.109
    pytest.approx (1.75, 2) == -0.122
    pytest.approx (1.75, 5) == -0.306
#=============================================================================================================
def test_reynolds_number():
    pytest.approx (0.048692, 0) == 0.0
    pytest.approx (0.048692, 1.65) == 80069
    pytest.approx (0.048692, 1.75) == 84922
    pytest.approx (0.28687, 1.65) == 471729
    pytest.approx (0.28687, 1.75) == 500318
#=============================================================================================================
def test_pressure_loss_from_pipe_reduction():
    pytest.approx (0.28687, 0, 1, 0.048692) == 0
    pytest.approx (0.28687, 1.65, 471729, 0.048692) == -163.744
    pytest.approx (0.28687, 1.75, 500318, 0.048692) == -184.182
#=============================================================================================================
pytest.main(["-v", "--tb=line", "-rN", __file__])