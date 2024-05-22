import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.ticker import MaxNLocator

def create_barplot(df, 
                   categories, 
                   columns, 
                   colors,
                   category_type=None,
                   rotation_xtick_label=None, 
                   position_xtick_label=None,
                   set_xlabel=True, 
                   set_xticks=True, 
                   set_ylabel_percentage=False, 
                   yaxis_by_thousands=False,
                   as_percentage_total=False, 
                   as_percentage_category=False, 
                   bar_perc_annotation=False, 
                   figure_title=False, 
                   rotate_xticks=False, 
                   vline_between_cat=False, 
                   put_number_on_top_bar=False, 
                   space_between_cat=0.0, 
                   space_between_bars=0.0,
                   yaxis_label=None,
                   fontsize_text_bars=12,
                   v_adjust_bars=0.01,
                   rotate_text_90=False,
                   **kwargs):
    """"
    General purpose function to create barplot
 
    In df, the categories are in the index, and the values are in the column
    If columns is a list of len >2, then the function will create a grouped barplot
    """
 
    plt.rcParams["font.family"] = "Avenir"
 
    # create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
 
    # select the categories, based on 'Categorie' column
    df_cat = df.loc[categories, : ]
 
    # get the number of categories
    n_cat = len(categories)
 
    # start by selecting the data
    data = df_cat[columns]
    xbar_loc_ls = []

    # get the number of columns
    n_col = len(data.columns)

    # check the shape of the data - if needed a new axis
    if len(data.shape) == 1:
        data = data[:, np.newaxis]
    # if as_percentage_total, then get total of all columns
    if as_percentage_category:
        # sum the data
        total = data.sum(axis=1)
        data = data.div(total, axis=0)
    if as_percentage_total:
        total = df.loc[categories, 'Totaal']
        
        # check if series, then convert to dataframe - then sum
        if isinstance(total, pd.Series):
            total = total.sum()
            data = data/total
        else:
            total = total.sum(axis=1)
            data = data.div(total, axis=0)
 
    # if columns is a list of len >=2, then create a grouped barplot
    if len(columns) == 1:
 
        # get the index
        x_value = np.arange(len(data))
 
        if data.shape[1] == 1:
            data = data.squeeze()
 
        # create the bars
        ax.bar(ind, data, color=colors[0])

        if put_number_on_top_bar:
            for i, v in enumerate(data):
                if set_ylabel_percentage:
                    text = str(round(v*100, 1)) + '%'
                else: 
                    text = str(round(v, 1))
                if rotate_text_90:
                    rotation = 90
                else:
                    rotation = 0
                ax.text(i, v + v_adjust_bars, text, ha='center', va='bottom', fontsize=fontsize_text_bars, rotation=rotation)
    
    else:
 
        # # get the width of each bar
        width = (1 / n_col) 
 
        # get the index
        ind = np.arange(len(data))
 
        # create the bars
        xbar_loc_ls = []
        i_per_cat = list(range(0, len(categories)))
        for i, col in enumerate(data.columns):

            # set the x-value
            x_value = ind + i * (width)

            # Add space between categories
            x_value = x_value + (space_between_cat* np.array(i_per_cat))

            # Add space between the bars
            if space_between_bars > 0:
                x_value = x_value + (i * space_between_bars) 
                x_value = x_value + (space_between_bars*n_col*np.array(i_per_cat))
                
            # append the x_value to xbar_loc_ls
            xbar_loc_ls.append(x_value[0])

            # set the y-value
            y_value = data[col]
            
            # create the bars
            ax.bar(x_value, y_value, label=col, color=colors[i], width=0.8*width)

            if put_number_on_top_bar:
                for i, v in enumerate(y_value):
                    if set_ylabel_percentage:
                        text = str(round(v*100, 1)) + '%'
                    else: 
                        text = str(round(v,1))

                    # if rotate_text_90, then rotate the text
                    if rotate_text_90:
                        rotation = 90
                    else:
                        rotation = 0
                    ax.text(x_value[i], v + v_adjust_bars, text, ha='center', va='bottom', fontsize=fontsize_text_bars, rotation=rotation)

    # add the patterns to the bars
    if 'fill_patterns' in kwargs:
        fill_patterns = kwargs['fill_patterns']

        # change the hatch color
        plt.rcParams['hatch.color'] = 'white'

        # the first bar needs the first pattern, the second bar needs the second pattern, etc.
        bars = ax.patches
        fill_patterns_per_bar =  fill_patterns * (n_cat + (n_col-1))
        i = 0
        for bar in bars:
            bar.set_hatch(fill_patterns_per_bar[i])
            i += 1 
    
    # set x-ticks
    if set_xticks:
        # set xticks - adjust for number of columns
        if len(categories) == 1:
            
            # xticks x-coordinates
            custom_xticks = xbar_loc_ls
            ax.set_xticks(custom_xticks)

            # xticks labels
            if 'custom_xticks' in kwargs:
                custom_xticks = kwargs['custom_xticks']
                custom_labels = custom_xticks
            else:
                custom_labels = columns
            ax.set_xticklabels(custom_labels, rotation=rotation_xtick_label, ha=position_xtick_label)

        elif len(columns) > 1:
            # x-ticks x-coordinates
            total_space_cols = (width) * n_col
            xtick_locs = np.arange(len(data)) + ((total_space_cols / 2)- width/2)

            # add space between categories
            x_tick_locs = xtick_locs + (space_between_cat * np.array(i_per_cat))

            # add space between bars
            if space_between_bars > 0:
                space_between_bars_per_cat = (space_between_bars * (n_col))
                x_tick_locs = x_tick_locs + (space_between_bars_per_cat * np.array(i_per_cat))  + (space_between_bars*2)
            
            # set custom xticks if available
            if 'custom_xticks' in kwargs:
                xticks = kwargs['custom_xticks']
            else:
                xticks = category_xticks
            ax.set_xticks(x_tick_locs, xticks)
                
          
        else:
            ax.set_xticks([])
 
    else:
        ax.set_xticks([])
 
    # set x-axis label and title
    if category_type is not None and set_xlabel:
        # if contains a :, then split it and use the first part
        if ':' in category_type:
            xlabel = category_type.split(':')[0]
        else:
            xlabel = category_type
    else:
        xlabel = None

    # set x-axis label
    ax.set_xlabel(xlabel, fontsize=16)

    # set y-axis ticks labels
    if yaxis_by_thousands is not False:
        if 'ylim' in kwargs and 'n_yticks' in kwargs:
            ylim = kwargs['ylim']
            n_yticks = kwargs['n_yticks']
            if 'yaxis_small' in kwargs:
                custom_yticks = ["{:.0f}".format(x) for x in np.linspace(0,ylim,n_yticks)]
            else:
                custom_yticks = ["{:.0f}".format(x/1000) for x in np.linspace(0,ylim,n_yticks)]
            ax.yaxis.set_major_locator(MaxNLocator(n_yticks))
            ax.set_yticklabels(custom_yticks)
            ax.set_ylim(0,ylim)
        else:
            ytick_labels = ["{:.0f}".format(x/1000) for x in ax.get_yticks()]
            ax.set_yticklabels(ytick_labels)
    else:
        pass

    # turn the y-axis to percentage
    if set_ylabel_percentage:
        if 'n_yticks' in kwargs and 'ylim' in kwargs:
            n_yticks = kwargs['n_yticks']
            ylim = kwargs['ylim']
            custom_yticks = [f'{a:.0f}%' for a in np.linspace(0,100,n_yticks)]
            ax.yaxis.set_major_locator(MaxNLocator(n_yticks))
            ax.set_yticklabels(custom_yticks)
            ax.set_ylim(0,ylim)
        else:
            ax.set_yticklabels(['{:.0f}%'.format(x) for x in ax.get_yticks()])
 
    # if not none, remove the category_type string from the categories
    if category_type is not None:
        # remove the category_type from the categories
        category_xticks = [cat.replace(category_type, '').strip() for cat in categories]
        # capitalize the first letter
        category_xticks = [cat.capitalize() for cat in category_xticks]
    else:
        category_xticks = categories   

    # set y-axis label
    if 'set_ylabel' in kwargs:
        yaxis_label = kwargs['set_ylabel']
        ax.set_ylabel(yaxis_label, fontsize=16)
    else:
        pass

    # annotation percentages on top bar chart
    if bar_perc_annotation is not False:
        for i in range(0,data.shape[1]):
            column = data.columns[i]
            x_coord = xbar_loc_ls[i]
            y_coord = data[column].values[0]
            value = y_coord/data.iloc[0,:].values.sum()*100
            ax.text(x_coord, y_coord, '{:.1f}%'.format(value), ha='center', va='bottom', fontsize=fontsize_text_bars, color=colors[i], weight='bold')
    else:
        pass

    # set figure_title
    if figure_title is not False:
        # get height
        if 'y_title' in kwargs:
            y_coord = kwargs['y_title']
            fig.suptitle(figure_title, fontsize=20, y=y_coord)  
        else:
            fig.suptitle(figure_title, fontsize=20, y=1.05)  
    else:
        pass

    # if vline_between_cat, then add a vertical line between categories
    if vline_between_cat:
        n_cat = len(categories)
        
        for i in range(1, n_cat):
            # define space taken per cat - depends on number of columns
            space_per_cat = (width * n_col)
            space_between_bars_per_cat = (space_between_bars * n_col)
            x_loc_vline = (i*(space_per_cat+space_between_bars_per_cat+space_between_cat))- (width/2)- (space_between_cat/2)
            ax.axvline(x=x_loc_vline , color='black', linewidth=0.5)
   
 
    return data, fig, ax


