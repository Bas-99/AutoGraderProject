# https://www.tensorflow.org/install/gpu
from tensorflow.keras.models import load_model
from OldFiles.Converting_Data_prod1 import X, classes
import numpy as np

model_path = 'C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\saved_ML_models\\model_1_pickup'

new_model = load_model(model_path, compile=True)

# new_model.summary()
# loss, acc = new_model.evaluate(X, Y, verbose=2)
# print('Restored model, accuracy: {:5.2f}%'.format(100 * acc))
# print(new_model.predict(X).shape)

score = 0
for i in range(len(X)):
    samples_to_predict = []
    samples_to_predict.append(X[i])
    samples_to_predict = np.array(samples_to_predict)

    predictions = new_model.predict(samples_to_predict)
    classif = np.argmax(predictions, axis=1)

    binary = classes[classif[0]]
    print(predictions)
    if binary == "correct":
        score += 1

finalScore = score/len(X)
print("Average score for picking product 1: "+str(finalScore)+" (maximum of 1.0)")


