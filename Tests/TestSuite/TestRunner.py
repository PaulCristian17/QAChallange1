import sys
import os

sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from Tests.Scripts.TestBasicForm  import SimpleForm
from Tests.Scripts.TestAlertsModals import BaseAlertsModals
from Tests.Scripts.TestLists import List

if __name__ == "__main__":
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(SimpleForm),
        test_loader.loadTestsFromTestCase(BaseAlertsModals),
        test_loader.loadTestsFromTestCase(List),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

