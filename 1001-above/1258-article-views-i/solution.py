# SQL:
# SELECT DISTINCT author_id AS id FROM Views WHERE author_id = viewer_id ORDER BY id ASC;

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    self_views = views[views['author_id'] == views['viewer_id']]
    unique_authors = self_views['author_id'].unique()
    unique_authors.sort()
    return pd.DataFrame({'id': unique_authors})
