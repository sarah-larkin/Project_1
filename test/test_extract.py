from src.lambda_handler.extract import extract_lambda_hander

def test_lambda_handler(): 
    assert extract_lambda_hander() == 1

#mock with moto 