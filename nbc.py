from pyvi import ViTokenizer
from sklearn import naive_bayes # thư viện NLP tiếng Việt
from tqdm import tqdm
import numpy as np
import gensim # thư viện NLP
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# chuẩn hoá dữ liệu
def clean_text(text):
    text = gensim.utils.simple_preprocess(text) # chuyển văn bản thành list các token (chữ thường, bỏ dấu câu, )
    text = ' '.join(text)
    text = ViTokenizer.tokenize(text) # tách các từ tiếng việt (vd: bắt đầu kinh doanh -> bắt_đầu kinh_doanh)
    return text

# def get_data():
#     dir_path = os.path.dirname(os.path.realpath(os.getcwd())) # lấy path directory chứa project
#     dir_path = os.path.join(dir_path, 'New Data') # đường dẫn đến folder New Data
#     train_path = os.path.join(dir_path, 'VNTC-master/Data/10Topics/Ver1.1/Train_Full') # đường dẫn đến folder train_full
#     X = []
#     y = []
#     dirs = os.listdir(train_path)  # list tên các label trong folder train_full
#     for path in tqdm(dirs):
#         file_paths = os.listdir(os.path.join(train_path, path)) # lấy list các file trong từng label
#         for file_path in tqdm(file_paths): # duyệt từng file
#             with open(os.path.join(train_path, path, file_path), 'r', encoding="utf-16") as f:
#                 lines = f.readlines()
#                 lines = ' '.join(lines)
#                 lines = clean_text(lines)

#                 X.append(lines) # thêm văn bản đã xử lý vào mảng X
#                 y.append(path)  # thêm nhãn văn bản vào mảng Y

#     pickle.dump(X, open('data/X_data.pkl', 'wb')) # lưu dữ liệu X vào file X_data.pkl
#     pickle.dump(y, open('data/y_data.pkl', 'wb')) # lưu dữ liệu y vào file y_data.pkl
#     return X, y


# def train_classifier(X, y):
#     # chia X làm 2 phần: 90% train và 10% test
#     # tham số random_state để 2 tập dữ liệu train và test từ X và Y ko bị thay đổi mỗi lần chạy lại
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

#     # thực hiện tính toán trên từng từ riêng lẻ
#     # token_pattern: định nghĩa token
#     #  \w: match [a-zA-Z0-9_], các dấu khác bị loại bỏ 
#     vectorizer = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')

#     # chuyển dữ liệu về dạng count vector
#     X_count = vectorizer.fit_transform(X_train)
#     X_test_count = vectorizer.transform(X_test)

#     # sử dụng mô hình naive bayes dạng multinomialNB
#     naive_bayes_classifer = naive_bayes.MultinomialNB().fit(X_count, y_train)

#     # sử dụng mô hình vừa train để xây dựng tập kết quả dự đoán trên tập test
#     test_prediction = naive_bayes_classifer.predict(X_test_count)
#     # so sánh kết quả với tập y_test
#     print('Test accuracy: ', accuracy_score(test_prediction, y_test))

#     # lưu lại model và vectorizer vào file pickle
#     pickle.dump(naive_bayes_classifer, open('data/naive_bayes_classifer.pkl', 'wb'))
#     pickle.dump(vectorizer, open('data/count_vectorizer.pkl', 'wb'))

# dự đoán nhãn dựa trên dữ liệu text đầu vào
def classify(text):
    # load model và vectorizer
    clf = pickle.load(open('data/naive_bayes_classifer.pkl', 'rb'))
    vectorizer = pickle.load(open('data/count_vectorizer.pkl', 'rb'))
    # dự đoán trên text
    pred = clf.predict(vectorizer.transform([text]))
    return pred[0]