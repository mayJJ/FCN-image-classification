import matplotlib.pyplot as plt
import pandas as pd


def show_train_history(train_history,train,validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()
    
# show_train_history(train_history,'acc','val_acc')
# show_train_history(train_history,'loss','val_loss')

def plot_images_labels_prediction(images,labels,prediction,
                                  idx,num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num>25: num=25 
    for i in range(0, num):
        ax=plt.subplot(5,5, 1+i)
        ax.imshow(images[idx], cmap='binary')

        ax.set_title("label=" +str(labels[idx])+
                     ",predict="+str(prediction[idx])
                     ,fontsize=10) 
        
        ax.set_xticks([]);ax.set_yticks([])        
        idx+=1 
    plt.show()
    
# plot_images_labels_prediction(x_test_image,y_test_label, prediction,idx=340)

# def plot_confusion matrix_mnist(y_test_label, prediction):
#     pd.crosstab(y_test_label,prediction, rownames=['label'],colnames=['predict'])