# function to create 2D heatmap - takes in matrix with values, row and column names, title, and color map
def create_2d_heatmap(df,
                      matrix, 
                      row_names,
                      col_names,
                      figure_title=None,
                      cmap='viridis',
                      label_as_percentage=False,
                      fontsize_labels=16,
                      **kwargs):
    """"
    General purpose function to create heatmap plots
 
    """

    # set the font family
    plt.rcParams["font.family"] = "Avenir"

    # create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))

    # create heatmap
    cax = ax.matshow(matrix, cmap=cmap)

    # set labels
    ax.set_xticks(np.arange(len(col_names)))
    ax.set_yticks(np.arange(len(row_names)))
    ax.set_xticklabels(col_names)
    ax.set_yticklabels(row_names)

    # Rotate the tick labels and set their alignment.
    if 'rotation' in kwargs:
        rotation = kwargs['rotation']
    else:
        rotation = 0
    plt.setp(ax.get_xticklabels(), rotation=rotation, ha="center", rotation_mode="anchor", size=fontsize_labels)
    plt.setp(ax.get_yticklabels(), rotation=rotation, ha="right", rotation_mode="anchor", size=fontsize_labels)

    # set the title
    if figure_title is not False:
            if 'y_pos' in kwargs:
                y_pos = kwargs['y_pos']
                fig.suptitle(figure_title, fontsize=20, y=y_pos)  
            else:
                fig.suptitle(figure_title, fontsize=20, y=0.95)  
    else:
        pass

    # show the values in matrix in the heatmap
    for i in range(len(row_names)):
        for j in range(len(col_names)):
            # create text here
            value_to_show = matrix[i, j]
            if label_as_percentage:
                value_to_show = f'{value_to_show:.1f}%'
            ax.text(j, i, value_to_show, ha="center", va="center", color="black", size=16)


    # annotation marginals below and right next to matrix
    if 'annotation_marginals' in kwargs:
        ls_marginals = kwargs['annotation_marginals']

        # marginals right hand side matrix
        ls_rhs = ls_marginals[0]
        # marginals below hand side matrix
        ls_bottom = ls_marginals[1]

        # right hand side
        for i in range(len(row_names)):

            # get value from marginal list
            value_to_show = ls_rhs[i]

            # format percentage
            value = f'{value_to_show*100:.1f}%'

            # annotate text
            ax.text(len(col_names), i, value, ha="center", va="center", color="black", size=16)
            ax.text(len(col_names), -0.66, 'average', ha="center", va="center", color="black", size=fontsize_labels)

        # bottom
        for j in range(len(col_names)):

            # get value from marginal list
            value_to_show = ls_bottom[j]

            # format percentage
            value = f'{value_to_show*100:.1f}%'

            # annotate text
            ax.text(j, len(row_names), value, ha="center", va="center", color="black", size=16)
            ax.text(-0.66, len(row_names), 'average', ha="right", va="center", color="black", size=fontsize_labels)

    else:
        pass

# matrix based on onderwijsvorm & leeftijd
def get_matrix(df, categories, metric, k_rows_matrix, k_cols_matrix):

    # get the metric per category
    metric_per_category = df.loc[categories, metric]

    # create empty matrix
    matrix = np.zeros((k_rows_matrix, k_cols_matrix))

    # fill the matrix - fill from (0, 0) to (0, 1), .., (1, 0), (1, 1), ..(k_rows_matrix, k_cols_matrix)
    i_cat = 0
    for i in range(k_rows_matrix):
        for j in range(k_cols_matrix):
            matrix[i, j] = metric_per_category[i_cat]
            i_cat += 1
    
    return matrix

# function to compute marginals and return as list
def marginals(df,categories, metric):

    # initialize list and iterate through categories
    marginals_ls = []

    for category in categories:

        # compute marginals and add to list
        marginal = df.loc[category, metric] / df.loc[category, 'Total']
        marginals_ls.append(marginal)

    return marginals_ls