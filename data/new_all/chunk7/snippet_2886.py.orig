#Source: https://stackoverflow.com/questions/59774035/attributeerror-tensor-object-has-no-attribute-numpy
DATADIR = r"C:\Users\angesu\Desktop\DOCUMENT_DATA"

CATEGORIES = ["resume","transcript","certificate"]
IMG_SIZE = 250

for category in CATEGORIES :
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)

training_data = []
def create_training_data():
    for category in CATEGORIES :
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try :
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass
create_training_data()
random.shuffle(training_data)

X = [] #features
y = [] #labels
for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.asarray(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

clf = ak.ImageClassifier(max_trials=10)
clf.fit(X,y,validation_split=0.1)

def prepare(file):
    IMG_SIZE = 250
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

path = r"C:\Users\angesu\Downloads\Garn-Certificate-4.jpg"

predicted_y = clf.predict(prepare(path))

print(clf.evaluate(test_set))