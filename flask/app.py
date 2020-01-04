
from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py

app = Flask(__name__)

# 准备工作
df = pd.read_csv('data.csv')#读取
Race_available = list(df.地区.dropna().unique())#列表下拉值赋予给regions_available
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()


@app.route('/',methods=['GET'])
def hu_run_2019():
    data_str = df.to_html()
    return render_template('results2.html',
                           the_res = data_str,
                           the_select_region=Race_available)

@app.route('/hurun',methods=['POST'])
#三个图表
def timeline_bar():

    with open("GDP地图.html", encoding="utf8", mode="r") as f:
        plot_all1 = "".join(f.readlines())

    with open("GDP与失业率对比.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())

    with open("居民消费水平地图.html", encoding="utf8", mode="r") as f:
        plot_all4 = "".join(f.readlines())
    with open("居民消费水平与失业率对比.html", encoding="utf8", mode="r") as f:
        plot_all5 = "".join(f.readlines())
    with open("失业率情况图.html", encoding="utf8", mode="r") as f:
        plot_all3 = "".join(f.readlines())

    data_str = df.to_html()

    return render_template('results2.html',
                            the_plot_all = plot_all1,
                           the_plot_all2 = plot_all2,
                           the_plot_all3 = plot_all3,
                           the_plot_all4 = plot_all4,
                           the_plot_all5 = plot_all5,
                            the_res = data_str,
                            the_select_region=Race_available,
                           )


if __name__ == '__main__':
    app.run(debug=True,port=8000)
