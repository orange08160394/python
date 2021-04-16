import bar_chart_race as bcr
import pandas as pd
df=pd.read_csv('taiwan_popualtion.csv',index_col='date',parse_dates=['date'])
print(df.tail())

bcr.bar_chart_race(
    df=df,
    filename='Taiwancity.mp4' ,
    orientation='h',
    sort='desc',
    n_bars=6,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=10,
    interpolate_period=False,
    label_bars=True,
    bar_size=.95,
    period_label={'x': .99, 'y': .25, 'ha': 'right', ' va': 'center'},
    period_fmt='%B %d, %Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total population: {v.nlargest(6).sum():,.0f},
                                      'ha': 'right', 'size': 8, 'family':'Courier New'},
    perpendicularbarfunc='median',
    period_length=800,
    figsize=(5, 3),
    dpi=144,
    cmap='darkl2',
    title='Population of Six_Cities',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={’alpha': .7},
    filter_column_colors=False)