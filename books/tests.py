from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from .models import Book





class EverythingAboutBookTest(TestCase):
#_______________________________________
#________________________________________________________
    def setUp(self):
        user = get_user_model().objects.create(username='reza',)
        user.set_password('12345')
        user.save()

        l = self.client.login(username="reza", password="12345")
        self.assertTrue(l)

        self.book1 = Book.objects.create(
            title='book1',
            author='author,book1',
            description='description,book1',
            price=11.11,
            user_id=1
        )

    # # -------------------------------------------------------------------------------
    def test_listview_url_name(self):
        response = self.client.get(reverse('book_list_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'book1')
        # ______________-_
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'books/book_list_view.html')

    # ---------------------------------------------------------------------------------
    def test_detail_view_url_name(self):
        l = self.client.login(username="reza", password="12345")
        self.assertTrue(l)
        # ---------------
        response = self.client.get(reverse('book_detail', args=[1]),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'book1')
        # ____________
        # response = self.client.get('/books/<int:1>/',follow=True)
        # self.assertEqual(response.status_code, 200)
        # -----------------
        self.client.logout()
        response = self.client.get(reverse('book_create'))
        self.assertNotEqual(response.status_code, 200)
    # ---------------------------------------------------------------------------------
    def test_createview_url_name(self):
        l = self.client.login(username="reza", password="12345")
        self.assertTrue(l)
        # ---------------
        response = self.client.get(reverse('book_create'),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'ایجاد کتاب')
        # __________
        # response = self.client.get('newbooke/',follow=True)
        # self.assertEqual(response.status_code, 200)
        l = self.client.login(username="reza", password="12345")
        response = self.client.post(reverse('book_create'),{
            'title' : 'book2',
            'author' : 'author,book2',
            'description' : 'description,book2',
            'price' : 22.22,
        },follow=True)


        response = self.client.get(reverse('book_detail', args=[2]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 22.22)
        # ____________
        # response = self.client.get('/books/<int:1>/',follow=True)
        # self.assertEqual(response.status_code, 200)
        # -----------------
        self.client.logout()
        response = self.client.get(reverse('book_create'))
        self.assertEqual(response.status_code, 302)
    # ---------------------------------------------------------------------------------
    def test_updateview_url_name(self):
        l = self.client.login(username="reza", password="12345")
        self.assertTrue(l)
        # ---------------
        response = self.client.get(reverse('book_update', args=[1]),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'ویرایش کردن')
        # ____________
        response = self.client.get('/books/1/edit/',follow=True)
        self.assertEqual(response.status_code, 200)
        # ------------------------
        response = self.client.post(reverse('book_update', args=[1]),{'title':'book1000',
            'author':'author,book1000',
            'description':'description,book1000',
            'price':11001.11},follow=True)

        # -------
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response,11.11)

    # ---------------------------------------------------------------------------------
    def test_deleteview_url_name(self):
        l = self.client.login(username="reza", password="12345")
        self.assertTrue(l)
        # ---------------
        response = self.client.get(reverse('book_delete', args=[1]),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'حذف کتاب')
        self.assertContains(response, self.book1.title)
        # ---
        response = self.client.post(reverse('book_delete', args=[1]),)
        self.assertEqual(response.status_code, 302)
        # ---
        response = self.client.get(reverse('book_delete', args=[1]),)
        self.assertNotEqual(response.status_code, 200)
        # ____________
        # response = self.client.get('/books/<int:1>/delet/',follow=True)
        # self.assertEqual(response.status_code, 200)











#
#
#
#
#
#
#
# -------------------------------------------------------------------------------------------------------------------
#
#
# class EverythingAboutBookTest(TestCase):
#
#
#     def test_listview_url_name(self):
#         response = self.client.get(reverse('book_list_view'))
#         self.assertEqual(response.status_code, 200)
#
#         respons = self.client.get('/')
#         self.assertEqual(respons.status_code, 200)
#
#     #
#     # def test_detail_view_url_name(self):
#     #     response = self.client.post(reverse('book_detail', args=[1]), {
#     #         'username': 'reza',
#     #         'password': 'reza'
#     #     }
#     #     )
#     #     self.assertEqual(response.status_code, 302)
#     #     response = self.client.get(reverse('book_detail', args=[1]))
#     #     self.assertEqual(response.content, 200)
#
#     #
#     #
#
#     def test_createview_url_name(self):
#         # user = CustomUser.objects.create(username='testuser', password='12345')
#         user = get_user_model().objects.create(username='reza')
#         user.set_password('12345')
#         user.save()
#         ----------
#         l = self.client.login(username="reza", password="12345")
#         self.assertTrue(l)
#         response = self.client.get(reverse('book_create'), follow=True)
#         self.assertEqual(response.status_code, 200)
#         # response = self.client.get(reverse('book_create'), follow=True)
#         self.assertContains(response, 'Title')
#         # self.assertEqual(response.status_code, 200)
#         # self.client.logout()
#         # respons = self.client.get(reverse('book_create'), follow=True)
#         # self.assertNotEqual(respons.status_code, 200)
#     #
#     # def test_updateview_url_name(self):
#     #     response = self.client.get(reverse('book_update', args=[2]))
#     #     self.assertEqual(response.status_code, 302)
#     #
#     #     respons = self.client.get('int:2>/edit/')
#     #     self.assertEqual(respons.status_code, 302)
#     #
#     #
#     # def test_deleteview_url_name(self):
#     #     response = self.client.get(reverse('book_delete', args=[3]))
#     #     self.assertEqual(response.status_code, 302)
#     #
#     #     respons = self.client.get('<int:3>/delet/')
#     #     self.assertEqual(respons.status_code, 200)
#     #

