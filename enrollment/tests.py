from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import render, redirect
from enrollment.models import Class, Enrollment
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

# Create your tests here.

class ClassTestCase(TestCase):

    def setUp(self):

        # create airports
        class1 = Class.objects.create(class_code="001", class_name="CN 001")
        class2 = Class.objects.create(class_code="002", class_name="CN 002")

        user = User.objects.create(first_name="abc", last_name="defg",username="harry2", is_active=True)
        user.set_password('12345')
        
    #test model
    def test_class_empty(self):
        """ is_class_empty should be True """

        a_class = Class.objects.first()

        self.assertTrue(a_class.is_class_empty())

    def test_class_not_empty(self):
        """ is_class_empty should be False """

        student1 = User.objects.create(
            first_name="harry", last_name="potter", username="harry1", password="1234")
        student2 = User.objects.create(
            first_name="hermione", last_name="granger", username="hermione1", password="1234")

        a_class = Class.objects.first()
        Enrollment.objects.create(student = student1, enrolled_class = a_class)

        self.assertFalse(a_class.is_class_empty())


    #test views
    def test_classlist(self):
        #ทดสอบว่าเรียก views class list ได้"
        """ class_list view's status code is ok """
        test_user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(test_user)

        response = self.client.get(reverse("class_list"))
        self.assertEqual(response.status_code, 200)

    def test_enroll_class1(self):
        #ทดสอบว่า enroll class ได้ ถ้ามีที่นั่งว่าง
        """test_enroll_class1 should return True"""
        test_user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(test_user)

        response = self.client.get(reverse("enroll_class", args=["001"]))
        self.assertEqual(response.status_code, 302)

        # Check for a success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(messages[0].message, 'You have successfully enrolled in this class.')


    def test_enrolled_classes(self):
        #ทดสอบว่าเรียก views enrolled_classes ได้"
        """ enrolled_classes view's status code is ok """
        test_user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(test_user)

        response = self.client.get(reverse("enrolled_classes"))
        self.assertEqual(response.status_code, 200)


    def test_unenroll_class1(self):
        #ทดสอบว่าun enroll class ได้
        """test_enroll_class1 should return True"""
        test_user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(test_user)

        self.client.get(reverse("enroll_class", args=["001"]))
        response = self.client.get(reverse("unenroll_class", args=["001"]))
        self.assertEqual(response.status_code, 302)

        # Check for a success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(messages[1].message, 'You have successfully unenrolled from this class.')
    

        

