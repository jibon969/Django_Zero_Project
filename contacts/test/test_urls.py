from django.test import SimpleTestCase
from django.urls import reverse, resolve
from contacts.views import (
    contact,
    contact_list,
    download_contact_csv
)


class TestUrls(SimpleTestCase):

    # contact urls
    def test_contact_url(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)

    # contact_list urls
    def test_contact_list_url(self):
        url = reverse('contact-list')
        self.assertEquals(resolve(url).func, contact_list)

    # update_contact
    def test_update_contact_url(self):
        """
        How do I unit test django urls ?
        :return:
        """
        url = reverse('update-contact', args=[1])
        self.assertEquals(url, '/update-contact/1/')

    # Delete contact urls
    def test_delete_contact_url(self):
        """
        How do I unit test django urls ?
        https://stackoverflow.com/questions/18987051/how-do-i-unit-test-django-urls
        :return:
        """
        url = reverse('delete-contact', args=[1])
        self.assertEquals(url, '/delete-contact/1/')

    # replay-contact
    def test_replay_contact_url(self):
        """
        :return:
        """
        url = reverse('replay-contact', args=[1])
        self.assertEquals(url, '/replay-contact/1/')
    

    # contact urls
    def test_download_contact_csv_url(self):
        url = reverse('download-contact-csv')
        self.assertEquals(resolve(url).func, download_contact_csv)
