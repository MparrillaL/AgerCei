
class GenderError(Exception):
    """
    Invalid Gender format. ["M" , "H"]
    """
class ActivityError(Exception):
    """
    Invalid Activity format. ["Sedentario", "Poco activo", "Activo con moderacion", "Activo", "Muy activo"]
    """
class FormError(Exception):
    """
    Something was wrong with the patient form, check data.
    """
class InvalidNameError(Exception):
    """Excepción personalizada para errores en el nombre o apellido."""