from calculator_core import soma, subtracao, multiplicacao, divisao, exponenciacao, radiciacao

def test_soma():
    assert soma(1,1) == 2

def test_subtracao():
    assert subtracao(2,2) == 0

def test_multiplicacao():
    assert multiplicacao(3,3) == 9

def test_divisao():
    assert divisao(4, 2) == 2

def test_exponenciacao():
    assert exponenciacao(5, 4) == 625

def test_radiciacao():
    assert radiciacao(81, 2) == 9