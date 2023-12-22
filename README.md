### Process :
1. Receive user ingredients input (Array of string of ingredients).
2. Filter recipes, compare the recipes' ingredients with user input.
3. Put the filtered recipes into the Ranking Model.
4. Send back the sorted recipes to App.

### Summary :
The prototype model use two tower model, with user embedding and recipes embedding. The results are predicted rating based on user rating history.
The RMSE hasn't been optimized so it's pretty high for now around 1.9 for the test. Then the model exported as .tflite and we use flask to make API for the processing.  

![image](https://github.com/CookNow-Bangkit2023/Machine-Learning/assets/93307670/467c9404-4ac7-4813-877f-c5af0ce7b3c0)

### Model Specification
* Python 3.8
* Tensorflow
* Tensorflow_Lite
* Tensorflow_recommenders
* Numpy
* Pandas
