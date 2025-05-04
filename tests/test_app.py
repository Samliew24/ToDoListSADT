
import unittest
import sys
import os

# Allow importing app.py using global Python interpreter
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app import app

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Home Page Test
    def test_homepage_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Functional Tests - Adding tasks
    def test_add_task_1(self):
        response = self.app.post('/add', data={'title': 'Task 1'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_2(self):
        response = self.app.post('/add', data={'title': 'Task 2'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_3(self):
        response = self.app.post('/add', data={'title': 'Task 3'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_4(self):
        response = self.app.post('/add', data={'title': 'Task 4'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_5(self):
        response = self.app.post('/add', data={'title': 'Task 5'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_6(self):
        response = self.app.post('/add', data={'title': 'Task 6'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_7(self):
        response = self.app.post('/add', data={'title': 'Task 7'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_8(self):
        response = self.app.post('/add', data={'title': 'Task 8'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_9(self):
        response = self.app.post('/add', data={'title': 'Task 9'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_10(self):
        response = self.app.post('/add', data={'title': 'Task 10'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_11(self):
        response = self.app.post('/add', data={'title': 'Task 11'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_12(self):
        response = self.app.post('/add', data={'title': 'Task 12'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_13(self):
        response = self.app.post('/add', data={'title': 'Task 13'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_14(self):
        response = self.app.post('/add', data={'title': 'Task 14'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_15(self):
        response = self.app.post('/add', data={'title': 'Task 15'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_16(self):
        response = self.app.post('/add', data={'title': 'Task 16'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_17(self):
        response = self.app.post('/add', data={'title': 'Task 17'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_18(self):
        response = self.app.post('/add', data={'title': 'Task 18'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_19(self):
        response = self.app.post('/add', data={'title': 'Task 19'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_20(self):
        response = self.app.post('/add', data={'title': 'Task 20'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_21(self):
        response = self.app.post('/add', data={'title': 'Task 21'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_22(self):
        response = self.app.post('/add', data={'title': 'Task 22'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_23(self):
        response = self.app.post('/add', data={'title': 'Task 23'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_24(self):
        response = self.app.post('/add', data={'title': 'Task 24'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_25(self):
        response = self.app.post('/add', data={'title': 'Task 25'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_26(self):
        response = self.app.post('/add', data={'title': 'Task 26'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_27(self):
        response = self.app.post('/add', data={'title': 'Task 27'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_28(self):
        response = self.app.post('/add', data={'title': 'Task 28'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_29(self):
        response = self.app.post('/add', data={'title': 'Task 29'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_30(self):
        response = self.app.post('/add', data={'title': 'Task 30'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_31(self):
        response = self.app.post('/add', data={'title': 'Task 31'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_32(self):
        response = self.app.post('/add', data={'title': 'Task 32'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_33(self):
        response = self.app.post('/add', data={'title': 'Task 33'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_34(self):
        response = self.app.post('/add', data={'title': 'Task 34'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_35(self):
        response = self.app.post('/add', data={'title': 'Task 35'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_36(self):
        response = self.app.post('/add', data={'title': 'Task 36'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_37(self):
        response = self.app.post('/add', data={'title': 'Task 37'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_38(self):
        response = self.app.post('/add', data={'title': 'Task 38'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_39(self):
        response = self.app.post('/add', data={'title': 'Task 39'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_40(self):
        response = self.app.post('/add', data={'title': 'Task 40'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_41(self):
        response = self.app.post('/add', data={'title': 'Task 41'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_42(self):
        response = self.app.post('/add', data={'title': 'Task 42'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_43(self):
        response = self.app.post('/add', data={'title': 'Task 43'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_44(self):
        response = self.app.post('/add', data={'title': 'Task 44'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_45(self):
        response = self.app.post('/add', data={'title': 'Task 45'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_46(self):
        response = self.app.post('/add', data={'title': 'Task 46'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_47(self):
        response = self.app.post('/add', data={'title': 'Task 47'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_48(self):
        response = self.app.post('/add', data={'title': 'Task 48'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_49(self):
        response = self.app.post('/add', data={'title': 'Task 49'})
        self.assertEqual(response.status_code, 302)

    def test_add_task_50(self):
        response = self.app.post('/add', data={'title': 'Task 50'})
        self.assertEqual(response.status_code, 302)


    # Functional Tests - Completing tasks
    def test_complete_task_1(self):
        response = self.app.get('/complete/1')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_2(self):
        response = self.app.get('/complete/2')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_3(self):
        response = self.app.get('/complete/3')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_4(self):
        response = self.app.get('/complete/4')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_5(self):
        response = self.app.get('/complete/5')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_6(self):
        response = self.app.get('/complete/6')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_7(self):
        response = self.app.get('/complete/7')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_8(self):
        response = self.app.get('/complete/8')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_9(self):
        response = self.app.get('/complete/9')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_10(self):
        response = self.app.get('/complete/10')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_11(self):
        response = self.app.get('/complete/11')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_12(self):
        response = self.app.get('/complete/12')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_13(self):
        response = self.app.get('/complete/13')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_14(self):
        response = self.app.get('/complete/14')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_15(self):
        response = self.app.get('/complete/15')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_16(self):
        response = self.app.get('/complete/16')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_17(self):
        response = self.app.get('/complete/17')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_18(self):
        response = self.app.get('/complete/18')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_19(self):
        response = self.app.get('/complete/19')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_task_20(self):
        response = self.app.get('/complete/20')
        self.assertTrue(response.status_code in [404, 302])


    # Functional Tests - Deleting tasks
    def test_delete_task_1(self):
        response = self.app.get('/delete/1')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_2(self):
        response = self.app.get('/delete/2')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_3(self):
        response = self.app.get('/delete/3')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_4(self):
        response = self.app.get('/delete/4')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_5(self):
        response = self.app.get('/delete/5')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_6(self):
        response = self.app.get('/delete/6')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_7(self):
        response = self.app.get('/delete/7')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_8(self):
        response = self.app.get('/delete/8')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_9(self):
        response = self.app.get('/delete/9')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_10(self):
        response = self.app.get('/delete/10')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_11(self):
        response = self.app.get('/delete/11')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_12(self):
        response = self.app.get('/delete/12')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_13(self):
        response = self.app.get('/delete/13')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_14(self):
        response = self.app.get('/delete/14')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_15(self):
        response = self.app.get('/delete/15')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_16(self):
        response = self.app.get('/delete/16')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_17(self):
        response = self.app.get('/delete/17')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_18(self):
        response = self.app.get('/delete/18')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_19(self):
        response = self.app.get('/delete/19')
        self.assertTrue(response.status_code in [404, 302])

    def test_delete_task_20(self):
        response = self.app.get('/delete/20')
        self.assertTrue(response.status_code in [404, 302])


    # Boundary and Exception Handling Tests

    def test_add_empty_task(self):
        response = self.app.post('/add', data={'title': ''})
        self.assertEqual(response.status_code, 302)

    def test_add_long_task(self):
        long_title = 'A' * 100
        response = self.app.post('/add', data={'title': long_title})
        self.assertEqual(response.status_code, 302)

    def test_add_special_char_task(self):
        response = self.app.post('/add', data={'title': '@!#$%^&*()'})
        self.assertEqual(response.status_code, 302)

    def test_delete_nonexistent_task(self):
        response = self.app.get('/delete/9999')
        self.assertTrue(response.status_code in [404, 302])

    def test_complete_nonexistent_task(self):
        response = self.app.get('/complete/9999')
        self.assertTrue(response.status_code in [404, 302])

    def test_wrong_http_method_on_add(self):
        response = self.app.get('/add')
        self.assertIn(response.status_code, [405, 302])

    def test_wrong_http_method_on_delete(self):
        response = self.app.post('/delete/1')
        self.assertIn(response.status_code, [405, 302])

    def test_access_invalid_url(self):
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

    def test_submit_whitespace_only_task(self):
        response = self.app.post('/add', data={'title': '   '})
        self.assertEqual(response.status_code, 302)

    def test_add_task_with_emojis(self):
        response = self.app.post('/add', data={'title': '😀👍🔥💯'})
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
