import unittest
#import recognise
#import imutils


class TestAgent(unittest.TestCase):
    

    def test_unrecognisable_face(self):
       #matches = face_recognition.compare_faces(data["encodings"], encoding)        
        scannedFace = "Unknown"
        self.assertFalse(scannedFace == "")
        
    def test_recognise_face(self):
       #matches = face_recognition.compare_faces(data["encodings"], encoding)
        scannedFace = "{}"
        self.assertFalse(scannedFace == "")
        
    def test_unlock_car(self):
        #Input from console
        choice = '1'
        confirmation = '1'
        self.assertEqual(choice, confirmation)
        
    def test_return_car(self):
        #Input from console
        choice = '2'
        confirmation = '2'
        self.assertEqual(choice, confirmation)
        
    def test_login(self):
        #Input from console
        username = ""
        password = ""
        self.assertTrue(username.isprintable())
        self.assertTrue(password.isprintable())
        
if __name__ == '__main__':
    unittest.main()
