from django.test import TestCase
from .views import (
    front_times_view,
    xyz_there_view,
    centered_average_view,
    no_teen_sum_view,
    fix_teen,
)


class FrontTimesTestCase(TestCase):
    def test_front_times_view(self):
        # Test the front_times_view with different inputs

        # Test case 1: Short input string
        front_times_response = self.client.post(
            "/front_times/", {"input_string": "Chocolate", "n": 2}
        )
        self.assertContains(front_times_response, "ChoCho")

        # Test case 2: Long input string
        front_times_response = self.client.post(
            "/front_times/", {"input_string": "Chocolate", "n": 3}
        )
        self.assertContains(front_times_response, "ChoChoCho")

        # Test case 3: Empty input string
        front_times_response = self.client.post(
            "/front_times/", {"input_string": "Abc", "n": 3}
        )
        self.assertContains(front_times_response, "AbcAbcAbc")


class XYZThereTestCase(TestCase):
    def test_xyz_there_view(self):
        # Test the xyz_there_view with different inputs

        # Test case 1: xyz is present
        xyz_there_response = self.client.post("/xyz_there/", {"input_string": "abcxyz"})
        self.assertContains(xyz_there_response, "True")

        # Test case 2: xyz is not directly preceded by a period
        xyz_there_response = self.client.post(
            "/xyz_there/", {"input_string": "abc.xyz"}
        )
        self.assertContains(xyz_there_response, "False")

        # Test case 3: xyz is present and directly preceded by a period
        xyz_there_response = self.client.post(
            "/xyz_there/", {"input_string": "xyz.abc"}
        )
        self.assertContains(xyz_there_response, "True")

        # Test case 4: Short input string
        xyz_there_response = self.client.post("/xyz_there/", {"input_string": "xyz"})
        self.assertContains(xyz_there_response, "True")


class CenteredAverageTestCase(TestCase):
    def test_centered_average_view(self):
        # Test the centered_average_view with different inputs

        # Test case 1: Regular input
        centered_average_response = self.client.post(
            "/centered_average/", {"nums": "1, 2, 3, 4, 100"}
        )
        self.assertContains(centered_average_response, "3")

        # Test case 2: Multiple copies of smallest and largest values
        centered_average_response = self.client.post(
            "/centered_average/", {"nums": "1, 1, 5, 5, 10, 8, 7"}
        )
        self.assertContains(centered_average_response, "5")

        # Test case 3: Negative values
        centered_average_response = self.client.post(
            "/centered_average/", {"nums": "-10, -4, -2, -4, -2, 0"}
        )
        self.assertContains(centered_average_response, "-3")


class NoTeenSumViewTestCase(TestCase):
    def test_no_teen_sum_view(self):
        # Test the no_teen_sum_view with different inputs

        # Test case 1: No teens present
        no_teen_sum_response = self.client.post(
            "/no_teen_sum/", {"a": 1, "b": 2, "c": 3}
        )
        self.assertContains(no_teen_sum_response, "6")

        # Test case 2: Teen present, but not counting as 0
        no_teen_sum_response = self.client.post(
            "/no_teen_sum/", {"a": 2, "b": 13, "c": 1}
        )
        self.assertContains(no_teen_sum_response, "3")

        # Test case 3: Teen present, counting as 0
        no_teen_sum_response = self.client.post(
            "/no_teen_sum/", {"a": 2, "b": 1, "c": 14}
        )
        self.assertContains(no_teen_sum_response, "3")

        # Test case 4: All teens
        no_teen_sum_response = self.client.post(
            "/no_teen_sum/", {"a": 14, "b": 15, "c": 19}
        )
        self.assertContains(no_teen_sum_response, "0")

    def test_fix_teen(self):
        # Test the fix_teen helper function

        # Test case 1
        fix_teen_result = fix_teen(14)
        self.assertEqual(fix_teen_result, 0)

        # Test case 2
        fix_teen_result = fix_teen(15)
        self.assertEqual(fix_teen_result, 15)

        # Test case 3
        fix_teen_result = fix_teen(17)
        self.assertEqual(fix_teen_result, 0)
