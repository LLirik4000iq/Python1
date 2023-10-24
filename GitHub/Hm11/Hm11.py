from intellect import RecognizeImg

path = 'Cat.jpg'
winName = 'cat'
fileName = 'haarcascade_frontalcatface_extended.xml'

rec = RecognizeImg(path)
rec.GetCoordinates(fileName)


newPath = 'glasses.png'
newPhotoPath = 'cat_with_glasses.png'
rec.AddImage(newPath, newPhotoPath)
rec.ShowImg('AddImage Cat')