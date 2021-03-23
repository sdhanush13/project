from app import models
from django.test import TestCase

# Create your tests here.
# class ExampleTestCase(TestCase):
#     def setUp(self):
#         self.a=10
#         self.b=10
#     def testCase(self):
#         self.assertEqual(self.a,self.b)
# class DBTestCase(TestCase):
#     def setUp(self):
#         print("Intial Setup for DB TestCase")
#
#     def testTenantinfo(self):
#         print("DB Test Case Running")
#         res = models.ExampleModel.objects.all().values('foobar')
#         print(type(res))
#         res = 1
#         self.assertEqual(res, 1)