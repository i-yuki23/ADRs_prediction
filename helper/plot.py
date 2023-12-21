from matplotlib import pyplot as plt

# Plotting the ROC curve
def plot_roc_curve(fpr, tpr, thresholds):
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='blue', lw=2, label='ROC curve')
    plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')

    # Adding annotations for thresholds
    # for i, txt in enumerate(thresholds):
    #     plt.annotate(f'{txt}', (fpr[i], tpr[i]), textcoords="offset points", xytext=(10,-10), ha='center')

    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.show()