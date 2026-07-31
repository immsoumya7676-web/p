import plotly.graph_objects as go


def risk_gauge(risk):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=risk,

        title={'text':"Risk Score"},

        gauge={

            'axis':{'range':[0,100]},

            'bar':{'color':"red"},

            'steps':[

                {'range':[0,40],'color':"green"},

                {'range':[40,70],'color':"yellow"},

                {'range':[70,100],'color':"red"}

            ]

        }

    ))

    return fig


def pie_chart(safe,risky):

    fig=go.Figure(

        data=[

            go.Pie(

                labels=["Safe","Risk"],

                values=[safe,risky],

                hole=.55

            )

        ]

    )

    return fig
