from django.test import TestCase
from .models import TodoNote, user
# Create your tests here.

class TodoNoteTest(TestCase):
    
    def test_model(self):
        test_user = user.objects.create_user('Test user')
        todo = TodoNote.objects.create(title='Test title', author=test_user)
        self.assertIsNotNone(TodoNote.objects.get(id=todo.id))