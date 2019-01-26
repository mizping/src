from sklearn import datasets
from sklearn import svm, metrics
import matplotlib.pyplot as plt

# 手書き数字データセットを読み込む
digits = datasets.load_digits()
X = digits.data		# 手書き数字データ
Y = digits.target	# ターゲット
n_train = len(X) * 2 // 3	# データの2/3

# 訓練データ
X_train, Y_train = X[:n_train], Y[:n_train]		# 前半2/3
# テストデータ
X_test, Y_test = X[n_train:], Y[n_train:]			# 後半1/3

# 学習器の作成と学習
clf = svm.SVC(gamma=0.001)	# 学習器
clf.fit(X_train, Y_train)	# 訓練データと教師データで学習する

# モデルの学習結果を評価する
accuracy = clf.score(X_test, Y_test)	# テストデータで試す
print(f"正答率{accuracy}")
predicted = clf.predict(X_test)		# テストデータの分類結果
n_error = (Y_test != predicted).sum()	# 正解と分類結果を比較する
print(f"誤った個数 {n_error}")

# 詳しいレポート
print("classification report")
print(metrics.classification_report(Y_test, predicted))
print("confusion matrix")
print(metrics.confusion_matrix(Y_test, predicted))

# 画像イメージと分類
imgs_yt_preds = list(zip(digits.images[n_train:], Y_test, predicted))
for index, (image, y_t, pred) in enumerate(imgs_yt_preds[404:416]):
    plt.subplot(3, 4, index + 1)
    plt.axis("off")
    plt.tight_layout()
    plt.imshow(image, cmap="Greys", interpolation="nearest")
    plt.title(f"t:{y_t}  pre:{pred}", fontsize=12)
plt.show()

