import matplotlib.pyplot as plt


def linear_reg_simple_plot(x_scatter, y_scatter, x_plot, y_plot, color_scatter, label_text):
    plt.scatter(x_scatter, y_scatter, color=color_scatter, label=label_text)
    plt.plot(x_plot, y_plot, color='black', label='Predict')
    plt.title('Salario vs Años de experiencia')
    plt.xlabel('Experiencia')
    plt.ylabel('Salario')
    plt.legend()
    plt.show()