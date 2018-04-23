from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todo.models import TodoItem

def createItem(client):
  url = reverse('todoitem-list')
  data = {'title':'walk the dog'}
  return client.post(url,data,format='json')


class TestCreateTodoItem(APITestCase):
  def setUp(self):
    self.response = createItem(self.client)
  
  def test_receive_201_create_status_code(self):
    self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)
  
  def test_receive_location_header_hyperlink(self):
    self.assertRegexpMatches(self.response['Location'],'^http://.+/todos/[\d]+$')
  
  def test_item_was_create(self):
    self.assertEqual(TodoItem.objects.count(),1)
  
  def test_item_has_correct_title(self):
    self.assertEqual(TodoItem.objects.get().title,'walk the dog')


class TestUpdateTodoItem(APITestCase):
  def setUp(self):
    self.response = createItem(self.client)
    self.assertEqual(TodoItem.objects.get().completed,False)
    url = self.response['Location']
    data = {'title':"walk the dog",'completed':True}
    self.response = self.client.put(url,data,format='json')

  def test_receive_200_create_status_code(self):
    self.assertEqual(self.response.status_code,status.HTTP_200_OK)
  

  def test_item_was_updated(self):
    self.assertEqual(TodoItem.objects.get().completed,True)
  
  def test_item_has_correct_title(self):
    self.assertEqual(TodoItem.objects.get().title,'walk the dog')

class TestPatchTodoItem(APITestCase):
  def setUp(self):
    self.response = createItem(self.client)
    self.assertEqual(TodoItem.objects.get().completed,False)
    url = self.response['Location']
    data = {'title':"walk the dog",'completed':True}
    self.response = self.client.patch(url,data,format='json')

  def test_receive_200_create_status_code(self):
    self.assertEqual(self.response.status_code,status.HTTP_200_OK)
  

  def test_item_was_updated(self):
    self.assertEqual(TodoItem.objects.get().completed,True)
  
  def test_item_has_correct_title(self):
    self.assertEqual(TodoItem.objects.get().title,'walk the dog')


class TestDeleteTodoItem(APITestCase):
  def setUp(self):
    self.response = createItem(self.client)
    self.assertEqual(TodoItem.objects.get().completed,False)
    url = self.response['Location']
    self.response = self.client.delete(url)

  def test_receive_204_delete_status_code(self):
    self.assertEqual(self.response.status_code,status.HTTP_204_NO_CONTENT)
  
  def test_item_was_delete(self):
    self.assertEqual(TodoItem.objects.count(),0)


class TestDeleteAllTodoItem(APITestCase):
  def setUp(self):
    createItem(self.client)
    createItem(self.client)
    self.assertEqual(TodoItem.objects.count(),2)
    self.response = self.client.delete(reverse("todoitem-list"))

  def test_receive_204_delete_status_code(self):
    self.assertEqual(self.response.status_code,status.HTTP_204_NO_CONTENT)
  
  def test_all_item_was_delete(self):
    self.assertEqual(TodoItem.objects.count(),0)