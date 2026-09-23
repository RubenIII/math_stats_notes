import numpy as np

from math_utils.derivacion import Derivacion

def test_derivada_seno_en_cero():
    derivador = Derivacion()

    resultado = derivador.derivada_numerica(
        np.sin,
        0
    )

    assert np.isclose(resultado, 1.0)


def test_derivada_seno_en_pi():
    derivador = Derivacion()

    resultado = derivador.derivada_numerica(
        np.sin,
        np.pi
    )

    assert np.isclose(resultado, -1.0)


def test_derivada_coseno_en_cero():
    derivador = Derivacion()

    resultado = derivador.derivada_numerica(
        np.cos,
        0
    )

    assert np.isclose(resultado, 0.0)