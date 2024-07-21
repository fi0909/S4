import unittest
import remilis_login as remilis_login
import random as rd
import string
class TestStringMethods(unittest.TestCase):
    #blackbox test
    def random_generator(self,size=6, chars=string.ascii_uppercase + string.digits+string.ascii_lowercase):
        return ''.join(rd.choice(chars) for _ in range(size))
    def test_login(self):
        result = remilis_login.login("ibu maya","123")
        self.assertIn('active',result)
    def test_login_false(self):
        result = remilis_login.login("ibu maya","111")
        self.assertNotIn('active',result)
    def test_register(self): 
        nama= self.random_generator()
        email = (self.random_generator()+'@gmail.com')
        pw = self.random_generator()
        self.assertTrue(remilis_login.register(nama,email,pw))
    def test_register_false(self):
        conn = remilis_login.connection_database()
        cursor = conn.cursor()
        cursor.execute("select nama,gmail,sandi from user")
        data = cursor.fetchone()
        self.assertFalse(remilis_login.register(data[0],data[1],data[2]))

if __name__ == "__main__":
    unittest.main()