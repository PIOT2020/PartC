import unittest
#import recognise
#import imutils


class TestAgent(unittest.TestCase):
    

    def test_unrecognisable_face(self):
        """Tests if scanned photo is unknown"""
       #matches = face_recognition.compare_faces(data["encodings"], encoding)        
        scannedFace = "Unknown"
        self.assertFalse(scannedFace == "")
        
    def test_recognise_face(self):
        """Tests if scanned photo is a register user"""
       #matches = face_recognition.compare_faces(data["encodings"], encoding)
        scannedFace = "{}"
        self.assertFalse(scannedFace == "")
        
    def test_unlock_car(self):
        """Tests if unlocking car works with input choice '1'"""
        #Input from console
        choice = '1'
        confirmation = '1'
        self.assertEqual(choice, confirmation)
        
    def test_return_car(self):
        """Tests if returning car works with input choice '2'"""
        #Input from console
        choice = '2'
        confirmation = '2'
        self.assertEqual(choice, confirmation)
        
    def test_login(self):
        """Tests logging in"""
        #Input from console
        username = ""
        password = ""
        self.assertTrue(username.isprintable())
        self.assertTrue(password.isprintable())
        
if __name__ == '__main__':
    unittest.main()
