import pandas as pd
import tiktoken

def get_comments(path: str = None) -> pd.DataFrame:
    if path is None:
        raise ValueError("Path is required")
    comments = pd.read_csv(path)
    comments['Date'] = pd.to_datetime(comments['Date'])
    comments = comments.sort_values(by=['Date', 'UnitCode'], ascending=[True, True]).reset_index(drop=True)
    comments['Year'] = comments['Date'].dt.year
    comments['MonthName'] = comments['Date'].dt.month_name()
    comments['MonthNumber'] = comments['Date'].dt.month
    return comments
def countTokens(prompt: str) -> int:
    return len(encoding.encode(prompt))
def formatComment(unitCode: str = None, year: int = None, month: int = None):
    data = comments[(comments['UnitCode'] == unitCode) & (comments['Year'] == year) & (comments['MonthNumber'] == month)]
    if data.empty:
        return 'No comments found'
    formatted = 'Comment for ' + data['MonthName'].iloc[0] + ':\n' + data['Comments'].iloc[0]
    return formatted
print(get_comments('Data/comments.csv'))