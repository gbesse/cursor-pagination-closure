import json
from .common import identifier,integer
def run(data):
 pages=data['pages'];limit=integer(data.get('max_pages',100),1,1000)
 if not isinstance(pages,dict)or len(pages)>1000:raise ValueError('pages')
 cursor='START';seen=set();items={};visited=[];reason=None
 for _ in range(limit):
  if cursor in seen:reason='cursor_cycle';break
  seen.add(cursor)
  if cursor not in pages:reason='missing_page';break
  page=pages[cursor];rows=page['items']
  if not isinstance(rows,list)or len(rows)>1000:raise ValueError('items')
  visited.append(cursor)
  for row in rows:
   key=identifier(row['id']);canonical=json.dumps(row,sort_keys=True,allow_nan=False)
   if key in items and canonical!=items[key][0]:reason='conflicting_item';break
   items[key]=(canonical,row)
  if reason:break
  nxt=page.get('next_cursor')
  if nxt is None:return {'complete':True,'visited_cursors':visited,'items':[r for _,r in items.values()],'reason':None}
  cursor=identifier(nxt)
 else:reason='page_budget'
 return {'complete':False,'visited_cursors':visited,'items':[r for _,r in items.values()],'reason':reason}
