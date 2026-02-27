import matplotlib.pyplot as plt


def plot_top(snap_data, ds1, ds2, ds3):

    styles = plt.style.available
    plt.style.use(styles[14])
    fig, ax = plt.subplots(figsize=(9, 7))
    plt.xticks(rotation=90)

    ax.set_ylabel('Cantidad de casos', fontsize=16)
    ax.set_title("Top paises estadisticas Covid-19", fontsize=20)
    ax.tick_params(axis="x", labelsize=14)
    ax.tick_params(axis="y", labelsize=0)

    width = 0.5
    x = snap_data['Country/Region']

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 0),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=10)

    rec1 = ax.bar(x, ds1, width, color='#3da5ff')
    rec2 = ax.bar(x, ds2, width, color='#49cc4c')
    rec3 = ax.bar(x, ds3, width, color='#f44336')

    autolabel(rec1)
    autolabel(rec2)
    autolabel(rec3)

    fig.tight_layout()
    plt.legend(['Confirmados', 'Recuperados', 'Muertos'], fontsize='medium')
    fig.savefig('app/static/img/top10.png')


def plot_arg(df):
    styles = plt.style.available
    plt.style.use(styles[14])
    fig, ax = plt.subplots(figsize=(25, 15))

    ax.set_ylabel('Cantidad de casos', fontsize=16)
    ax.set_title("Argentina", fontsize=35)

    ax.tick_params(axis="x", labelsize=20)
    ax.tick_params(axis="y", labelsize=20)

    for i in df.columns[:3]:
        ax.plot(df['Date'], df[i], label=i)
        ax.scatter(df['Date'], df[i])
        ax.text(df['Date'].iloc[-1],
                df[i].iloc[-1],
                df[i].iloc[-1],
                fontsize=25,
                ha='right')

    ax.legend(fontsize='xx-large')

    fig.savefig('app/static/img/arg.png')
