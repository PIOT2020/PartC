# PartC

We don't have a webcam so for validation you'd need to upload a variety of photos of your face into a folder named after yourself.

Then run encode.py which'll scan the photos and create the file 'encodings.pickle' which holds the newly scanned photos.

Then to verify yourself you need to upload a new photo in the same directory as encode.py, rename it to 'search.jpg' and run recognise.py.

This'll then scan the new photo and verify if it is you or not.

For the demonstration, we have pre loaded and encoded photos of 4 celebrities.