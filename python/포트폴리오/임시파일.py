# 크롤링 라이브러리
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# dash 라이브러리
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State

# 댓글을 달 빈 리스트를 생성합니다.
url = "https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=100&oid=421&aid=0005545824"

def get_df(url):
    # 댓글을 달 빈 리스트를 생성한다.
    List = []
    url = url
    oid = url.split("oid=")[1].split("&")[0]
    aid = url.split("aid=")[1]
    page = 1
    header = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "referer": url,

    }
    while True:
        c_url = "https://apis.naver.com/commentBox/cbox/web_neo_list_jsonp.json?ticket=news&templateId=default_society&pool=cbox5&_callback=jQuery1707138182064460843_1523512042464&lang=ko&country=&objectId=news" + oid + "%2C" + aid + "&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page=" + str(
            page) + "&refresh=false&sort=FAVORITE"
    # 파싱하는 단계입니다.
        r = requests.get(c_url, headers=header)
        cont = BeautifulSoup(r.content, "html.parser")
        total_comm = str(cont).split('comment":')[1].split(",")[0]

        match = re.findall('"contents":([^\*]*),"userIdNo"', str(cont))
        # 댓글을 리스트에 중첩합니다.
        List.append(match)

        # 한번에 댓글이 20개씩 보이기 때문에 한 페이지씩 몽땅 댓글을 긁어 옵니다.
        if int(total_comm) <= ((page) * 20):
            break
        else:
            page += 1

    def flatten(l):
        flatList = []
        for elem in l:
        # if an element of a list is a list
        # iterate over this list and add elements to flatList
            if type(elem) == list:
                for e in elem:
                    flatList.append(e)
            else:
               flatList.append(elem)
        return flatList

    # 리스트 결과입니다.
    # print(flatten(List))

    # convert dataframe
    data = pd.DataFrame(flatten(List), columns=["기사댓글"])
    data = data.rename_axis("index").reset_index()

    # write_excel
    # data.to_excel("news_comments.xlsx", sheet_name="Sheet1")
    return data

# data = get_df(url)
data = pd.DataFrame({"index": [0],
                     "기사댓글": ["댓글"]})
# print(data.head())

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True,
                prevent_initial_callbacks=True)

app.title = "네이버 크롤링"
server = app.server # 해당 코드를 새롭게 추가한다.

app.layout = html.Div(
    children = [
        html.Div(
            children = [
                html.H1(children="네이버 뉴스 댓글 크롤링 싸이트", className="header_title", ),
                html.P(children="temp ~~~ ", className="header_description", ),
            ],
            className='header',
        ),
        # URL html.Div
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="네이버 뉴스 주소를 입력하여 주세요", className="menu-title"),
                        dcc.Input(id="naver_news_url",
                                  placeholder="URL을 입력하여 주세요",
                                  className="naver_news_url"),
                        html.P("예: https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=100&oid=586&aid=0000027892",
                               className="url_sample"),
                        html.Button('크롤링 시작', id='submit-val', n_clicks=0),
                    ]
                ), # html.Div
            ], # children
            className="menu"
        ), # URL html.Div
        html.Div(
            children=[
                html.Div(
                    children=dash_table.DataTable(
                        id = "data_id",
                        columns=[{"id":c, "name":c} for c in data.columns],
                        data = [],
                        style_cell={'textAlign': 'left',
                                    'whiteSpace': 'normal',
                                    'fontWeight': 'normal',
                                    'height': 'auto'
                                    },
                        style_header={
                            'backgroundColor': 'black',
                            'fontWeight': 'bold',
                            'color': 'white'
                        },
                        export_format="xlsx",
                    ) # children
                ) # Table
            ],
            className="wrapper",
        ), # html.Div
    ]
)

# URL 텍스트
@app.callback(
    Output(component_id="data_id", component_property="data"),
    [Input(component_id="submit-val", component_property="n_clicks")],
    [State(component_id="naver_news_url", component_property='value')]

)

def update_output_url(n_clicks, input_url):
    global data
    if n_clicks > 0:
        data = get_df(input_url)
    else:
        print("None")
    return data.to_dict('records')


if __name__ == "__main__":
	app.run_server(debug=True)