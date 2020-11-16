def get_manhattan_plot(df,significance_column):
    
    df['minuslog10pvalue'] = -np.log10(df[significance_column])
    df = df.sort_values('CHR')
    df['ind'] = range(len(df))
    df_grouped = df.groupby(('CHR'))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    colors = ['red','green']

    x_labels = []
    x_labels_pos = []
    for num, (name, group) in enumerate(df_grouped):
        group.plot(kind='scatter', x='ind', y='minuslog10pvalue',color=colors[num % len(colors)], ax=ax)
        x_labels.append(name)
        x_labels_pos.append((group['ind'].iloc[-1] - (group['ind'].iloc[-1] - group['ind'].iloc[0])/2))

    yline = -np.log10(0.05)
    ax.axhline(yline, linestyle='--', color='k')
    ax.set_xticks([x_labels_pos[0],x_labels_pos[-1]])
    ax.set_xticklabels([x_labels[0],x_labels[-1]])
    ax.set_ylabel('$- log_{10}(P)$')
    ax.set_xlabel('Chromosome')
    plt.title('Manhattan Plot');
    return