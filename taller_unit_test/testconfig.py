# coding: utf-8
"""
Módulo para configuración de tests
"""
from mock import patch
from django.test.runner import DiscoverRunner


class NoDBRunner(DiscoverRunner):
    """Test runner sin base de datos para tests unitarios"""

    def setup_databases(self, *args, **kwargs):
        """
        Sobreescribimos el comportamiento de DiscoverRunner
        para no inicializar la bdd
        """
        self._db_patch = patch('django.db.backends.utils.CursorWrapper')
        self._db_mock = self._db_patch.start()
        self._db_mock.side_effect = RuntimeError(
            'Tests con base de datos no permitidos!'
        )
        return None

    def teardown_databases(self, *args, **kwargs):
        """
        Sobreescribimos el comportamiento de DiscoverRunner
        ya que no hay que desmontar ninguna bdd
        """
        self._db_patch.stop()
        return None


class LiveDBRunner(DiscoverRunner):
    u"""
    Con este runner evitamos crear la base de datos de test y
    utilizamos la base de datos local
    """

    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, *args, **kwargs):
        pass
