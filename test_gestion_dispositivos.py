import unittest
from gestion_dispositivos import agregar_dis, listar_dis  

class TestGestionDispositivos(unittest.TestCase):
    def test_agregar(self):
        response = agregar_dis({"name": "Switch", "job": "Core"})
        self.assertEqual(response.status_code, 201)

    def test_listar(self):
        response = listar_dis()
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
