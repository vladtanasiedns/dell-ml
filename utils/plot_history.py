import matplotlib.pyplot as plt

def plot_history(history):
  fig, ax = plt.subplots(1,2, figsize=(25, 10))

  ax[0].plot(history.history['loss'], marker='o', label='loss')
  ax[0].plot(history.history['val_loss'], marker='o', label='val_loss')
  ax[0].set_title("Loss")
  ax[0].legend()

  ax[1].plot(history.history['accuracy'], marker='o', label='accuracy')
  ax[1].plot(history.history['val_accuracy'], marker='o', label='val_accuracy')
  ax[1].set_title("Validation accuracy")
  ax[1].legend()