import argparse

def outputLandmarks(landmarks):
    
    if landmarks:
        print('Landmarks found: \n')
        for landmark in landmarks:
            print(landmark.description)
    else:
        print('No landmarks found :(')

def identifyLandmarkLocal(path):
    from google.cloud import vision_client
    visionClient = vision.Client()
    with io.open(path, 'rb') as imageFile:
        content = imageFile.read()

    image = visionClient.image(content=content)
    return image.detect_landmarks


def identifyLandmark(cloudUri):
    from google.cloud import vision 

    print('Connecting to api...')
    visionClient = vision.Client()

    print('Processing image source ' + cloudUri + ' ...')
    image = visionClient.image(source_uri=cloudUri)

    return image.detect_landmarks()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Identifies the landmark in the given image.')
    parser.add_argument(
        'gcs_uri', help=('The Google Cloud Storage uri to the image to identify'
                         ', of the form: gs://bucket_name/object_name.jpg'))
    args = parser.parse_args()

    outputLandmarks(identifyLandmark(args.gcs_uri)) 

