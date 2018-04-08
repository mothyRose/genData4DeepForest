import numpy as np
PATH='D:\\Users\\mothyRose\\Desktop\\github\\data.npz'
def get_data(path=PATH):
        f = np.load(path)
        x_train, y_train = f['x_train'], f['y_train']
        x_test, y_test = f['x_test'], f['y_test']
        f.close()
        return (x_train,y_train),(x_test,y_test)
(x,y),(xt,yt)=get_data()
