import unittest,copy,json
from cursor_pagination_closure import run
DEMO={'pages': {'START': {'items': [{'id': 'first'}], 'next_cursor': 'p2'}, 'p2': {'items': [{'id': 'second'}]}}}
class DomainTests(unittest.TestCase):
 def test_reads_second_page(self):
  x=run(DEMO);self.assertTrue(x['complete']);self.assertEqual([r['id']for r in x['items']],['first','second'])
 def test_missing_is_not_empty(self):
  x=copy.deepcopy(DEMO);del x['pages']['p2'];y=run(x);self.assertFalse(y['complete']);self.assertEqual(y['reason'],'missing_page')
 def test_cursor_cycle(self):
  x=copy.deepcopy(DEMO);x['pages']['p2']['next_cursor']='START';self.assertEqual(run(x)['reason'],'cursor_cycle')
 def test_conflicting_identity(self):
  x=copy.deepcopy(DEMO);x['pages']['p2']['items']=[{'id':'first','changed':True}];self.assertEqual(run(x)['reason'],'conflicting_item')
