
class Derivacion:
    """Clase para realizar operaciones relacionadas con derivadas."""

    def derivada_numerica(self, funcion, x, h=0.00005):
        """
        Calcula la derivada de una funcion utilizando diferencias centrales.

        Parameters
        ----------
        funcion : callable
            Funcion cuya derivada se desea calcular.
        x : float
            Punto donde se calcula la derivada.
        h : float
            Incremento utilizado para aproximar la derivada.

        Returns
        -------
        float
            Aproximacion numerica de la derivada 
        """
        return (funcion(x + h) - funcion(x - h)) / (2 * h)