import pandas as pd 
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
s = "TRL_987"
#to cut the info of a particular student
student_df = df.loc[df["student_id"] == "TRL_987"]
fig=go.Figure(go.Bar(x=student_df.groupby("level")["attempt"].mean(),y=["level 1","level 2","level 3","level 4"],orientation='h'))
fig.show()






