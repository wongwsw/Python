def prepare_dfs(group):
    path = group + r'*hr.out'
    files = glob.glob(path)
    dfs_list = []
    for i in files:
        header = i.split(".size")[0]
        smaple_prefix, idx =header.split("_")
        #timepoint = int(timepoint[:-3])
        #df_i = pd.read_csv(i, sep="\t")
        df_i = pd.read_csv(i,sep="\t",nrows=1, index_col=0)
        df_i['Sample'] = df_i.index.str.split(":").str[0]
        df_i = df_i.set_index("Sample")
        dfs_list.append(df_i)

    dfs = pd.concat(dfs_list)
    dfs = dfs.sort_index()
    #dfs = dfs.rename(columns = {'#size':'Size','percentage':'Frequency'})
    return dfs
