from django.test import TestCase
# Create your tests here.
from .views import alert1
class Test(TestCase):
    def alltest(self):
        req = {'stat':'1234,65,45,35'}
        self.assertEquals(alert1(req),'No Alert,1234')
        req = {'stat':'1234,95,45,55'}
        self.assertEquals(alert1(req),'Alert,1234, CPU UTILIZATION VIOLATED')
        req = {'stat':'1234,75,95,35'}
        self.assertEquals(alert1(req),'Alert,1234, MEMORY UTILIZATION VIOLATED')
        req = {'stat':'1234,75,35,85'}
        self.assertEquals(alert1(req),'Alert,1234, DISK UTILIZATION VIOLATED')
        req = {'stat':'1234,95,85,35'}
        self.assertEquals(alert1(req),'Alert,1234, CPU UTILIZATION VIOLATED, MEMORY UTILIZATION VIOLATED')
        req = {'stat':'1234,95,85,35'}
        self.assertEquals(alert1(req),'Alert,1234, CPU UTILIZATION VIOLATED, DISK UTILIZATION VIOLATED')
        req = {'stat':'1234,35,85,85'}
        self.assertEquals(alert1(req),'Alert,1234, MEMEORY UTILIZATION VIOLATED, DISK UTILIZATION VIOLATED')
        req = {'stat':'1234,95,85,75'}
        self.assertEquals(alert1(req),'Alert,1234, CPU UTILIZATION VIOLATED, MEMEORY UTILIZATION VIOLATED, DISK UTILIZATION VIOLATED')

        
