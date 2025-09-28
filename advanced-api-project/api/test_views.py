from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpass")

        # Create some sample books
        self.book1 = Book.objects.create(title="Python Basics", author="John Doe", publication_year=2020)
        self.book2 = Book.objects.create(title="Django Advanced", author="Jane Doe", publication_year=2021)

        # Auth clients
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        self.admin_client = APIClient()
        self.admin_client.login(username="admin", password="adminpass")

        # URLs
        self.list_url = reverse("book-list")   # hook to ListView
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.pk})
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", kwargs={"pk": self.book1.pk})
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book1.pk})

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": "Jane Doe"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Jane Doe")

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Python"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn("Python Basics", response.data[0]["title"])

    def test_order_books(self):
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Django Advanced")

    def test_create_book_authenticated(self):
        data = {"title": "New Book", "author": "Alice", "publication_year": 2022}
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        unauth_client = APIClient()
        data = {"title": "Unauthorized", "author": "Bob", "publication_year": 2023}
        response = unauth_client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book(self):
        data = {"title": "Updated Python Basics", "author": "John Doe", "publication_year": 2020}
        response = self.client.put(self.update_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Python Basics")

    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
