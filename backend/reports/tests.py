import json
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from reports.models import Report


class ReportViewsTests(TestCase):

    @classmethod
    def setUp(cls):
        cls.user = get_user_model().objects.create_user(
            username='auth_user',
            email='123@mail.ru',
            password='111'
        )
        cls.other_user = get_user_model().objects.create_user(
            username='other_auth_user',
            email='321@mail.ru',
            password='111'
        )
        cls.auth_client = Client()
        cls.other_auth_client = Client()
        cls.auth_client.force_login(cls.user)
        cls.other_auth_client.force_login(cls.other_user)
        cls.report = Report.objects.create(
            author=cls.user,
            title='Test report',
            text=json.dumps({'par_info': [], 'tab_info': []})
        )
        cls.url_detail = reverse('reports:detail', args=[cls.report.id])
        cls.url_list = reverse('reports:report_list')
        cls.url_download = reverse('reports:download')
        cls.url_delete = reverse('reports:delete', args=[cls.report.id])

    def test_download_report_view_auth(self):
        response = self.auth_client.get(self.url_download)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        response = self.client.get(self.url_download)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_detail_report_view(self):
        response = self.auth_client.get(self.url_detail)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        response = self.other_auth_client.get(self.url_detail)
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)

    def test_delete_report_view(self):
        notes_count = Report.objects.count()
        response = self.auth_client.post(self.url_delete)
        self.assertRedirects(response, self.url_list)
        self.assertLess(Report.objects.count(), notes_count)
